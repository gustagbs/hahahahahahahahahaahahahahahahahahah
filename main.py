import csv,operator
import random
import time
import colorama
from colorama import init, Fore, Back, Style
brauktie = ['k1']
import os
kpunkti = ['u1', 'u2', 'u3', 'u4','u5']
import pandas as pandasForSortingCSV
import math
import re
from prettytable import PrettyTable
from prettytable import from_csv
import pandas as pd
print('Spēle “Tūrisma rallijs Liepāja 2022” ')
print('AUTORI: Gustavs Judeiks, Ronalds Gackis💀💀💀')

lauki = [
    "Kontrolpunkts", "k1", "k2", "k3", "k4", "k5",
    "k6", "k7", "k8", "k9", "k10", "u1",
    "u2", "u3", "u4","u5"
]


init(autoreset=True)
def noteik():
    print('================================================')
    f = open("noteikumi.txt", 'r')
    file_contents = f.read()
    print(file_contents)
    print('================================================')




global file_path2
file_path2 = "/home/runner/hahahahahahahahahaahahahahahahahahah/faili/jautajumi.csv"

global file_path3
file_path3 = "/home/runner/hahahahahahahahahaahahahahahahahahah/faili/atbildes.csv"
global file_path4
file_path4="/home/runner/hahahahahahahahahaahahahahahahahahah/faili/pilsetas.csv"
global file_path5
file_path5="/home/runner/hahahahahahahahahaahahahahahahahahah/faili/rezultāti_bonus.csv"
global file_path6
file_path6="/home/runner/hahahahahahahahahaahahahahahahahahah/faili/rezultāti_laiks.csv"
global file_path7
file_path7="/home/runner/hahahahahahahahahaahahahahahahahahah/faili/sorted.csv"
global file_path8
file_path8="/home/runner/hahahahahahahahahaahahahahahahahahah/faili/sorted2.csv"
def tab():
    global file_path
    file_path = "/home/runner/hahahahahahahahahaahahahahahahahahah/faili/kontrolpunkti.csv"

    with open(file_path) as fp:
        mytable = from_csv(fp, delimiter=',')
    print('Tabula ar visiem vajadzīgajiem attālumiem(km)')
    print(mytable)
    print(Style.DIM+'Auto ar pilnu uzlādi saulainā laikā var nobraukt 140km un lietainā laikā 80km')
    print('================================================')




b = 'k1'

global kur 
def laiks(timeris, uzlade, punkti,c,attālums,x,b):

  stundas = ['1', '2', '3', '4', '5', '6', '7']
  
  

  
  if c == 'lietains laiks':
    global h
    h = int(*random.choices(stundas, weights=(30, 40, 35, 25, 15, 10, 5)))
    print('Ja velies pagaidit līdz lietus beidzas, uzraksti 1. Tev būs jāgaida',h,'stunda(s). Ja nevēlies, ievadi jebko ko vēlies!')
    global lieta
    lieta = input()
    if lieta == '1':
      print('paiet', h, 'stundas')
      timeris += h
      
  return timeris, uzlade, punkti, c, attālums,x,b


def sakums():
    print(
        'Tavs ceļojums uzsākas Valmierā - Māra Štromberga BMX trasē. Apskati kontrolpunktu un atbildi uz jautājumu'
    )
    print('================================================')
    timeris = 0
    punkti = 100
    uzlade = 100
    c='filler'
    attālums=0
    
    b='filler'

    x = 'k1'
    timeris += 0.5
    fails = open(file_path2, "r")
    lasitajs = csv.DictReader(fails)
    
    for rinda in lasitajs:
        if rinda['punkts'] == x:
            g = rinda

            selected_valuesx = [
                value for key, value in g.items() if len(key) >= 7
            ]

          

            jautaju = random.choice(selected_valuesx)

            print(jautaju)

    selected_valuesaty = []

    while True:
        atbilde = input()
        fails = open(file_path3, "r")
        lasitajs = csv.DictReader(fails)
        for rinda in lasitajs:
            if rinda['jautajums'] == jautaju:
                at = rinda
                selected_valuesaty = [
                    value for key, value in at.items() if len(key) > 8
                ]
               
        if (atbilde in selected_valuesaty):
            print(Fore.GREEN + 'atbilde ir pareiza')
            punkti += 10
            
            break
        else:
            print(Fore.RED+ 'atbilde bija nepareiza! Tu zaudēji bonus punktus! Mēģini vēlreiz')
            punkti -= 10
    b='k1'
    return timeris, uzlade, punkti, c, attālums,x,b


