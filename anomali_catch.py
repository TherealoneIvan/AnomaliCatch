import numpy as np
import json
def decoder(path):
    dictOfData = dict()
    mas = list()
    with open(path , "r") as read_file:
        data = json.loads(read_file.read())
        for i in data['results'][0]['series'][0]['values']:
            # print(i[0])
            a = i[0][5:]
            b = i[1]
            mas.append(b)
            dictOfData[a] = b

    return dictOfData
anomalies = []
def findAnomalies(oldDataPath,newDataPath ):
    oldData = decoder(oldDataPath)
    dictOfNewData = decoder(newDataPath)
    OldDataMas = []
    i = 0
    newDataMas = []
    for it in dictOfNewData:
        OldDataMas.append(oldData[it])
        newDataMas.append(dictOfNewData[it])
    OldDataStd = np.std(OldDataMas)
    OldDataMasMean = np.mean(OldDataMas)
    anomalyCutOff = OldDataStd * 3
    lowerLimit = 0
    upperLimit = OldDataMasMean + anomalyCutOff
    if OldDataMas == newDataMas:
        print("yes")
    for outlier in newDataMas:
        if outlier > upperLimit or outlier < lowerLimit:
            anomalies.append(outlier)
            print(outlier)
    return anomalies


# print(findAnomalies("stat_sample.json" ,"stat_sample_false_data.json"))