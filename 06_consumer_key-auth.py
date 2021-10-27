import requests

host_origin = 'http://ec2-3-35-222-159.ap-northeast-2.compute.amazonaws.com:30609'
host_origin = 'http://202.30.164.201:30490'

def list_jwt_credential(user_name):
    url = f'{host_origin}/consumers/{user_name}/key-auth'
    res = requests.get(url)
    print(res, res.content)

def create_jwt_credential(user_name):
    url = f'{host_origin}/consumers/{user_name}/jwt'
    res = requests.post(url)
    print(res, res.content)

user_name = 'solum-consumer2'
# create_jwt_credential('user123')
list_jwt_credential(user_name)