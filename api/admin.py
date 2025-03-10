# admin.py
from django.contrib import admin
from .models import  Category, Product, Solution, Document,Slider,ContactMessage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')

@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    filter_horizontal = ('related_products',)
    list_display = ('title', 'description')

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'doc_type')

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_active')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')



admin.site.site_header = "Jidar Admin Panel"
admin.site.site_title = "Jidar Admin"
admin.site.index_title = "Welcome to Jidar Admin Dashboard"