from datetime import timedelta, datetime
from django.utils import timezone


def find_time(schedules, preferred_date):
    possible_times = []

    start_of_day = datetime.combine(preferred_date, datetime.min.time())
    start_of_day = timezone.make_aware(start_of_day, timezone.get_current_timezone())

    for i in range(0, 24):
        start_time = start_of_day + timedelta(hours=i)
        end_time = start_time + timedelta(hours=1)
        possible_times.append((start_time, end_time))

    bids = {f"{slot[0].strftime('%H:%M')}-{slot[1].strftime('%H:%M')}": 0 for slot in possible_times}

    for participant, participant_schedules in schedules.items():
        for schedule in participant_schedules:
            for slot_start, slot_end in possible_times:
                if schedule.start_time <= slot_start and schedule.end_time >= slot_end:
                    bids[f"{slot_start.strftime('%H:%M')}-{slot_end.strftime('%H:%M')}"] += 1

    best_slot = min(bids, key=bids.get)

    best_start_time = datetime.strptime(best_slot.split('-')[0], "%H:%M")

    best_time = start_of_day.replace(hour=best_start_time.hour, minute=best_start_time.minute)

    return best_time
