users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"},
]

friendships = [
    (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
]

# свойство friends содержит друзей для пользователя user
for user in users:
    user["friends"] = []

for i, j in friendships:
    # это работает, потому что users[i] - это пользователь,
    # чей id равен i
    users[i]["friends"].append(users[j]) # добавить j как друга для i
    users[j]["friends"].append(users[i]) # добавить i как друга для j

