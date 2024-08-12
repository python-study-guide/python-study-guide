# The requests package is used for making http requests
# more info about the 'requests' package https://requests.readthedocs.io/en/latest/ 
# before running this script, you have to first run 
# pip install requests
import requests

# Here's the example we'll use - http://open-notify.org/Open-Notify-API/People-In-Space/

response = requests.get('http://api.open-notify.org/astros.json')

print(response.json())

print('\n\n')
for people in response.json()['people']:
    print(people['name'])