import tweepy

bearer_token = "Insert bearer token here"

client=tweepy.Client(bearer_token)

username = "Insert Twitter handle here"

output = client.get_user(username=username)

for i in output.data:
    print(i.id)


