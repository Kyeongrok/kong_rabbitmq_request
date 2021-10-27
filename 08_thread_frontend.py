import time
from threading import Thread
import requests

total_page = 30000
def run(idx, results):
    url = 'http://202.30.164.201:32453'
    # url = 'http://202.30.164.201:31615/test/hpa'
    # url = 'http://202.30.164.201:32453/api/test/callStore?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImlzcyI6InRwV25Id3h6UWYzbmhBZ0FzRGRxOUZ3Y2VUdHJyVXdBIn0.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.BRaOymLqtquOlRZqc1AvYG2m3jSBKOAYFZW9_nO-4NM'
    # url = 'http://202.30.164.201:32282/store/main?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImlzcyI6InRwV25Id3h6UWYzbmhBZ0FzRGRxOUZ3Y2VUdHJyVXdBIn0.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.BRaOymLqtquOlRZqc1AvYG2m3jSBKOAYFZW9_nO-4NM'
    print(idx, url)
    res = requests.get(url)

    print(res, res.content)

results = [None] * total_page
for i in range(total_page):
    Thread(target=run, args=(i, results)).start()
    time.sleep(0.5)
time.sleep(30)