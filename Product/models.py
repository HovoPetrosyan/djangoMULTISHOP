from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db.models import Count, Sum, Avg


# Create your models here.
class Category(MPTTModel):
    status = (
        ('True', 'True'),
        ('False', 'False'),
    )
    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children'
    )
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='category/')
    status = models.CharField(max_length=20, choices=status)
    slug = models.SlugField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title


class Stock(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='stock/')
    slug = models.SlugField(null=True, unique=True)
    crated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def stock_image_url(self):
        if self.image:
            return self.image.url
        else:
            return ""

    def get_absolute_url(self):
        return reverse('product_element', kwargs={'slug': self.slug})


class Product(models.Model):
    status = (
        ('True', 'True'),
        ('False', 'False'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='product/')
    new_price = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    old_price = models.DecimalField(decimal_places=2, max_digits=15)
    amount = models.IntegerField(default=0)
    detail = models.TextField()
    status = models.CharField(max_length=20, choices=status)
    slug = models.SlugField(null=True, unique=True)
    crated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" heights="70" width="60" />'.format(self.image.url))

    image_tag.short_description = 'Image'

    def ImageURL(self):
        if self.image:
            return self.image.url
        else:
            return ""

    def get_absolute_url(self):
        return reverse('product_element', kwargs={'slug': self.slug})

    def average_review(self):
        reviews = Comment.objects.filter(product=self, status=True).aggregate(average=Avg('rate'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
            return avg
        else:
            return avg

    def total_review(self):
        reviews = Comment.objects.filter(product=self, status=True).aggregate(count=Count('id'))
        cnt = 0
        if reviews['count'] is not None:
            cnt = float(reviews['count'])
            return cnt


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(blank=True, upload_to='product/')

    def __str__(self):
        return self.title


class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200, blank=True)
    comment = models.TextField(max_length=3000, blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=40, choices=STATUS, default='New')
    crated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']
