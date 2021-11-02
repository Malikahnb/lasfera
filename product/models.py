from django.db import models
from django.utils.translation import gettext_lazy as _


class CategoryModel(models.Model):
    parent_menu = models.CharField(max_length=65, verbose_name=_('parent menu'))
    name = models.CharField(max_length=65, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class ColorModel(models.Model):
    color = models.CharField(max_length=50, verbose_name=_('color'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = _('color')
        verbose_name_plural = _('colors')


class SizeModel(models.Model):
    size = models.CharField(max_length=50, verbose_name=_('color'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.size

    class Meta:
        verbose_name = _('size')
        verbose_name_plural = _('sizes')


class ProductModel(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('title'))
    price = models.FloatField(verbose_name=_('price'))
    cover = models.FileField(upload_to='products', verbose_name=_('cover'))
    discount = models.PositiveSmallIntegerField(default=0, verbose_name=_('discount'))
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.PROTECT,
        related_name='product',
        verbose_name=_("category")
    )
    color = models.ManyToManyField(
        ColorModel,
        related_name='product',
        verbose_name=_("color")
    )
    size = models.ManyToManyField(
        SizeModel,
        related_name='product',
        verbose_name=_("size")
    )

    description = models.TextField(null=True, blank=True, verbose_name=_('description'))
    features = models.TextField(null=True, blank=True, verbose_name=_('features'))
    in_stock = models.BooleanField(default=True, verbose_name=_('in stock'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    edited_at = models.DateTimeField(auto_now=True, verbose_name=_('edited at'))

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')


class ProductDetailModel(models.Model):
    title = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE,
        related_name='product',
        verbose_name=_("title")
    )

    images = models.FileField(upload_to='products', verbose_name=_('images'))

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = _('product detail')
        verbose_name_plural = _('product details')
