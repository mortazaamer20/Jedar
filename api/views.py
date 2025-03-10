from rest_framework import viewsets, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Slider, Category, Product, Solution, Document, ContactMessage
from .serializers import (
    SliderSerializer, CategorySerializer, ProductSerializer,
    SolutionSerializer, DocumentSerializer, ContactMessageSerializer
)
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets

class SliderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'description'] 
    ordering_fields = ['name', 'created_at']


class SolutionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['title']

class DocumentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title']


class HomePageAPIView(APIView):
    def get(self, request, *args, **kwargs):
        slider = Slider.objects.all()
        featured_products = Product.objects.all()[:3]
        featured_solutions = Solution.objects.all()[:3]
        documents = Document.objects.all() 
        data = {
            "slider": SliderSerializer(slider, many=True, context={"request": request}).data,
            "featured_products": ProductSerializer(featured_products, many=True, context={"request": request}).data,
            "featured_solutions": SolutionSerializer(featured_solutions, many=True, context={"request": request}).data,
            "documents": DocumentSerializer(documents, many=True, context={"request": request}).data,
        }
        return Response(data)



class ContactMessageCreateAPIView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
