from http.client import responses

import requests
from requests.auth import HTTPBasicAuth
url=''
token='3fecf3290be275cfd19566fd507131385d3cddf1a75bcef5dbbd8531248f700f'
head={
    'Accept':'text/plain',
    'Content-type':'application/json',
    'Authorization':'bearer'
}
data={"id":7595918,
      "name":"Anshula Varman DDS",
      "email":"anshula_dds_varman@bergnaum.example",
      "gender":"female",
      "status":"active"}
def testPostAuthCall():
    responses=requests.post()