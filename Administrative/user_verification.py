import json
import requests


def verify_user(steam_id64):
    url = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=471329DABD92E4048C86FABED4EC9824&steamids=' + steam_id64
    req = requests.get(url)
    user_data = req.json()
    print(user_data['response']['players'][0]['personaname'])

# user_data = json.loads('{"response":{"players":[{"steamid":"76561197960435530","communityvisibilitystate":3,"profilestate":1,"personaname":"Robin","lastlogoff":1544511112,"profileurl":"https://steamcommunity.com/id/robinwalker/","avatar":"https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/f1/f1dd60a188883caf82d0cbfccfe6aba0af1732d4.jpg","avatarmedium":"https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/f1/f1dd60a188883caf82d0cbfccfe6aba0af1732d4_medium.jpg","avatarfull":"https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/f1/f1dd60a188883caf82d0cbfccfe6aba0af1732d4_full.jpg","personastate":0,"realname":"Robin Walker","primaryclanid":"103582791429521412","timecreated":1063407589,"personastateflags":0,"loccountrycode":"US","locstatecode":"WA","loccityid":3961}]}}')
