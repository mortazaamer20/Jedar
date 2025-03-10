from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name="العنوان")
    description = models.TextField(blank=True, verbose_name="الوصف")
    image = models.ImageField(upload_to='sliders/', verbose_name="الصورة")
    link = models.URLField(blank=True, verbose_name="رابط إضافي")
    is_active = models.BooleanField(default=True, verbose_name="نشط")

    class Meta:
        verbose_name = "الصور في الصفحة الرئيسية"  # Singular display name
        verbose_name_plural = "الصور في الصفحة الرئيسية"  # Plural display name


    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "الفئات"  # Singular display name
        verbose_name_plural = "الفئات"  # Plural display name


    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    pdf = models.FileField(upload_to='product_docs/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    class Meta:
        verbose_name = "المنتجات"  # Singular display name
        verbose_name_plural = "المنتجات"  # Plural display name


    def __str__(self):
        return self.name


class Solution(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='solutions/')
    related_products = models.ManyToManyField(Product, blank=True)
    class Meta:
        verbose_name = "الحلول"  # Singular display name
        verbose_name_plural = "الحلول"  # Plural display name


    def __str__(self):
        return self.title


class Document(models.Model):
    DOC_TYPES = [
        ('catalog', 'كتالوج المنتجات'),
        ('presentation', 'العرض التقديمي'),
        ('iso', 'شهادة ISO'),
        ('tds', 'وثيقة بيانات المنتج'),
        ('nano_gel', 'تغنية Nano Gel'),
    ]
    title = models.CharField(max_length=200)
    doc_type = models.CharField(max_length=50, choices=DOC_TYPES)
    file = models.FileField(upload_to='documents/')
    class Meta:
        verbose_name = "المستندات"  # Singular display name
        verbose_name_plural = "المستندات"  # Plural display name


    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone= models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "تواصل معنا"  # Singular display name
        verbose_name_plural = "تواصل معنا"  # Plural display name

    def __str__(self):
        return f"Contact from {self.name} - {self.subject}"
