import requests

def testGetCall():
    coin_cap_rest_api_url = 'https://api.coincap.io/v2/assets'
    header_value = {"Context-Type":"application/json","Accept-Encoding":"deflate"}
    coin_cap_api_response = requests.get(coin_cap_rest_api_url,headers=header_value)
    print(coin_cap_api_response)

    assert coin_cap_api_response.status_code==200