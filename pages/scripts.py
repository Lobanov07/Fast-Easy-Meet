from faker import Faker
from accounts.models import CustomUser
from django.utils import timezone
import random
from datetime import timedelta
from .models import Schedule

fake = Faker()


def create_fake_user():

    user = CustomUser.objects.create(
        username=fake.user_name(),
        email=fake.email(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        date_of_birth=fake.date_of_birth(minimum_age=18, maximum_age=80),
        phone_number=fake.phone_number(),
        bio=fake.text(),
    )
    return user


def create_users(num_users=10000):

    users = []
    for _ in range(num_users):
        user = create_fake_user()
        users.append(user)
    print(f'{num_users} пользователей успешно созданы!')


def create_fake_schedule(user, num_entries=10):
    start_time = timezone.now()
    for _ in range(num_entries):

        duration = random.randint(30, 120)
        end_time = start_time + timedelta(minutes=duration)
        description = fake.text(max_nb_chars=200)

        Schedule.objects.create(
            user=user,
            start_time=start_time,
            end_time=end_time,
            description=description
        )

        start_time = end_time + timedelta(minutes=random.randint(10, 60))

def create_schedules_for_all_users():
    users = CustomUser.objects.all()
    for user in users:
        create_fake_schedule(user, num_entries=random.randint(5, 15))
    print("Записи расписания для всех пользователей созданы!")
