from http.client import responses

import requests
from requests.auth import HTTPBasicAuth




def test_basic_get_call():
    response=requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200
    response_data=response.json()
    for x in range(0,len(response_data)):
        val=(response_data[x]["title"])
        if val=="sunt aut facere repellat provident occaecati excepturi optio reprehenderit":
            assert response_data[x]['id']==1
