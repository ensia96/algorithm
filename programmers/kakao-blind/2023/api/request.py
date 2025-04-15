import requests
import json

BASE_URL = 'https://68ecj67379.execute-api.ap-northeast-2.amazonaws.com/api'
X_Auth_Token = 'e6701fd0abdfae6115670a5c735a7dce'

headers = {
    'X-Auth-Token': X_Auth_Token,
    'Content-Type': 'application/json'
}
data = {}


def get(endpoint):
    return requests.get(BASE_URL + endpoint, headers=headers).json()


def post(endpoint, data):
    return requests.post(BASE_URL + endpoint, headers=headers, data=json.dumps(data)).json()


def put(endpoint, data):
    return requests.put(BASE_URL + endpoint, headers=headers, data=json.dumps(data)).json()


def start(scenario):
    res = post('/start', {"problem": scenario})
    headers['Authorization'] = res['auth_key']
    return res['day']


def get_reservations():
    return get('/new_requests')['reservations_info']


def reply(assignment):
    return put('/reply', {'replies': assignment})['day']


def simulate(assignment):
    return put('/simulate', {'room_assign': assignment})


def get_score():
    print(get('/score'))
