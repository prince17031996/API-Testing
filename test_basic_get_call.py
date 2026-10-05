from http.client import responses

import requests
from requests.auth import HTTPBasicAuth




def test_basic_get_call_mocktest_1():
    response=requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200
    response_data=response.json()
    for x in range(0,len(response_data)):
        val=(response_data[x]["title"])
        if val=="sunt aut facere repellat provident occaecati excepturi optio reprehenderit":
            assert response_data[x]['id']==1


def test_basic_get_call_mocktest_2():
    response=requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    response_data=response.json()
    assert 'id' in response_data
    assert 'userId' in response_data
    assert 'title' in response_data
    assert 'body' in response_data
    assert isinstance(response_data['id'],int)
    assert isinstance(response_data['userId'],int)
    assert isinstance(response_data['title'],str)
    assert isinstance(response_data['body'],str)
    assert len(response_data['title']) >= 1
    assert len(response_data['body']) >= 1
    assert response_data['id']==1
    assert response_data['userId']==1

    response_time = response.elapsed.total_seconds()
    print(response_time)
    assert response_time < 2