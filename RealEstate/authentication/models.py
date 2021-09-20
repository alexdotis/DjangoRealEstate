from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    is_agent = models.BooleanField(verbose_name='Agent', default=False)


def image_agent_path(instance,filename):
    return f'Agents/{instance.user.username}/{filename}'

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(verbose_name='About - Description')
    company_name = models.CharField(verbose_name='Company Name', max_length=50)
    country = models.CharField(verbose_name='Country', max_length=80)
    state = models.CharField(verbose_name='State', max_length=80)
    city = models.CharField(verbose_name='City', max_length=80)
    zipcode = models.CharField(verbose_name='Zip Code', validators=[
                               RegexValidator(r'\d{5}')], max_length=5)
    address = models.CharField(verbose_name='Address', max_length=80)
    website = models.CharField(verbose_name='Website', max_length=80)
    license = models.CharField(verbose_name='License', max_length=20)
    phone = models.CharField(verbose_name='phone', validators=[
                             RegexValidator(r'\d{10}')], unique=True, max_length=10)
    image = models.ImageField(verbose_name='image',upload_to=image_agent_path,null=True)

    def __str__(self) -> str:
        return f'{self.user}'

