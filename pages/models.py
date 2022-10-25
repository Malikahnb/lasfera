from django.db import models
from django.utils.translation import gettext_lazy as _


class HomeModel(models.Model):
    banner = models.ImageField(upload_to='banner', null=True, blank=True, verbose_name=_('banner'))
    title = models.CharField(max_length=255, verbose_name=_('title'))
    description = models.CharField(max_length=255, verbose_name=_('description'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('home')
        verbose_name_plural = _('homes')


class PopularModel(models.Model):
    image = models.ImageField(upload_to='category', verbose_name=_('image'))
    name = models.CharField(max_length=50, verbose_name=_('name'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('popular')
        verbose_name_plural = _('populars')


class ServicesModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('service')
        verbose_name_plural = _('services')