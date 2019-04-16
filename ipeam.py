import pandas as pd
#from ggplot import *
import matplotlib.pyplot as plt


data = {}

df = open("Mayo2018Descargas.txt")

#p  cambia las columnas 1 -> pais, 2 -> ciudad
p=1

for line in df.readlines():
    sf = line.split()
    
    myValue = data.get(sf[p], 0)

    if(myValue == 0):
        data.update({sf[p]:1})
    else:
        data.update({sf[p]:1+myValue})

    #pass        
    #print(myValue)

#gr = ggplot(aes())
from collections import OrderedDict

d_sorted_by_value = OrderedDict(sorted(data.items(), key=lambda x: x[1], reverse=True))



plt.bar(list(d_sorted_by_value.keys()), d_sorted_by_value.values(), color='g')
plt.show()

print(data)
"""
for w in sorted(data, key=data.get, reverse=True):
    print(w, data[w])
"""