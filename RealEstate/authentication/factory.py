import factory
import factory.django
from .models import User, Agent
from faker import Faker
from factory.fuzzy import FuzzyChoice
from django.conf import settings
fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.LazyAttribute(lambda _:fake.unique.first_name().lower())





images = [str(image) for image in settings.HOUSE_IMAGES.iterdir()]


class AgentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Agent

  
    user = factory.SubFactory(UserFactory, is_agent=True)
    about = factory.Faker('sentence')
    country = factory.Faker('country')
    state = factory.Faker('city')
    city = factory.Faker('city')
    zipcode = factory.Faker('zipcode')
    address = factory.Faker('address')
    website = factory.Faker('ascii_company_email')
    license = factory.Faker('isbn10')

    company_name = factory.LazyAttribute(lambda _: fake.company())
    phone = factory.LazyAttribute(lambda _: ''.join(fake.msisdn()[:10]))
    image = factory.django.ImageField(from_path=FuzzyChoice(images))
    
  