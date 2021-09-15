import factory
from factory.declarations import LazyAttribute
import factory.django
from factory.fuzzy import FuzzyChoice
from faker import Faker
from .models import Listing, ListingImages, ExtraFeature
from .choices import ESTATE_CATEGORY, SUBCATECORY, PROPERTY_STATUS
from authentication.factory import AgentFactory
import random
from django.conf import settings
fake = Faker()

images = [str(image) for image in settings.HOUSE_IMAGES.iterdir()]
estate_category = [x[0] for x in ESTATE_CATEGORY]
subcategory = [x[0] for x in SUBCATECORY]
property_status = [x[0] for x in PROPERTY_STATUS]


class ListingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Listing
    
    agent = factory.SubFactory(AgentFactory)
    title =LazyAttribute(lambda _: fake.unique.text(max_nb_chars=20))
    description = factory.LazyAttribute(
        lambda _: ''.join(fake.text() for i in range(5)))
    property_type = FuzzyChoice(estate_category)
    subcategory = FuzzyChoice(subcategory)
    status = FuzzyChoice(property_status)
    bedrooms = LazyAttribute(lambda _: random.randint(1, 5))
    bathrooms = LazyAttribute(lambda _: random.randint(1, 5))
    rooms = LazyAttribute(lambda _: random.randint(1, 5))
    floors = LazyAttribute(lambda _: random.randint(1, 5))
    garages = LazyAttribute(lambda _: random.randint(1, 5))
    area = LazyAttribute(lambda _: random.randint(50, 5000))
    price = LazyAttribute(lambda _: fake.random_number(4))
    property_id = factory.Faker('isbn10')
    address = factory.Faker('address')
    country = factory.Faker('country')
    city = factory.Faker('city')
    state = factory.Faker('state')
    postal_code = factory.Faker('zipcode')
    active = True
    created_at = LazyAttribute(
        lambda _: fake.date_time_this_year().strftime('%Y-%m-%d %H=%M=%S'))
    updated_at = LazyAttribute(
        lambda _: fake.date_time_this_month().strftime('%Y-%m-%d %H=%M:%S'))
    image = factory.django.ImageField(from_path=FuzzyChoice(images))



class ExtraFeatureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ExtraFeature
    
    listing = factory.SubFactory(ListingFactory)
    feature = LazyAttribute(lambda _:fake.text(max_nb_chars=10)) 
    choice = LazyAttribute(lambda x:random.choice(ExtraFeature.CHOICES)[0])


class ListingImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ListingImages
    
    listing = factory.SubFactory(ListingFactory)
    image = factory.django.ImageField(from_path=FuzzyChoice(images))