def jautajumi(timeris, uzlade, punkti, c, attālums,x,b):
  fails = open(file_path4, "r")
  punkti=punkti
  lasitajs = csv.DictReader(fails)
  for rinda in lasitajs:
    if rinda["kpunkts"] ==x:
      global l
      
      l = rinda['pilseta']
   
      print(Fore.BLUE+'Tu esi nonācis',Fore.BLUE+l)
   
  if (x in kpunkti):
    punkti -= 15
    uzlade = 100
    if punkti<0:
     
      print('Kamēr gaidi pilnu baterijas uzlādi, atbildi uz vienu jautājumu par pilsētu kurā atrodies!' )
      print('================================================')
    
  else:
    print('Apskati šo kontrolpunktu un atbildi uz vienu jautājumu kura temats ir saistīts ar vietu kurā šobrīd atrodies!')
    print('================================================')
  timeris += 0.5
  selected_valuesat=[]
  fails = open(file_path2, "r")
  lasitajs = csv.DictReader(fails)
  print(x)
  for rinda in lasitajs:
    if rinda['punkts'] == x:
      g = rinda
            

      selected_values = [
          value for key, value in g.items() if len(key) >= 7
      ]

      
      global jautaj
      jautaj = random.choice(selected_values)
  print(jautaj)
  while True:
        
    fails = open(file_path3, "r")
    lasitajs = csv.DictReader(fails)

    for rinda in lasitajs:
      if rinda['jautajums'] == jautaj:
        at = rinda
        

        selected_valuesat = [value for key, value in at.items() if len(key) > 1]

        
    atbilde = input()
   
      
    if (atbilde in selected_valuesat):
      print(Fore.GREEN+'Atbilde ir pareiza!! Tu ieguvi +10 bonuspunktus')
      punkti += 10
      
      break
    else:
      print(Fore.RED+'atbilde bija nepareiza! Tu zaudēji 10 bonuspunktus! Mēģini vēlreiz')
      punkti -= 10
      if punkti<0:
        punkti=0
  b=x
  return timeris, uzlade, punkti, c, attālums,x,b
   


