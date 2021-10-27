import time
from threading import Thread
import requests

total_page = 1000
def run(idx, results):
    url = 'http://202.30.164.201:32453/app/test/hpa'
    print(idx, url)
    res = requests.get(url)
    print(res, res.content)

results = [None] * total_page
for i in range(total_page):
    Thread(target=run, args=(i, results)).start()
    time.sleep(0.1)
time.sleep(30)