import random

data = []

for i in range(10):
    user = {
        "user_id": i + 1,
        "daily_app_opens": random.randint(1, 20),
        "avg_session_duration": round(random.uniform(1, 30), 2)
    }
    data.append(user)

print(data)