import httplib, urlparse, urllib, sys
from md5p import md5, padding

url = sys.argv[1]
mark = sys.argv[2]
#url = "https://mathlab.utsc.utoronto.ca/courses/cscd27f16/assignment/01/server/?tag=c4ca99a303c91599f24f8b3a25b11657&utorid=chenha17"
#mark = '100'
# ADD CODE HERE

# parse url 
my_url = urlparse.urlparse(url)
# take out the query part of the url(tag=c4ca99a303c91599f24f8b3a25b11657&utorid=chenha17)
query = my_url.query 
#split the the query in to dictionary
query_dic = {}
for s in query.split("&"):
    query_dic[s.split('=')[0]] = s.split('=')[1]

# update the hash 
tag = query_dic['tag']
utorid = query_dic['utorid']
# update the hash with the tag 
h = md5(state=tag.decode("hex"), count=512)
mark_query = '&mark=' + str(mark) + '&utorid=' + utorid
# update the hash
h.update(mark_query)

# get the Url with the first & and this is the url param
u = query[query.find("&"):]

for i in range(8, 17):
    # form the new url 
    # make things a bit easier
    FirstHalfUrl = url.split('?')[0]
    url = (FirstHalfUrl + '?tag=' + h.hexdigest() + u 
           + urllib.quote(padding((len(u) + i)*8)) 
           + mark_query)
    print i
    print repr(url)[1:-1]
    # parameter url is the attack url you construct
    parsedURL = urlparse.urlparse(url)
    
    # open a connection to the server
    httpconn = httplib.HTTPSConnection(parsedURL.hostname)
    
    # issue server-API request
    httpconn.request("GET", parsedURL.path + "?" + parsedURL.query)
    
    # httpresp is response object containing a status value and possible message
    httpresp = httpconn.getresponse()
    
    if httpresp.status == 200:
        # valid request will result in httpresp.status value 200
        print httpresp.status
        
        # in the case of a valid request, print the server's message
        print httpresp.read()
        break