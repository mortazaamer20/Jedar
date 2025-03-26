from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.core.exceptions import ValidationError

class Slider(models.Model):
    title_en = models.CharField(max_length=200, verbose_name="العنوان بالإنجليزية", blank=True, null=True)
    title_ar = models.CharField(max_length=200, verbose_name="العنوان بالعربية", blank=True, null=True)
    description_en = models.TextField(blank=True, verbose_name="الوصف بالإنجليزية", null=True)
    description_ar = models.TextField(blank=True, verbose_name="الوصف بالعربية", null=True)
    image = models.ImageField(upload_to='sliders/', verbose_name="الصورة")
    link = models.URLField(blank=True, verbose_name="رابط إضافي")
    is_active = models.BooleanField(default=True, verbose_name="نشط")
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)

    class Meta:
        verbose_name = "الصور في الصفحة الرئيسية"  
        verbose_name_plural = "الصور في الصفحة الرئيسية" 


    def __str__(self):
        return self.title_ar

class Category(models.Model):
    name_en = models.CharField(max_length=255, verbose_name="الاسم بالإنجليزية")
    name_ar = models.CharField(max_length=255, verbose_name="الاسم بالعربية")
    description_en = models.TextField(blank=True, verbose_name="الوصف بالإنجليزية")
    description_ar = models.TextField(blank=True, verbose_name="الوصف بالعربية")
    image = models.ImageField(upload_to='categories/', null=True,verbose_name="الصورة")
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True,verbose_name="تاريخ الإضافة")

    class Meta:
        verbose_name = "الفئات"  
        verbose_name_plural = "الفئات" 


    def __str__(self):
        return self.name_ar


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,verbose_name="الفئة")
    name_en = models.CharField(max_length=255, verbose_name="الاسم بالإنجليزية")
    name_ar = models.CharField(max_length=255, verbose_name="الاسم بالعربية")
    description_en = models.TextField(verbose_name="الوصف بالإنجليزية")
    description_ar = models.TextField(verbose_name="الوصف بالعربية")
    image = models.ImageField(upload_to='products/',verbose_name="الصورة")
    related_products = models.ManyToManyField(
        'self',
        blank=True,
        verbose_name="منتجات قد تعجبك",
        symmetrical=False
    )
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True,verbose_name="تاريخ الإضافة")
    class Meta:
        verbose_name = "المنتجات" 
        verbose_name_plural = "المنتجات" 


    def __str__(self):
        return self.name_ar

    
class ProductFile(models.Model):
    product = models.ForeignKey(Product, related_name='files', on_delete=models.CASCADE,verbose_name="المنتج")
    file = models.FileField(upload_to='product_docs/',verbose_name="الملف")

    def __str__(self):
        return f"File for {self.product.name_ar}"


class Services(models.Model):
    services_name_ar = models.CharField(max_length=255, verbose_name="اسم الخدمة بالعربية")
    services_name_en = models.CharField(max_length=255, verbose_name="اسم الخدمة بالإنجليزية")
    description_ar = models.TextField(verbose_name="الوصف بالعربية")
    description_en = models.TextField(verbose_name="الوصف بالإنجليزية")
    image = models.ImageField(upload_to='projects/', verbose_name="الصورة")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")

    class Meta:
        verbose_name = "الخدمات"
        verbose_name_plural = "الخدمات"

    def __str__(self):
        return self.services_name_ar




class Solution(models.Model):
    title_en = models.CharField(max_length=255, verbose_name="العنوان بالإنجليزية")
    title_ar = models.CharField(max_length=255, verbose_name="العنوان بالعربية")
    description_en = CKEditor5Field(verbose_name="الوصف بالإنجليزية")
    description_ar = CKEditor5Field(verbose_name="الوصف بالعربية")
    image = models.ImageField(upload_to='solutions/',verbose_name="الصورة")
    related_products = models.ManyToManyField(Product, blank=True,verbose_name="المواد المستخدمة")
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True,verbose_name="تاريخ الإضافة")
    class Meta:
        verbose_name = "الحلول" 
        verbose_name_plural = "الحلول"  


    def __str__(self):
        return self.title_ar


class Document(models.Model):
    title_en = models.CharField(max_length=200, verbose_name="العنوان بالإنجليزية")
    title_ar = models.CharField(max_length=200, verbose_name="العنوان بالعربية") 
    image = models.ImageField(upload_to='documentsImages/', null=True, blank=True,verbose_name="الصورة")
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True,verbose_name="تاريخ الإضافة")
    
    class Meta:
        verbose_name = "المستندات"  
        verbose_name_plural = "المستندات"  

    def __str__(self):
        return self.title_ar

class DocumentFile(models.Model):
    document = models.ForeignKey(Document, related_name='files', on_delete=models.CASCADE,verbose_name="المستند")
    file = models.FileField(upload_to='documents/',verbose_name="الملف")

    def __str__(self):
        return f"File for {self.document.title_ar}"


class AboutUs(models.Model):
    title_en = models.CharField(max_length=100, default="About Us", verbose_name="العنوان بالإنجليزية")
    title_ar = models.CharField(max_length=100, default="نبذة عنا", verbose_name="العنوان بالعربية")


    def save(self, *args, **kwargs):
        
        if AboutUs.objects.exists() and not self.pk:
            raise ValueError("يسمح بأدخال نبذة عنا واحدة فقط")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_ar
    class Meta:
        verbose_name = "نبذة عنا "
        verbose_name_plural = "نبذة عنا "

class AboutUsSection(models.Model):
    
    about_us = models.ForeignKey(AboutUs, related_name="sections", on_delete=models.CASCADE, verbose_name="نبذة عنا")
    section_number = models.PositiveSmallIntegerField(verbose_name="رقم القسم", unique=True)
    text_en = models.TextField(verbose_name="النص بالإنجليزية")
    text_ar = models.TextField(verbose_name="النص بالعربية")
    image = models.ImageField(upload_to="about_us/", blank=True, null=True, verbose_name="الصورة")

    class Meta:
        ordering = ["section_number"]
        unique_together = ("about_us", "section_number")
        verbose_name = "نبذة عنا "  
        verbose_name_plural = "نبذة عنا "

    def __str__(self):
        return f"Section {self.section_number} - {self.text_ar[:30]}..."
    
          


class ContactMessage(models.Model):
    name = models.CharField(max_length=255, verbose_name="الاسم")
    email = models.EmailField(verbose_name="البريد الإلكتروني")
    phone= models.CharField(max_length=255, verbose_name="رقم الهاتف")
    subject = models.CharField(max_length=255, verbose_name="الموضوع")
    message = models.TextField(verbose_name="الرسالة")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="تاريخ الإرسال")
    class Meta:
        verbose_name = "تواصل معنا"  
        verbose_name_plural = "تواصل معنا"  

    def __str__(self):
        return f"Contact from {self.name} - {self.subject}"
