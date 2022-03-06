import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
# Import settings
django.setup()

from faker import Faker
from AppTwo.models import User

fakegen = Faker()

def populate(N=5):

    for entry in range(N):
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        user = User.objects.get_or_create(First_Name=fake_first_name,Last_Name=fake_last_name,Email=fake_email)


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')