def brauc(timeris, uzlade, punkti, c, attālums,x,b):
  global pe
  
  if ('k10' in brauktie):
    return timeris, uzlade, punkti, c, attālums,x,b
  pe=1
  
  
  tab()
  print(Fore.CYAN+'Šobrīd atrodies',Fore.CYAN+b,Fore.CYAN+'kontrolpunktā')
  print(':::::::::::')
  print(Fore.CYAN+'Tagadējais auto uzlādes līmenis ir',Fore.CYAN+ str(uzlade),Fore.CYAN+'%')
  print(':::::::::::')
  print(Fore.CYAN+'Tev šobrīd ir',Fore.CYAN+str(punkti),Fore.CYAN+'bonuspunkti')
  print('Ievadi uz kuru kontrolpunktu vai uzpildes staciju vēlies braukt. Ievēro savu uzlādes līmeni...')
  
 


  x = input()
 

  while True:
    if x=='noteikumi' or x=='Noteikumi':
      noteik()
      print('Ievadi uz kuru kontrolpunktu vai uzpildes staciju vēlies braukt. Ievēro savu uzlādes līmeni...')
      x=input()
    if x!='noteikumi' or x!='Noteikumi':

      
      break
    

  if (x in lauki):

    if (x in brauktie):
      print(':::::::::::')
      print(Fore.RED+'Uz šo kontrolpunktu jau bijāt, izvēlaties citu!')
      print(':::::::::::')
      timeris, uzlade, punkti, c, attālums,x,b = brauc(timeris, uzlade, punkti, c, attālums,x,b)
    fails = open(file_path, "r")

    lasitajs = csv.DictReader(fails)
    for rinda in lasitajs:
      if rinda["Kontrolpunkts"] == b:
        a = float(rinda[x])
        print('::::::::::::::::')
        print('jabrauc', a, 'km')

  
    if pe==1:
      lel = ['lietains laiks', 'saulains laiks']
      laikapstakli = random.choices(lel, weights=(20, 80))
      c = ('[]'.join(laikapstakli))
      print('::::::::::::::::')
      print('Būs', c)
      print('::::::::::::::::')
      pe+=1
    if c=='saulains laiks':
      print('Auto ar tagadējo uzlādes līmeni var nobraukt',uzlade*140/100,'km')
      print('::::::::::::::::')
    if c=='lietains laiks':
      print('Auto ar tagadējo uzlādes līmeni var nobraukt',uzlade*80/100,'km')
      print('::::::::::::::::')
    
      
     
          
    print(Fore.YELLOW+'Vai vēlies braukt vai tomēr esi pārdomājis? Ievadi jebko, ja vēlies braukt, ievadi nē, ja tomēr vēlies braukt uz citu kontrolpunktu!')
    lol=input()
    if lol=='nē' or lol=='ne' or lol =='Nē' or lol=='Ne':
      timeris, uzlade, punkti, c, attālums,x,b = brauc(timeris, uzlade, punkti, c, attālums,x,b)
    else:
     
      timeris, uzlade, punkti, c, attālums,x,b = laiks(timeris, uzlade, punkti, c, attālums,x,b) 
    
   
    if c == 'lietains laiks' and lieta!='1':
      
      
      uzlade -= round(a / 80 * 100,2)
      timeris += a / 90
      
      if uzlade <= 0:
        
        print('================================================')
        print(Fore.YELLOW+'Uzlādes limenis ir sasniedzis 0. Ievadi uz kuru uzpildes staciju vēlies doties. Uzmanies! Jo tālāku staciju izvēlēsies jo smagāks būs sods! Attālums tiks mērīts no pēdējā apmeklētā kontrolpunkt')
        while True:
          kur = input()
          if (kur not in kpunkti):
            print('ievadi atbilstošu uzlādes stacijas identifikatoru!!')
          else:
            break
        fails = open(file_path, "r")
        lasitajs = csv.DictReader(fails)
        a=None
        for rinda in lasitajs:
          if rinda["Kontrolpunkts"] == b:
            a = float(rinda[kur])
       
        punkti -=round(a / 3)
        if punkti < 0:
          punkti = 0
        timeris += a / 10
        timeris += 0.5
        x = kur
        brauktie.append(x)
            
        attālums+=a
        timeris, uzlade, punkti, c, attālums,x,b = jautajumi(
            timeris, uzlade, punkti, c, attālums,x,b)
        return timeris, uzlade, punkti,c,attālums,x,b

    if c == 'saulains laiks' or lieta == '1':

      timeris += a / 100
      uzlade -= round(a / 140 * 100,2)
      
      if uzlade <= 0:
        print('================================================')
        print(Fore.YELLOW+'Uzlādes limenis ir sasniedzis 0. Ievadi uz kuru uzpildes staciju vēlies doties. Uzmanies! Jo tālāku staciju izvēlēsies jo smagāks būs sods!')

        while True:
          kur = input()
          if (kur not in kpunkti):
            print('================================================')
            print('ievadi atbilstošu uzlādes stacijas identifikatoru!!')
            print('================================================')
          else:
            break
        fails = open(file_path, "r")
        lasitajs = csv.DictReader(fails)
        a=None
        for rinda in lasitajs:
          if rinda["Kontrolpunkts"] == b:
            a = float(rinda[kur])
            
            

          
       
        punkti -= round(a / 3)
        if punkti < 0:
          punkti = 0
        timeris += a / 10
        timeris += 0.5
        x = kur
        brauktie.append(x)
        
            
        attālums+=a
            
        timeris, uzlade, punkti, c, attālums,x,b = jautajumi(timeris, uzlade, punkti, c, attālums,x,b)
        timeris += math.ceil(a / 90)
        return timeris, uzlade, punkti,c,attālums,x,b
        
    brauktie.append(x)
    attālums+=a
    punkti-=0

    timeris, uzlade, punkti, c, attālums,x,b = jautajumi(timeris, uzlade,punkti, c, attālums,x,b)
       
      

  else:
    print('ievadi esošu kp identifikatoru')
    timeris, uzlade, punkti, c, attālums,x,b = brauc(timeris, uzlade, punkti, c, attālums,x,b)
  return timeris, uzlade, punkti, c, attālums,x,b
noteik()
print('Vai esi gatavs? Tad uz priekšu! Lai uzsāktu spēli nospiedu taustiņu Enter!')
sakuma=input()
while sakuma!='':
  sakuma=input()
if sakuma=='':
  start = time.time()
  tab()
  
  timeris,uzlade,punkti,c,attālums,x,b=sakums()


