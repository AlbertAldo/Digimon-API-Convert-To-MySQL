from bs4 import BeautifulSoup
import requests
import json

import mysql.connector
myDB = {
    'user' : 'root',
    'password' : 'Albert123',
    'host' : 'localhost',
    'database' : 'Digimon'
}

conn = mysql.connector.connect(**myDB)
Cr = conn.cursor()

url = "http://digidb.io/digimon-list/"
web = requests.get(url)
out = BeautifulSoup(web.content, "html.parser")

############################### NAMA DIGIMON ##############################################
kotak = []
for i in out.find_all("a"):
  kotak.append(i.text)

# print(kotak)
# print(kotak[11])
# print(kotak[351])
digimon = []
for i in range(11,352):
    digimon.append(kotak[i])

# print(digimon)
# print(len(digimon))

########################## STAGE, TYPE, ATTRIBUTE, MEMORY, SAMPAI SPEED ######################################

bungkus = []
for i in out.find_all("center"):
  bungkus.append(i.text)
# print(bungkus)

###### STAGE
# print(len(bungkus)) # 3752
stage = []
for i in range (0, len(bungkus)-1, 11):
    stage.append(bungkus[i])
# print(stage)
# print(len(stage))

###### TYPE
tipe = []
for i in range (1, len(bungkus)-1, 11):
    tipe.append(bungkus[i])
# print(tipe)
# print(len(tipe))

###### Attribute
attribut = []
for i in range (2, len(bungkus)-1, 11):
    attribut.append(bungkus[i])
# print(attribut)
# print(len(attribut))

###### Memory
memory = []
for i in range (3, len(bungkus)-1, 11):
    memory.append(bungkus[i])
# print(memory)
# print(len(memory))

###### Equip Slot
equipslot = []
for i in range (4, len(bungkus)-1, 11):
    equipslot.append(bungkus[i])
# print(equipslot)
# print(len(equipslot))

###### HP
hp = []
for i in range (5, len(bungkus)-1, 11):
    hp.append(bungkus[i])
# print(hp)
# print(len(hp))

###### SP
sp = []
for i in range (6, len(bungkus)-1, 11):
    sp.append(bungkus[i])
# print(sp)
# print(len(sp))

###### Atk
atk = []
for i in range (7, len(bungkus)-1, 11):
    atk.append(bungkus[i])
# print(atk)
# print(len(atk))

###### Defense
defense = []
for i in range (8, len(bungkus)-1, 11):
    defense.append(bungkus[i])
# print(defense)
# print(len(defense))

###### Intelligence
intel = []
for i in range (9, len(bungkus)-1, 11):
    intel.append(bungkus[i])
# print(intel)
# print(len(intel))

###### Speed
speed = []
for i in range (10, len(bungkus)-1, 11):
    speed.append(bungkus[i])
# print(speed)
# print(len(speed))

############################################ FOTO ########################################################

plastik = []    
for i in out.find_all("img"):
  plastik.append(i)

# print(plastik)
# print(plastik[2], type(plastik[2]))
# print(plastik[342])

link = []
for i in range(2,343):
    a = str(plastik[i])
    foto = []
    for j in a:
        foto.append(j)
    # print(foto)
    ambil = foto[9:49]
    gabung = "".join(ambil)
    # print(gabung)
    link.append(gabung)
# print(link)
# print(len(link))

##################################### BIKIN NOMOR ###########################################
nomor = []
for i in range(1, 342):
    nomor.append(i)
# print(nomor)

################################### GABUNGIN SEMUA KE DATABASE DIGIMON ########################################
"""
query = ''' CREATE TABLE Digimon_List(
    No smallInt,
    Digimon char(50),
    ImageLink char(200),
    Stage char(20),
    Type char(20),
    Attribute char(20),
    Memory tinyInt,
    EquipSlots tinyInt,
    HP smallInt,
    SP smallInt,
    Atk smallInt,
    Def smallInt,
    Intelligence smallInt,
    Spd smallInt
)
'''
Cr.execute(query)
print('Table Created')
"""

"""
sql = "INSERT INTO Digimon_List VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
for i in range(0,341):
    val = (nomor[i], digimon[i], link[i], stage[i], tipe[i], attribut[i], memory[i], equipslot[i], hp[i], sp[i], atk[i], defense[i], intel[i], speed[i])
    Cr.execute(sql,val)
    conn.commit()

print("Data Submitted")
"""