# admin.py
from django.contrib import admin
from .models import  Category, Product, Solution, Document,Slider,ContactMessage,AboutUs,AboutUsSection,ProductFile,DocumentFile,Services

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_ar', 'description_ar')

class ProductFileInline(admin.TabularInline): 
    model = ProductFile
    extra = 1 

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name_ar', 'category', 'created_at']
    inlines = [ProductFileInline]
    filter_horizontal = ['related_products']


@admin.register(Services)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['services_name_ar', 'services_name_en', 'created_at']
   


@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    filter_horizontal = ('related_products',)
    list_display = ('title_ar', 'description_ar')

class DocumentFileInline(admin.TabularInline):  
    model = DocumentFile
    extra = 1 

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title_ar', 'title_en']
    inlines = [DocumentFileInline]

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title_ar', 'description_ar', 'is_active')

class AboutUsSectionInline(admin.StackedInline):
    model = AboutUsSection
    extra = 1
    fields = ["section_number", "text_en", "text_ar","image"]
    ordering = ["section_number"]

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    inlines = [AboutUsSectionInline]

    def has_add_permission(self, request):
        """Disallow adding more than one instance"""
        return not AboutUs.objects.exists()

    def has_delete_permission(self, request, obj=None):
        """Allow deleting the single instance"""
        return True  

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')

    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request ):
        return False



admin.site.site_header = "لوحة تحكم جدار"
admin.site.site_title = "جدار"
admin.site.index_title = "مرحبا بك في لوحة تحكم جدار"