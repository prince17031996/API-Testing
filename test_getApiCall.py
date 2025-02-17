from http.client import responses

import pytest
import requests

'''class TestClass:
    def test_method(self):
        pass'''
link="https://fakerestapi.azurewebsites.net/api/v1/Activities/"

def testGetCall():
    responses=requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities",verify=False)
    print("please proivde the status code",responses.status_code)
    print(responses.json())
    assert responses.status_code==200


@pytest.mark.login
def testPostCall():
    data={
                  "id": 200,
                  "title": "string",
                  "dueDate": "2024-12-20T18:51:39.971Z",
                  "completed": True
                }
    responses=requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities/",json=data)
    print("please provide the post Status code")
    print(responses.json())
    ans=responses.json()
    print('id is',ans['id'])
    assert responses.status_code==200 and ans['id']==201 ,'Test Failed as status code is not equal'


@pytest.mark.login
def testPutCall():
    data={ "id": 7120,
                  "title": "prince",
                  "dueDate": "2024-12-20T18:51:39.971Z",
                 "completed": True
    }
    responses=requests.put(link,json=data)
    print()
    print(responses.json())

@pytest.mark.login
def testPutCall1():
    data={ "id": 7120,
                  "title": "prince",
                  "dueDate": "2024-12-20T18:51:39.971Z",
                 "completed": True
    }
    responses=requests.put(link,json=data)
    print()
    print(responses.json())

'''testData=[(1,'Activity 1'),(2,'Activity 2'),(3,'Activity 3')]
@pytest.mark.parametrize('userId','title',testData)
def testParmeterCall(userId,title):
    responses=requests.get(f'{link}/{userId}')
    responsesBody=responses.json()
    print('respose',responsesBody)
    assert responsesBody[title]==title'''


testData = [(1, 'Activity 1'), (2, 'Activity 2'), (3, 'Activity 3')]

@pytest.mark.parametrize('userId,title', testData)  # Use a single string for parameter names
def testParmeterCall(userId, title):
    response = requests.get(f'{link}/{userId}')
    responseBody = response.json()
    print('why this is not returning response:', responseBody['title'])
    assert responseBody['title'] == title  # Fixed