from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tag.models import Tag
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ..models import Recipe
from ..serializers import RecipeSerializer, TagSerializer
from rest_framework.pagination import PageNumberPagination 
from rest_framework.viewsets import ModelViewSet

class RecipeAPIv2Pagination(PageNumberPagination):
    page_size = 10

class RecipeAPIv2ViewSet(ModelViewSet):
    queryset = Recipe.objects.get_published()
    serializer_class = RecipeSerializer
    pagination_class = RecipeAPIv2Pagination

    def get_queryset(self):
        qs =super().get_queryset()
        category_id = self.request.query_params.get('category_id', None)

        if category_id != '' and category_id.isnumeric():
            qs = qs.filter(category_id=category_id)
        return qs
    

    def partial_update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        recipe = self.get_queryset().filter(pk=pk).first()
        serializer = RecipeSerializer(
            instance=recipe,
            data=request.data,
            many=False,
            context={'request': request},
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
        )

@api_view()
def tag_api_detail(request, pk):
    tag = get_object_or_404(
        Tag.objects.all(),
        pk=pk
    )
    serializer = TagSerializer(
        instance=tag,
        many=False,
        context={'request': request},
    )
    return Response(serializer.data)