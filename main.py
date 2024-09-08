import json
import pprint

followers = []

with open('followers_1.json', 'r') as data:
    follower_data = json.load(data)

for follower in follower_data:
    for name in follower['string_list_data']:
      followers.append(name['value'])

amount_followers = len(followers)
print(f'followers: {amount_followers}')

# Load the data from the JSON file
with open('following.json', 'r') as file:
    following_data = json.load(file)

following_values = []

for following in following_data['relationships_following']:
    for item in following['string_list_data']:
        following_values.append(item['value'])

amount_following = len(following_values)
print(f'following: {amount_following}')


not_following_back = []


for i in range (0, len(following_values)):
  if following_values[i] not in followers:
    not_following_back.append(following_values[i])


for not_following in not_following_back:
    print(not_following)