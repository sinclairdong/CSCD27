import os, requests, urllib

PROTOCOL = "http"
HOST = "localhost"
PORT = "8080"
BASE = PROTOCOL + "://" + HOST + ":" + PORT

with requests.Session() as s:
    res = s.get(BASE + "/delete.php", params ={'id':"3"})