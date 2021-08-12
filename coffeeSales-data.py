import csv
import plotly_express as px
import numpy as np

def getDatasource(data_path):
    days= []
    marks= []
    with open (data_path) as f:
        file = csv.DictReader(f)
        for x in file:
            days.append(float(x['Coffeeinml']))
            marks.append(float(x['sleepinhours']))
    return {'x':days,'y':marks}
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource['x'],dataSource['y'])
    print ('The correlation is ::',correlation[0,1])
def setup():
    data_path = 'C:/Users/Admin/OneDrive/Desktop/Python/Pro-106/project-files/coffeeSales-data.csv'
    dataSource = getDatasource(data_path)
    findCorrelation(dataSource)
setup()