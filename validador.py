from glob import glob


ruta = '/DWHSAP/sap_upload/respaldo/20220615'
files = glob(ruta + '/*')
#print files
data = []
f = open(files[0])
try:
        for line in f:
                line = line.strip()
                data.append(line.split('|'))
finally:
        f.close()
print data [0]