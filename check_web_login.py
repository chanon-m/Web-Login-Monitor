#!/usr/bin/python3.4
import httplib2

url = 'https://YOUR_URL_LOGIN_PAGE'
username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'
key = "WORD_MONITOR"

http = httplib2.Http(".cache")
http.add_credentials(username, password)

try:
    response, content = http.request(url)

    if response.status == 200:
       if key in content.decode('UTF-8'):
            result = "0 Server=0; Website is up, The key words are " + key
       else:
            result = "2 Server=2; Website is down, The key words are " + key
    else:
         result = "1 Server=1; Website has error, HTTP Status=" + str(response.status)

except httplib2.ServerNotFoundError:
    result = "1 Server=1; Website has error, ServerNotFound"

print (result)
