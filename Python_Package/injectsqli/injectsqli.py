import requests

def predict(val, api_key):
    url = f'http://188.166.252.140:8000/predict/{val}'
    
    headers = {
    'accept': 'application/json',
    'X-API-Key': api_key
}
    
    res = requests.post(url, headers=headers)

    if res.status_code == 200:
        return res.json()
    else:
        return f'Request failed with status code {res.status_code}'