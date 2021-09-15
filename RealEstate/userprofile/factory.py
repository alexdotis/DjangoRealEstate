import factory
from factory.declarations import LazyAttribute
from faker import Faker
from .models import  AssignmentProperty
from listing.choices import ESTATE_CATEGORY,PROPERTY_STATUS
from factory.fuzzy import FuzzyChoice
import random
from authentication.factory import UserFactory

fake = Faker()

estate_category = [x[0] for x in ESTATE_CATEGORY]
property_status = [x[0] for x in PROPERTY_STATUS]



class AssignmentPropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model= AssignmentProperty
    
    user = factory.SubFactory(UserFactory,agent=False)
    country = factory.Faker('country')
    region = factory.Faker('city')
    property_type = FuzzyChoice(estate_category)
    status = FuzzyChoice(property_status)
    area = LazyAttribute(lambda _: random.randint(50, 500))
    phone = factory.LazyAttribute(lambda _: ''.join(fake.msisdn()[:10]))


    @factory.post_generation
    def agency(self,create,extracted,**kwargs):
        if not create:
            return 
        if extracted:
            for agency in extracted:
                self.agency.add(agency)
            