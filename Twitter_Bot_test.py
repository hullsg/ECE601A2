#Determines if a Twitter account is a bot

import botometer

Rapid_API_Key = "Enter Rapid API Key"

twitter_auth = {
    API_Key = "Enter API Key",
    API_Secret = "Enter API Secret",
    Access_Token = "Enter Access Token",
    Access_Secret = "Enter Access Secret",
}

Botometer_url = https://botometer-pro.p.mashape.com
bom = botometer.Botometer(wait_on_ratelimit=True, rapidapi_key=Rapid_API_Key, **twitter_auth)

username = "enter account username"
output = bom./4/check_account(username)

print(output)
