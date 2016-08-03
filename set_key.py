import urllib2, json, pandas, requests

#Need this auth to specificaly retrieve the scouts
def get_key ():
    auth = 'https://login.globo.com/api/authentication'
    payload = "{\"payload\":{\"email\":\"youremail@site.com\",\"password\":\"YourPassword\",\"serviceId\": 438}}"
    headers = {
        'authorization': "Basic Z2FicmllbHRmMTQxQGdtYWlsLmNvbTpCYW5kcGMzdGh4NA==",
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "bd1c05ac-0d84-af56-1e6f-aa0fe5253835"
    }
    get_key = requests.request("POST", auth, data=payload, headers=headers)
    json_data = json.loads(get_key.text)
    key = json_data['glbId']
    return key