timeris, uzlade, punkti, c, attālums,x,b = brauc(timeris, uzlade, punkti,c,attālums,x,b)
timeris, uzlade, punkti, c, attālums,x,b = brauc(timeris, uzlade, punkti,c,attālums,x,b)
timeris, uzlade, punkti, c, attālums,x,b = brauc(timeris, uzlade, punkti,c,attālums,x,b)
timeris, uzlade, punkti, c, attālums,x,b = brauc(timeris, uzlade, punkti,c,attālums,x,b)
timeris, uzlade, punkti, c, attālums,x,b = brauc(timeris, uzlade, punkti,c,attālums,x,b)
timeris, uzlade, punkti, c, attālums,x,b = brauc(timeris, uzlade, punkti,c,attālums,x,b)
timeris, uzlade, punkti, c, attālums,x,b = brauc(timeris, uzlade, punkti,c,attālums,x,b)
timeris, uzlade, punkti, c, attālums,x,b = brauc(timeris, uzlade, punkti,c,attālums,x,b)
timeris, uzlade, punkti, c, attālums,x,b = brauc(timeris, uzlade, punkti,c,attālums,x,b)
timeris, uzlade, punkti, c, attālums,x,b = brauc(timeris, uzlade, punkti,c,attālums,x,b)
timeris, uzlade, punkti, c, attālums,x,b = brauc(timeris, uzlade, punkti,c,attālums,x,b)
timeris, uzlade, punkti, c, attālums,x,b = brauc(timeris, uzlade, punkti,c,attālums,x,b)
timeris, uzlade, punkti, c, attālums,x,b = brauc(timeris, uzlade, punkti,c,attālums,x,b)
timeris, uzlade, punkti, c, attālums,x,b = brauc(timeris, uzlade, punkti,c,attālums,x,b)


end = time.time()
print('Malacis! Tu izgāji spēli: Tūrisma rallijs Liepāja 2022! Ievadi savu vārdu/lietotājvārdu lai redzētu savus status. ')
beigulaiks=round((end-start))


varc = input()
laikss = timeris * 60
bruh = math.floor(laikss // 60)
breh = math.ceil(((timeris - bruh) * 60))
print('ceļu paveici', bruh, 'stundās un ', breh, 'minūtēs')
print('Spēli pabeidzi ar', punkti, 'bonuspunktiem')
print('Šajā ceļojumā nobrauci',attālums,'kilometru')
aaa=beigulaiks/60
baa=beigulaiks-aaa

if aaa<1:
  print('Spēles programmā pavadīji',beigulaiks,'sekundes')
elif baa==0:
  print('Spēles programma pavadīji',aaa,'minūtes!')
else:
  
  
  print('Spēles programma pavadīji',aaa,'minūtes un',round(baa*60),'sekundēs')
  


rows=[varc,round(timeris,2),attālums,round(beigulaiks),punkti]
with open(file_path6,'a') as f: 
  write=csv.writer(f)
  write.writerow(rows)
#csvData = pandasForSortingCSV.read_csv(file_path6)
#csvData.sort_values([csvData.columns[1]],
                    #axis=0,
                    #ascending=[True],
                    #inplace=True)
sorted = pd.read_csv(file_path6)
sorted.sort_values(["laiks spēlē(h)","bonuspunkti"], axis=0, ascending=[True,False], inplace=True)




sorted=os.linesep.join(str.split(os.linesep)[:10])
print(Fore.BLUE+'Līderu saraksts pēc īsākā laika pavadīta ceļā.')
print(sorted)
#data = csv.reader(open(file_path6),delimiter=',')
#data = sorted(data, key=operator.itemgetter(1))
#filew =open(file_path8,'w')
#filew.write(str(data))
#filew.close()
#str(sorted)
# read the csv file
#gg = open(file_path8, 'r')
#gg = gg.readlines()
 
# Separating the Headers
#l1 = gg[0]
#l1 = l1.split(',')
 
# headers for table
#t = PrettyTable([l1[0], l1[1]])
 
# Adding the data
#for i in range(1, len(gg)) :
    #t.add_row(gg[i].split(','))
 
#code = t.get_html_string()
#html_file = open(file_path8, 'w')
#html_file = html_file.write(code)




#with open(file_path8) as fp:
  #mytable = from_csv(fp, delimiter=',')
  #print(Fore.BLUE+'Līderu saraksts pēc īsākā laika pavadīta ceļā.')
 
  #print(mytable)
rows=[varc,punkti,round(timeris,2),attālums,round(beigulaiks)]
with open(file_path5,'a') as f: 
  write=csv.writer(f)
  write.writerow(rows)
#csvData = pandasForSortingCSV.read_csv(file_path5)
#csvData.sort_values([csvData.columns[1]],
                    #axis=0,
                    #ascending=[False],
                    #inplace=True)

sorted = pd.read_csv(file_path5)
sorted.sort_values(["bonuspunkti","laiks spēlē(h)"], axis=0, ascending=[False,True], inplace=True)
print(Fore.BLUE+'Līderu saraksts pēc bonuspunktu skaita')
print(sorted)

#filew = open(file_path7, 'w')
#filew.write(str(sorted))
#filew.close()
#gg = open("read_file.csv", 'r')
 
# read the csv file
#gg = gg.readlines()
 
# Separating the Headers
#l1 = a[0]
#l1 = l1.split(',')
 
# headers for table
#t = PrettyTable([l1[0], l1[1]])
 
# Adding the data
#for i in range(1, len(a)) :




 
