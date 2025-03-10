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
)

router = DefaultRouter()
router.register(r'sliders', SliderViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'solutions', SolutionViewSet)
router.register(r'documents', DocumentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('home/', HomePageAPIView.as_view(), name='home-page'),
    path('contact/', ContactMessageCreateAPIView.as_view(), name='contact'),
]
