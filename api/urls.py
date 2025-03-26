from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    HomePageAPIView,
    ContactMessageCreateAPIView,
    SliderViewSet,
    CategoryViewSet,
    ProductViewSet,
    SolutionViewSet,
    DocumentViewSet,
    AboutUsViewSet,
    ServicesViewSet
)

router = DefaultRouter()
router.register(r'sliders', SliderViewSet, basename="sliders")
router.register(r'categories', CategoryViewSet, basename="categories")
router.register(r'products', ProductViewSet, basename="products")
router.register(r'solutions', SolutionViewSet, basename="solutions")
router.register(r'documents', DocumentViewSet, basename="documents")
router.register(r'about-us', AboutUsViewSet, basename="about-us")
router.register(r'our-Services', ServicesViewSet, basename="our-Services")

urlpatterns = [
    path('', include(router.urls)),
    path('home/', HomePageAPIView.as_view(), name='home-page'),
    path('contact/', ContactMessageCreateAPIView.as_view(), name='contact'),
]
