
from django.urls import reverse_lazy
from django.db import models
from django.utils.translation import ugettext_lazy as _

from slugify import slugify_url

from managers import ProductManager


class Product(models.Model):

    STATUS_VISIBLE =(
        ('visible', 'Visible'),
        ('invisible', 'Invisible')
    )

    is_visible = models.CharField(choices=STATUS_VISIBLE, max_length=255, default=True)

    objects = ProductManager()

    availability = models.BooleanField(_('Availability'), default=False)

    category = models.ForeignKey(
        'categories.Category',
        verbose_name=_('Category'),
        related_name='products',
        on_delete=models.CASCADE
    )

    name = models.CharField(_('Name'), max_length=255, db_index=True)

    price = models.FloatField(_('Price'))

    new_price = models.FloatField(_('Price with sale'), blank=True, null=True)

    logo = models.ImageField(
        _('Logo'), upload_to='product_logos', max_length=255, blank=True, null=True)

    tags = models.TextField(
        _('Tags'),
        max_length=1000,
        db_index=True,
        blank=True)

    description = models.TextField(_('Description'), max_length=1500, blank=True)

    code = models.CharField(_('Code'), max_length=255, blank=True)

    cars = models.CharField(_('Cars'), max_length=255, blank=True)

    year = models.CharField(_('Graduation year'), max_length=255, blank=True)

    manufacturer = models.CharField(_('Manufacturer'), max_length=255, blank=True)

    def __str__(self):
        return self.name

    @property
    def slug(self):
        return slugify_url(self.name) or 'product'

    def get_absolute_url(self):
        return reverse_lazy('products:detail', args=[
            self.category.slug, self.category.id, self.slug, self.id
        ])

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
