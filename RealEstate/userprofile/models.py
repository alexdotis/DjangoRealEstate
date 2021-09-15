from django.db import models
from django.core.validators import RegexValidator
from listing.choices import ESTATE_CATEGORY, PROPERTY_STATUS


class AssignmentProperty(models.Model):
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    country = models.CharField(verbose_name='country', max_length=100)
    region = models.CharField(verbose_name='region', max_length=100)
    property_type = models.CharField(verbose_name='type',
                                     choices=ESTATE_CATEGORY, max_length=100)
    status = models.CharField(verbose_name='status',
                              choices=PROPERTY_STATUS, max_length=20)
    area = models.PositiveIntegerField(verbose_name='area', default=0)
    phone = models.CharField(verbose_name='phone', validators=[RegexValidator(r'\d{10}')],
                             max_length=10)
    agency = models.ManyToManyField('authentication.Agent')
    is_assigned = models.BooleanField(
        verbose_name='is_assigned', default=False)
    created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.user}'

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'Assginment Properties'
