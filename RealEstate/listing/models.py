from django.db import models
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.safestring import mark_safe
from .choices import ESTATE_CATEGORY, SUBCATECORY, PROPERTY_STATUS

from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator


def listing_media_path(instance, filename):
    return f'Properties/{instance.title}/{filename}'


class Listing(models.Model):

    agent = models.ForeignKey('authentication.Agent', on_delete=models.CASCADE)

    title = models.CharField(
        verbose_name='Property Title', max_length=120, unique=True)

    description = models.TextField(
        verbose_name='Property Description')

    property_type = models.CharField(
        choices=ESTATE_CATEGORY, verbose_name='Property Type', max_length=20)

    subcategory = models.CharField(choices=SUBCATECORY, max_length=120)

    status = models.CharField(
        choices=PROPERTY_STATUS, verbose_name='Property Status', max_length=10)

    bedrooms = models.PositiveIntegerField(verbose_name='Bedrooms', default=0)

    bathrooms = models.PositiveIntegerField(
        verbose_name='Bathrooms', default=0)

    rooms = models.PositiveIntegerField(verbose_name='Rooms', default=0)

    floors = models.PositiveIntegerField(verbose_name='Floors', default=0)

    garages = models.PositiveIntegerField(verbose_name='Garages', default=0)

    area = models.PositiveIntegerField(verbose_name='Area', default=0)

    price = models.DecimalField(
        verbose_name='Price', decimal_places=2, max_digits=8)

    property_id = models.CharField(
        verbose_name='Property ID', unique=True, max_length=20)

    address = models.CharField(verbose_name='Address', max_length=120)

    country = models.CharField(verbose_name='Country', max_length=80)

    city = models.CharField(verbose_name='City', max_length=80)

    state = models.CharField(verbose_name='State', max_length=80)

    postal_code = models.CharField(
        verbose_name='Postal Code/Zip', validators=[RegexValidator(r'\d{5}')], max_length=5)

    video = models.FileField(
        verbose_name='Video', upload_to=listing_media_path, blank=True)

    active = models.BooleanField(verbose_name='Active', default=True)

    slug = models.SlugField(blank=True, null=True, editable=False, unique=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    image = models.ImageField(
        verbose_name='Image Property', upload_to=listing_media_path)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" width="60" height="30"/>' % self.image.url)
        else:
            return 'No Image'

    @property
    def price_display(self):
        return '{:,}'.format(self.price)

    @property
    def subcategory_type(self):
        return self.get_subcategory_display()

    class Meta:
        verbose_name_plural = 'Properties'
        ordering = ('-created_at',)


@receiver(pre_save, sender=Listing)
def populate_slug(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)


class ExtraFeature(models.Model):
    YES = 1
    NO = -1
    CHOICES = (
        (YES, 'YES'),
        (NO, 'NO')
    )

    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    feature = models.CharField(verbose_name='Feature name', max_length=25)
    choice = models.IntegerField(verbose_name='choice',
                                 choices=CHOICES)

    def __str__(self) -> str:
        return f'{self.feature}'


def image_property(instance, filename):
    return f'Properties/{instance.listing}/images/{filename}'


class ListingImages(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='image', upload_to=image_property)

    def __str__(self) -> str:
        return f'{self.listing}'

    class Meta:
        verbose_name_plural = 'Property Images'


class ListingReview(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    comment = models.TextField()
    created = models.DateField(auto_now_add=True)
    review = models.PositiveIntegerField(
        default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])

    def __str__(self) -> str:
        return f'{self.property.title}'

    class Meta:
        unique_together = ('user', 'listing')
        verbose_name_plural = 'Property Review'
