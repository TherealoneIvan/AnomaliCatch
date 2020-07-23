import json
import re
import datetime as DT
import numpy as np
def decoder2(path):
    dictOfData = []
    mas = list()
    with open(path, "r") as read_file:
        data = json.loads(read_file.read())
        for i in data['results'][0]['series'][0]['values']:
            a = i[0][:-1]
            a = re.sub(r"[-T:]", "", a)
            a = DT.datetime.strptime(a, '%Y%m%d%H%M%S')
            b = i[1]
            dictOfData.append(b)
    return dictOfData
def AnomaliesCatcher(oldDataPath , newDataPath , threshold):
    oldData = decoder2(oldDataPath)
    newData = decoder2(newDataPath)

    Q1 = np.percentile(sorted(oldData), 25, interpolation='midpoint')
    Q3 = np.percentile(sorted(oldData), 75, interpolation='midpoint')
    IQR = Q3 - Q1
    print(IQR)
    up_bound = Q3 + threshold*IQR
    low_bound = 10000
    anomalies = []
    for it in newData:
        if it > up_bound or it < low_bound:
                anomalies.append(it)
    return anomalies
AnomaliesCatcher("/Users/macos/PycharmProjects/firstProj/stat_sample.json" , "/Users/macos/PycharmProjects/firstProj/stat_sample_false_data.json" , 1.25)
