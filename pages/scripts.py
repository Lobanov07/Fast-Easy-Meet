from accounts.models import CustomUser
from .models import Meeting, Schedule
from faker import Faker
import random
from django.utils import timezone
from datetime import timedelta

fake = Faker()

def create_femadmin():
    try:
        femadmin = CustomUser.objects.get(username='FEMadmin')
        print("Пользователь FEMadmin уже существует.")
    except CustomUser.DoesNotExist:
        femadmin = CustomUser.objects.create_superuser(
            username='FEMadmin',
            password='adminpassword123',
            email='femadmin@example.com'
        )
        print("Пользователь FEMadmin был создан.")
    return femadmin

def create_users(num_users=10):
    users = []
    existing_usernames = set()

    for _ in range(num_users):
        username = fake.user_name()

        while username in existing_usernames:
            username = fake.user_name()

        existing_usernames.add(username)

        user = CustomUser(
            username=username,
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            password=fake.password(),
            bio=fake.text(),
            date_of_birth=fake.date_of_birth(),
            phone_number=fake.phone_number(),
            profile_picture=None,
        )
        users.append(user)

    CustomUser.objects.bulk_create(users)
    print(f"{num_users} пользователей успешно созданы!")
    return users



def create_meeting():
    femadmin = create_femadmin()

    meeting = Meeting.objects.create(
        title="Общее собрание",
        host=femadmin,
        status="Запланировано",
    )

    print(f'Встреча "{meeting.title}" была создана с хостом {meeting.host.username}, время начала: {meeting.date_time}')
    
    return meeting

def assign_users_to_meeting(meeting):
    users = CustomUser.objects.all()
    meeting.participants.set(users)
    print(f"{len(users)} пользователей были добавлены к встрече.")

def create_schedules_for_all_users():
    users = CustomUser.objects.all()
    for user in users:
        create_random_schedule_for_user(user)
    print(f"Созданы случайные расписания для {len(users)} пользователей на 15 декабря.")


def create_random_schedule_for_user(user):
    """
    Функция генерирует три случайных расписания для каждого пользователя на 15 декабря.
    """
    schedules = []

    fixed_date = timezone.make_aware(timezone.datetime(2024, 12, 15, 0, 0))
    for _ in range(3):
        random_hour = random.randint(8, 18)
        random_minute = random.randint(0, 59)
        start_time = fixed_date + timedelta(hours=random_hour, minutes=random_minute)

        duration_minutes = random.randint(30, 120)
        end_time = start_time + timedelta(minutes=duration_minutes)

        schedule = Schedule(
            user=user,
            start_time=start_time,
            end_time=end_time,
            description=f"Случайное расписание для пользователя {user.username} на 15 декабря"
        )
        schedules.append(schedule)

    Schedule.objects.bulk_create(schedules)
    print(f"Созданы 3 случайных расписания для пользователя {user.username} на 15 декабря")
