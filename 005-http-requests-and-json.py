# The requests package is used for making http requests
# more info about the 'requests' package https://requests.readthedocs.io/en/latest/ 
# before running this script, you have to first run 
# pip install requests
import requests

# Here's the example we'll use - http://open-notify.org/Open-Notify-API/People-In-Space/

response = requests.get('http://api.open-notify.org/astros.json')

# The built-in 'type' function is isued to print out the variable's data type. 
# In this example I think it indicates that the it's custom data type that's 
# been returned for a class called requests.models.Response. I.e. this variable is an instance of that class. 
print(type(response)) # <class 'requests.models.Response'>

print(response.json())

print('\n\n')
for people in response.json()['people']:
    print(people['name'])