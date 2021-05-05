import requests # lib to make http requests
import json # lib to help with parsing JSON objects

# 8-Dec,0.16,55.0,50.0,TRUE
url = "https://rain-app-eric-caleb.herokuapp.com/predict?att0=8-Dec&att1=55.0&att2=50.0"
# url = "https://interview-flask-app.herokuapp.com/predict?level=Junior&lang=Java&tweets=yes&phd=yes"
# url = "http://127.0.0.1:5000/predict?level=Junior&lang=Java&tweets=yes&phd=yes"

# make a GET request to get the search results back
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
response = requests.get(url=url)

# first thing... check the response status code 
status_code = response.status_code
print("status code:", status_code)

if status_code == 200:
    # success! grab the message body
    json_object = json.loads(response.text)
    print(json_object)