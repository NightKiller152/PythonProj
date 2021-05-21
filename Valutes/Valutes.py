import urllib.request
import xml.etree.ElementTree as ET
import datetime
import numpy as np

x = 90
y = 34

rub = {}
val = {}
num = []

while x > 0:

    date = datetime.datetime.today()

    x -= 1
    y -= 1

    aDate = date - datetime.timedelta(x)

    url = "http://www.cbr.ru/scripts/XML_daily.asp?date_req=" + aDate.strftime('%d/%m/%Y')
    data = urllib.request.urlopen(url).read()

    root = ET.fromstring(data)
    dt = root.attrib['Date']

    val[dt] = {}

    for item in root:
        v = float(item[4].text.replace(',', '.'))
        k = item[3].text
        num.append(float(item[4].text.replace(',', '.')))
        val[dt][k] = v

    for y in range(34):
        nm = root[y][3].text
        rub[nm] = []

    for dat, value in val.items():
        for name in value:
            rub[name].append(value[name])
            if value[name] == max(num):
                yx = name
                zx = value[name]
                dx = dat
            if value[name] == min(num):
                ym = name
                zm = value[name]
                dy = dat

for key, value in rub.items():
    mid = "%.2f" % np.mean(value)
    valute = key
    print('Cредняя цена:', valute, ' = ', mid)
print('Дата: ', dx, 'Валюта: ', yx, ', макс. цена: ', zx)
print('Дата: ', dy, 'Валюта: ', ym, ', мин. цена: ', zm)
