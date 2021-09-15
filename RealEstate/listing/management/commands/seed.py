
from django.core.management.base import BaseCommand
from listing.factory import ListingFactory, ExtraFeatureFactory, ListingImageFactory
from authentication.factory import AgentFactory, UserFactory
from authentication.models import Agent, User
from allauth.account.models import EmailAddress
from blogs.factory import BlogFactory
from userprofile.factory import AssignmentPropertyFactory


class Command(BaseCommand):
    help = 'Seed the database'

    def add_arguments(self, parser) -> None:
        parser.add_argument('--properties', default=20,
                            type=int, help='The number of fake properties')

        parser.add_argument('--agents', default=10, type=int,
                            help='The number of fake agents')

        parser.add_argument('--blogs', default=30, type=int,
                            help='The number of fake blogs')

        parser.add_argument('--users', default=10, type=int,
                            help='The number of users')

    def handle(self, *args, **options):
        

        for _ in range(options['agents']):
            agent = AgentFactory.create()

            for _ in range(options['properties']):
                pr = ListingFactory.create(agent=agent)
                for _ in range(20):
                    ExtraFeatureFactory.create(listing=pr)
                for _ in range(4):
                    ListingImageFactory.create(listing=pr)


        print('Completed first stage...please wait')
        agents = Agent.objects.all()
        for _ in range(options['users']):
            usr = UserFactory.create()
            AssignmentPropertyFactory.create(user=usr, agency=agents)

        users = User.objects.all()
        for user in users:
            user.set_password('qwerty')
            user.save()
            EmailAddress.objects.create(
                user_id=user.id, email=user.email, verified=True, primary=True)

        for _ in range(options['blogs']):
            BlogFactory.create()

        print('Done!!')
