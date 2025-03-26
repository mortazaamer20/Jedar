from rest_framework import viewsets, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Slider, Category, Product, Solution, Document, ContactMessage,AboutUs,Services
from .serializers import (
    SliderSerializer, 
    CategorySerializer,
    ProductSerializer,
    SolutionSerializer,
    DocumentSerializer,
    ContactMessageSerializer,
    AboutUsSerializer,
    ServicesSerializer,
    HomePageSerializer,
)
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from collections import defaultdict

class SliderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Slider.objects.all().order_by('-created_at')
    serializer_class = SliderSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all().order_by('-created_at')
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name_ar', 'description_ar', 'name_en', 'description_en']
    ordering_fields = ['name_ar','name_en', 'created_at']


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name_ar', 'description_ar', 'name_en', 'description_en'] 
    ordering_fields = ['name_ar', 'created_at', 'category', 'name_en']
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'minimal',
                openapi.IN_QUERY,
                description="Set to 'true' to return only 'name_en' ,'name_ar', 'description_en','description_en' and 'image'",
                type=openapi.TYPE_BOOLEAN
            )
        ],
        responses={
            200: ProductSerializer(many=True),
        }
    )
    def list(self, request, *args, **kwargs):
        """Get all products. Use `minimal=true` to retrieve only name_en , name_ar & image."""
        minimal = request.query_params.get('minimal') == 'true'
        products = self.get_queryset()

        grouped_data = defaultdict(list)
        for product in products:
            category_name = product.category.name_en if product.category else "Uncategorized"
            product_data = {
                "id": product.id,
                "name_en": product.name_en,
                "name_ar": product.name_ar,
                "description_en": product.description_en,
                "description_ar": product.description_ar,
                "image": product.image.url if product.image else None,
            } if minimal else ProductSerializer(product).data

            grouped_data[category_name].append(product_data)

        return Response(grouped_data)


class ServicesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Services.objects.all().order_by('-created_at')
    serializer_class = ServicesSerializer

class SolutionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Solution.objects.all().order_by('-created_at')
    serializer_class = SolutionSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title_ar', 'description_ar', 'title_en', 'description_en']
    ordering_fields = ['title_ar', 'title_en', 'created_at']

class DocumentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Document.objects.all().order_by('-created_at')
    serializer_class = DocumentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title_ar', 'title_en']
    ordering_fields = ['title_ar', 'title_en', 'created_at']


class HomePageAPIView(APIView):
    serializer_class = HomePageSerializer

    @swagger_auto_schema(
        operation_summary="Retrieve Home Page Data",
        operation_description=(
            "This endpoint returns all necessary data for the home page including slider images, "
            "featured products, featured solutions, about-us details, and services."
        ),
        responses={
            200: openapi.Response(
                description="Successful retrieval of home page data",
                examples={
                    "application/json": {
                        "slider": [
                            {
                                "id": 1,
                                "title_en": "Slider Title EN",
                                "title_ar": "Slider Title AR",
                                "description_en": "Slider description EN",
                                "description_ar": "Slider description AR",
                                "image": "https://example.com/media/sliders/image1.jpg",
                                "link": "https://example.com",
                                "is_active": True,
                                "created_at": "2025-03-26T12:00:00Z"
                            }
                        ],
                        "featured_products": [
                            {
                                "id": 1,
                                "name_en": "Product Name EN",
                                "name_ar": "Product Name AR",
                                "description_en": "Product description EN",
                                "description_ar": "Product description AR",
                                "image": "https://example.com/media/products/image1.jpg",
                                "related_products": [],
                                "created_at": "2025-03-26T12:00:00Z"
                            }
                        ],
                        "featured_solutions": [
                            {
                                "id": 1,
                                "title_en": "Solution Title EN",
                                "title_ar": "Solution Title AR",
                                "description_en": "Solution description EN",
                                "description_ar": "Solution description AR",
                                "image": "https://example.com/media/solutions/image1.jpg",
                                "related_products": [],
                                "created_at": "2025-03-26T12:00:00Z"
                            }
                        ],
                        "about-us": [
                            {
                                "id": 1,
                                "title_en": "About Us",
                                "title_ar": "نبذة عنا",
                                "sections": [
                                    {
                                        "id": 1,
                                        "section_number": 1,
                                        "text_en": "About us text EN",
                                        "text_ar": "About us text AR",
                                        "image": "https://example.com/media/about_us/section1.jpg"
                                    }
                                ]
                            }
                        ],
                        "Service": [
                            {
                                "id": 1,
                                "services_name_en": "Service Name EN",
                                "services_name_ar": "Service Name AR",
                                "description_en": "Service description EN",
                                "description_ar": "Service description AR",
                                "image": "https://example.com/media/projects/service1.jpg",
                                "created_at": "2025-03-26T12:00:00Z"
                            }
                        ]
                    }
                }
            )
        }
    )
    

    def get(self, request, *args, **kwargs):
        slider = Slider.objects.all().order_by('-created_at')
        featured_products = Product.objects.all().order_by('-created_at')[:5]
        featured_solutions = Solution.objects.all().order_by('-created_at')[:5]
        aboutus = AboutUs.objects.all()[:1]
        Service = Services.objects.all().order_by('-created_at')
        data = {
            "slider": SliderSerializer(slider, many=True, context={"request": request}).data,
            "featured_products": ProductSerializer(featured_products, many=True, context={"request": request}).data,
            "featured_solutions": SolutionSerializer(featured_solutions, many=True, context={"request": request}).data,
            "about_us": AboutUsSerializer(aboutus, many=True, context={"request": request}).data,
            "Service": ServicesSerializer(Service, many=True, context={"request": request}).data,
        }
        return Response(data)



class AboutUsViewSet(viewsets.ReadOnlyModelViewSet):  
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        """Ensure only one instance is returned"""
        return AboutUs.objects.all()[:1]


class ContactMessageCreateAPIView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
