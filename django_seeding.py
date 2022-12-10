import factory
import factory.fuzzy
from factory.django import DjangoModelFactory
from django.contrib.auth.hashers import make_password
from accounts.models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('email')
    phone_number = factory.Faker("phone_number")
    email = factory.Faker("email")
    is_active = True
    password = factory.LazyFunction(lambda: make_password('default'))
    
    
from accounts.models import User
from seeders.users.factories import UserFactory

NUM_USER = 100


def run():
    print("------------ Load user data -------------")

    User.objects.all().delete()

    # Add user
    for _ in range(NUM_USER):
        UserFactory()

    print("------------ End user data -------------")
    return
