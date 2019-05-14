from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    
    price = models.DecimalField(max_digits=10, decimal_places=0)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='shop/static/img/', blank=True)

    op_sys = models.CharField(max_length=150, default='', null=True, blank = True)
    cpu = models.CharField(max_length=200, default='', null=True, blank = True)
    gpu = models.CharField(max_length=200, default='', null=True, blank = True)
    monitor = models.CharField(max_length=200, default='', null=True, blank = True)
    front_camera = models.CharField(max_length=200, default='', null=True, blank = True)
    behind_camera = models.CharField(max_length=200, default='', null=True, blank = True)
    ram = models.CharField(max_length=200, default='', null=True, blank = True)
    rom = models.CharField(max_length=200, default='', null=True, blank = True)
    battery = models.CharField(max_length=1500, default='', null=True, blank = True)
    advance = models.TextField(blank = True, null = True)
    description = models.TextField(blank=True)
    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])