import requests



payload = {
    "title": "API Testing",
    "body": "Learning requests library",
    "userId": 1
}
#Validate that the returned title, body, and userId match what you sent
def test_basic_post_call_mocktest_1():

    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    assert response.status_code == 201
    response_data=response.json()
    print(response_data)
    assert 'id' in response_data
    assert 'title' in response_data
    assert 'body' in response_data
    assert 'userId' in response_data
    assert isinstance(response_data['id'],int)
    assert isinstance(response_data['title'],str)
    assert isinstance(response_data['body'],str)
    assert isinstance(response_data['userId'],int)
    assert response_data['userId'] == 1
    assert response_data['title'] == 'API Testing'
    assert response_data['body'] == 'Learning requests library'



