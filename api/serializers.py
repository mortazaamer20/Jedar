from rest_framework import serializers
from .models import Slider, Category, Product, Solution, Document, ContactMessage,AboutUsSection,AboutUs,DocumentFile,ProductFile,Services

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFile
        fields = '__all__'

class RelatedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name_en', 'name_ar',,'description_en','description_ar'  'image']

class ProductSerializer(serializers.ModelSerializer):
    files = ProductFileSerializer(many=True, read_only=True)
    related_products = RelatedProductSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    
    class Meta:
        model = Product
        fields=['id','name_en','name_ar','description_en','description_ar','image','category','category_id','related_products','files','created_at']



class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class SolutionSerializer(serializers.ModelSerializer):
    related_products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Solution
        fields = '__all__'

class DocumentFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentFile
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    files = DocumentFileSerializer(many=True, read_only=True)
    class Meta:
        model = Document
        fields = ['id', 'title_en', 'title_ar', 'image', 'files', 'created_at']


class AboutUsSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsSection
        fields = '__all__'

class AboutUsSerializer(serializers.ModelSerializer):
    sections = AboutUsSectionSerializer(many=True)

    class Meta:
        model = AboutUs
        fields = '__all__'

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'


class HomePageSerializer(serializers.Serializer):
    slider = SliderSerializer(many=True)
    featured_products = ProductSerializer(many=True)
    featured_solutions = SolutionSerializer(many=True)
    about_us = AboutUsSerializer(many=True)
    Service = ServicesSerializer(many=True)