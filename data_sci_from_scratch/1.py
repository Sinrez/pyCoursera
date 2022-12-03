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
    {"id": 9, "name": "Klein"}
]
# дружеские отношения пользователей
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
# списки друзей пользователей
# for user in users:
#     user["friends"] = []

friendships = {user["id"]: [] for user in users}

# print(*users)


#заполняем друзей
for i, j in friendship_pairs:
    friendships[i].append(j)  # Add j as a friend of user i
    friendships[j].append(i)  # Add i as a friend of user j

# print(friendships)

def number_of_friends(user):
    #ск друзей есть у юзера
    return len(user["friends"])

total_connections = sum(number_of_friends(user) for user in users)

num_users = len(users) # Длина списка пользователей
avg_connections = total_connections / num_users # 24 / 10 = 2.4

