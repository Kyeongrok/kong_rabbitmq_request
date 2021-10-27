import requests

host_origin = 'http://ec2-3-35-222-159.ap-northeast-2.compute.amazonaws.com:30609'
host_origin = 'http://202.30.164.201:30490'


def create_service(service_name):
    url = f'{host_origin}/services/'
    res = requests.post(url, data={'name':service_name,
                                   'url':'http://mockbin.org'})
    print(res, res.content)

def create_api():
    url = f'{host_origin}/apis/'
    res = requests.post(url, data={'name':'test',
                                   'upstream_url':'http://httpbin.org',
                                   'request_host':'api.example.org',
                                  'request_path':'/test',
                                   'strip_request_path': True,
                                   })
    print(res, res.content)

def create_route(service_name):
    url = f'{host_origin}/services/{service_name}/routes'
    res = requests.post(url, data={'hosts[]':'example.com'})
    print(res, res.content)

def list_plugin(service_name):
    # Enable the plugin on a service
    url = f'{host_origin}/services/{service_name}/plugins'
    res = requests.get(url, data={'name':'jwt'})
    print(res, res.content)

service_name = 'example-service'
# create_route('example-service')
# create_service()
list_plugin(service_name)