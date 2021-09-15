import factory
from factory.declarations import LazyAttribute
from factory.fuzzy import FuzzyChoice
from faker import Faker
from .models import Blog
from django.conf import settings

fake = Faker()

images = [str(image) for image in settings.HOUSE_IMAGES.iterdir()]


class BlogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Blog
    title = LazyAttribute(lambda _: fake.text(max_nb_chars=20))
    text = LazyAttribute(lambda _: ''.join(fake.text() for i in range(20)))
    created_at = LazyAttribute(
        lambda _: fake.date_time_this_year().strftime('%Y-%m-%d %H=%M=%S'))
    image = factory.django.ImageField(from_path=FuzzyChoice(images))
