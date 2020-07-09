import json
import requests
from requests.auth import HTTPBasicAuth
import urllib3

# URL of API resource which retrieves the list of devices
URL = "https://primeinfrasandbox.cisco.com/webacs/api/v3/data/Devices.json"

# Add the query parameter to indicate that whole objects be returned rather than just IDs of the entities.
querystring = {".full":"true"}
# Provide login and password for the basic authorization
basicAuth = HTTPBasicAuth('devnetuser', 'DevNet123!')

# Disable SSL certificate verification
SSL_VERIFY = False
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Make request
response = requests.request("GET", URL, params=querystring, auth=basicAuth, verify=SSL_VERIFY)

# Parse the received JSON
parsed_response = json.loads(response.text)


# Iterate over the list of devices and print IP addresses and statuses
for entity in parsed_response["queryResponse"]["entity"]:
    adminStatus = entity["devicesDTO"]["adminStatus"]
    ipAddress = entity["devicesDTO"]["ipAddress"]
    deviceId = entity["devicesDTO"]["@id"]
    print(ipAddress, adminStatus, deviceId,)
