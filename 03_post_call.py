import requests

kong_proxy = ''

def call_request():
    url = 'http://localhost:8000/login/'
    res = requests.post(url, data={'id':'krk', 'pw':'ggg'})
    print(res.content)

call_request()


