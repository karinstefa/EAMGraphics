

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
    
    
print(data)

