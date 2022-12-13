import tweepy

bearer_token = "Insert bearer token here"

client=tweepy.Client(bearer_token)

user_id = "insert target user id here"
recent = 2022-12-01

output = client.get_users_tweets(id=user_id, end_time=recent, max_results=10)

for i in output.data:
    print(i.id)
    print(i.text)
