import time, json, os
from threading import Thread

from rabbit_mq_test.rabbit_mq_pub_sub import RabbitMQTest

mq = RabbitMQTest('202.30.164.208', os.getenv('ID'), os.getenv('PASSWORD'))

total_page = 1
def run(idx, results):
    msg = f'{"H" * 1751}[{i}]'
    mq.pub_test(f'test{idx}',msg, 100000, idx)

results = [None] * total_page
for i in range(total_page):
    Thread(target=run, args=(i, results)).start()
    time.sleep(0.0001)
time.sleep(30)

m = {"id":"null","stationCode":"TEST052","customBatchId":"20211214105741216013","requestSequence":211214105741440026,"messageProvider":"ARTICLE_BATCH","type":"ASSIGN","status":"STARTING","messageParam":"{\"customBatchId\":\"20211214105907418104\",\"assignInfo\":[{\"stationCode\":\"TEST052\",\"labelCode\":\"FA1009C5B294\",\"articles\":[{\"stationCode\":\"TEST052\",\"id\":\"1201115143200\",\"nfcString\":\"http://google.com\",\"originPrice\":\"2456\",\"salePrice\":\"2222\",\"discountPercent\":\"9.0\",\"seq\":0,\"data\":{\"LIST_PRICE\":\"2456\",\"A_MARKER\":\"1\",\"ALIAS\":\"Super Blueberry Milk\",\"BARCODE\":\"7801115143200\",\"UNIT_PRICE\":\"3789\",\"ITEM_NAME\":\"Mail Milk Super Blueberry Milk\",\"ORIGIN\":\"KOREA\",\"ETC_2\":\"etc 2\",\"ETC_1\":\"etc 1\",\"ETC_0\":\"etc 0\",\"CATEGORY2\":\"Low-fat Milk\",\"ETC_6\":\"etc 6\",\"CATEGORY3\":\"160 kcal\",\"ETC_5\":\"etc 5\",\"CATEGORY4\":\"HACCP\",\"ETC_4\":\"etc 4\",\"ARTICLE_ID\":\"1201115143200\",\"CATEGORY5\":\"Best by 14.09.25\",\"ETC_3\":\"etc 3\",\"WEIGHT\":\"200ml\",\"UNIT_DIMENSION\":\"2\",\"TYPE\":\"Milk\",\"ETC_9\":\"etc 9\",\"WEIGHT_UNIT\":\"100ml\",\"DISPLAY_TYPE\":\"01\",\"ETC_8\":\"etc 8\",\"UNIT_PRICE_UNIT\":\"4\",\"CATEGORY1\":\"Blueberry Juice 1.5%\",\"ETC_7\":\"etc 7\",\"DISPLAY_TYPE3\":\"03\",\"DISPLAY_TYPE2\":\"02\",\"R_MARKER\":\"1\",\"MANUFACTURER\":\"Mail MILK\",\"NFC_URL\":\"http://google.com\",\"SALE_PRICE\":\"2222\",\"STORE_CODE\":\"TEST052\"}}],\"templates\":null,\"templateList\":[\"APP - 2.9_HD_ _ 384 X 168.xsl\"],\"skipChecksumValidation\":false,\"arrow\":null,\"addInfo2\":null,\"addInfo3\":null,\"addInfo4\":null,\"addInfo5\":null}],\"forcedUpdatePage\":-1}","numberOfItems":1,"serverId":0,"created":"null","lastModified":"null"}