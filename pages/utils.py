from datetime import timedelta, datetime
from django.utils import timezone


def generate_possible_times(preferred_date):
    """generate_possible_times."""
    possible_times = []

    start_of_day = datetime.combine(
        preferred_date, datetime.min.time()
        )

    start_of_day = timezone.make_aware(
        start_of_day, timezone.get_current_timezone()
        )

    for i in range(0, 23): 
        possible_times.append(start_of_day + timedelta(hours=i))

    return possible_times


def count_available_participants(time, schedules):
    """count_available_participants."""
    available_participants = 0

    for schedule in schedules.values():
        for schedule_item in schedule:

            local_start_time = timezone.localtime(
                schedule_item.start_time, timezone.get_current_timezone()
                )

            local_end_time = timezone.localtime(
                schedule_item.end_time, timezone.get_current_timezone()
                )

            if not (local_start_time <= time < local_end_time):
                available_participants += 1

    return available_participants
