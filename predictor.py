import requests # lib to make http requests
import json # lib to help with parsing JSON objects

# Jul-08,Melbourne,11.0,14.5,0.6,5.2,4.0,W,63.0,W,WSW,30.0,35.0,66.0,52.0,1013.4,1016.2,7.0,4.0,11.8,13.7,No,Yes
url = "https://rain-app-eric-caleb.herokuapp.com/predict?att0=Jul-08&att1=11.0&att2=14.5&att3=4.0"
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