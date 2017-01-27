# users is a list of dictionaries
users = [
{ "id": 0, "name": "Hero" },
{ "id": 1, "name": "Dunn" },
{ "id": 2, "name": "Sue" },
{ "id": 3, "name": "Chi" },
{ "id": 4, "name": "Thor" },
{ "id": 5, "name": "Clive" },
{ "id": 6, "name": "Hicks" },
{ "id": 7, "name": "Devin" },
{ "id": 8, "name": "Kate" },
{ "id": 9, "name": "Klein" }
]

# this is a list of sets defining pairs of friend relations
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), 
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# for each user, make a list of friends, and add it to the dict
for user in users:
  user["friends"] = []

for i, j in friendships:
  users[i]["friends"].append(j)
  users[j]["friends"].append(i)

# get the avg no of connections in our friendships graph
def number_of_friends(user):
  '''
  gets the no of friends the user has, from the users dict
  '''
  return len(user["friends"])

avg_no_of_connections = sum([number_of_friends(user) for user in users])/float(len(users))
print ('avg no of connections ', avg_no_of_connections)

# get list of user ids sorted in decreasing order of no of friends
connections_list = [[user["id"], len(user["friends"])] for user in users]
connections_list = sorted(connections_list, key = (lambda x: x[1]),  reverse = True)
print (connections_list)

# get a list of friends of friends
def get_friends_of_friends(user):
  return list(set(fof for friend in user["friends"] for fof in users[friend]["friends"] if fof not in user["friends"]))

print (get_friends_of_friends(users[0]))

# it will be a good idea to meet people with similar interests
# following is a list of id, interest
interests = [
(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
(0, "Spark"), (0, "Storm"), (0, "Cassandra"),
(1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
(1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
(2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
(3, "statistics"), (3, "regression"), (3, "probability"),
(4, "machine learning"), (4, "regression"), (4, "decision trees"),
(4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
(5, "Haskell"), (5, "programming languages"), (6, "statistics"),
(6, "probability"), (6, "mathematics"), (6, "theory"),
(7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
(7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
(8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
(9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

# buid a function to get ids of all scientists who share the same interest
def data_scientists_who_like(target_interest):
  return [user_id for user_id, user_interest in interests if user_interest == target_interest]

# since the interests list can be quite big, it will be useful
# to build a mapping from id -> interest and vice versa

from collections import defaultdict
# keys are interests, values are lists of user_ids with that interest
user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
  user_ids_by_interest[interest].append(user_id)

# keys are user_ids, values are lists of interests for that user_id
interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
  interests_by_user_id[user_id].append(interest)

