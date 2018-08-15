from __future__ import division   #integer division is lame
from collections import Counter

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

for user in users:
    user["friends"] = []

for i, j in friendships:
    #this works because users[i] is the user whose id is i
    users[i]["friends"].append(users[j]) # add i as a friend of j
    users[j]["friends"].append(users[i]) # add j as a friend of i
    # break

# print(users[0]["friends"])
def number_of_frieds(user):
    """how many friends does _user_ have?"""
    return len(user["friends"]) #length of friend_ids list

total_connections = sum(number_of_frieds(user)
                        for user in users) #24
print(total_connections)
# print([number_of_frieds(user)
#           for user in users])
num_users = len(users)      #length of the users list
avg_connections = total_connections / num_users    # 2.4
print(avg_connections)

# create a list ( user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_frieds(user))
                     for user in users]

print(num_friends_by_id)

s = sorted(num_friends_by_id,
       key=lambda user: user[1],
       reverse=True)

print(s)

def friends_of_friend_ids_bad(user):
    # "foaf" is short for "friend of a friend"
    return [foaf["id"]
            for friend in user["friends"] # for each of user's friends
            for foaf in friend["friends"]] # get each of _their_ friends

print(friends_of_friend_ids_bad(users[0]))

print([friend["id"] for friend in users[0]["friends"]])
print([friend["id"] for friend in users[1]["friends"]])
print([friend["id"] for friend in users[2]["friends"]])

def not_the_same(user, other_user):
    """two users are not the same if they have different ids"""
    return user["id"] != other_user["id"]

def not_friends(user, other_user):
    """other_user is not a friend if he's not in user["friends"];
    that is, if he's not_the_same as all the people in user["friends"]"""
    return all(not_the_same(friend, other_user)
               for friend in user["friends"])

def friends_of_friend_ids(user):
    return Counter(foaf["id"]
                   for friend in user["friends"] # for each of my friends
                   for foaf in friend["friends"] # count "their" friends
                   if not_the_same(user, foaf) # who aren't me
                   and not_friends(user, foaf)) # and aren't my friends

print(friends_of_friend_ids(users[3]))
