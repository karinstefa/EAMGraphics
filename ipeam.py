import pandas as pd
import numpy as np
from plotnine import *
import urllib.request
import csv
import geoip2.database

db = geoip2.database.Reader('./GeoLite2-City.mmdb')

with open('Descargas_May2018.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count =0
    for row in csv_reader:
        try:
            response = db.city(row[5])
            print (row[5], response.country.name, response.city.name, response.country.iso_code, response.location.longitude,   response.location.latitude)
        except:
            pass
        line_count += 1
    #print(f'Processed {line_count} lines.')



#np.savetxt("newDataFile.csv", data, fmt='%.18e', delimiter=', ', header='New Data', comments='# ')

