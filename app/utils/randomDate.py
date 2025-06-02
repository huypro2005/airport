import random
from datetime import datetime, timedelta


def random_date(start, end):
    """Generate a random datetime between two datetime objects."""
    delta = end - start
    random_days = random.randint(0, delta.days)
    random_seconds = random.randint(0, 86400)  # 24 hours in seconds
    return start + timedelta(days=random_days, seconds=random_seconds)


# print(random_date(datetime(2025, 1, 1), datetime(2025, 12, 31)).date())