from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import json

def home(request):
    if request.method == 'POST':
        followers_file = request.FILES.get('followerFile')
        following_file = request.FILES.get('followingFile')
        if followers_file and following_file:
            followers_content = followers_file.read().decode('utf-8')
            following_content = following_file.read().decode('utf-8')

            try:
                num_follower, num_following, notFollowingBack = getBadFollowers(followers_content, following_content)
                # print(num_follower)
                # print(notFollowingBack)
                followerUploaded = True
                followingUploaded = True
            except (json.JSONDecodeError, KeyError) as e:
                num_follower, num_following, notFollowingBack = 0, 0, []
                followerUploaded = False
                followingUploaded = False
        else:
            num_follower, num_following, notFollowingBack = 0, 0, []
            followerUploaded = False
            followingUploaded = False

        context = {
            'followerUploaded': followerUploaded,
            'followingUploaded': followingUploaded,
            'num_follower': num_follower,
            'num_following': num_following,
            'notFollowingBack': notFollowingBack
        }
        return render(request, 'home.html', context=context)
    return render(request, 'home.html')

def getBadFollowers(follower_json_str, following_json_str):
    followers = []

    follower_data = json.loads(follower_json_str)
    for follower in follower_data:
        for name in follower['string_list_data']:
            followers.append(name['value'])

    amount_followers = len(followers)

    ########################################################

    following_values = []

    following_data = json.loads(following_json_str)
    for following in following_data['relationships_following']:
        for item in following['string_list_data']:
            following_values.append(item['value'])

    amount_following = len(following_values)

    ########################################################

    not_following_back = [person for person in following_values if person not in followers]

    return amount_followers, amount_following, not_following_back