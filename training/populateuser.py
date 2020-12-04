import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','training.settings')
import django
django.setup()

from app.models import User
from faker import Faker

fake = Faker()

def populate(n):
    for i in range(n):
        s = User.objects.get_or_create(first_name=fake.name(),last_name = fake.name(),email = fake.email())[0]


if __name__ == '__main__':
    populate(20)
    print("populated")
