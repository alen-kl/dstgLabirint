import random
import queue

#postavke (minimalno 3 x 3)
brojRedaka=5
brojStupaca=5
#*******

class Celija:
  def __init__(self, x, y, posjeceno):
    self.koordinate=(x,y)
    self.posjeceno = posjeceno
    self.susjedi=[]
    self.s=[]

class cell:
  def __init__(self,koordinate,broj):
    self.koordinate=koordinate
    self.broj=broj
  
def generirajCelije(x,y,lista):
  for i in range (0,x):
    for j in range (0,y):
      lista.append(Celija(i,j,False))
  '''
def popuniSusjede(lista):
  for c in range(0,brojRedaka*brojStupaca):
    #***#
    if(lista[c].koordinate[0]==0 and lista[c].koordinate[1]==0):
      lista[c].susjedi.append((0,1))
      lista[c].susjedi.append((1,0))
      #***#
    if(lista[c].koordinate[0]==0 and lista[c].koordinate[1]==brojStupaca-1):
      lista[c].susjedi.append((0,brojStupaca-2))
      lista[c].susjedi.append((1,brojStupaca-1))
      #***#
    if(lista[c].koordinate[0]==brojRedaka-1 and lista[c].koordinate[1]==0):
      lista[c].susjedi.append((brojRedaka-2,0))
      lista[c].susjedi.append((brojRedaka-1,1))
      #***#
    if(lista[c].koordinate[0]==brojRedaka-1 and lista[c].koordinate[1]==brojStupaca-1):
      lista[c].susjedi.append((brojRedaka-2,brojStupaca-1))
      lista[c].susjedi.append((brojRedaka-1,brojStupaca-2))
      #***#
    if(lista[c].koordinate[0]==0 and lista[c].koordinate[1] in range (1,brojStupaca-1)):
      lista[c].susjedi.append((0,lista[c].koordinate[1]-1))
      lista[c].susjedi.append((0,lista[c].koordinate[1]+1))
      lista[c].susjedi.append((1,lista[c].koordinate[1]))
      #***#
    if(lista[c].koordinate[0] in range (1,brojRedaka-1) and lista[c].koordinate[1]==0):
      lista[c].susjedi.append((lista[c].koordinate[0]-1,0))
      lista[c].susjedi.append((lista[c].koordinate[0]+1,0))
      lista[c].susjedi.append((lista[c].koordinate[0],1))
      #***#
    if(lista[c].koordinate[0] in range (1,brojRedaka-1) and lista[c].koordinate[1]==brojStupaca-1):
      lista[c].susjedi.append((lista[c].koordinate[0]-1,brojStupaca-1))
      lista[c].susjedi.append((lista[c].koordinate[0]+1,brojStupaca-1))
      lista[c].susjedi.append((lista[c].koordinate[0],lista[c].koordinate[1]-1))
      #***#
    if(lista[c].koordinate[0]==brojRedaka-1 and lista[c].koordinate[1] in range (1,brojStupaca-1)):
      lista[c].susjedi.append((brojRedaka-1,lista[c].koordinate[1]-1))
      lista[c].susjedi.append((brojRedaka-1,lista[c].koordinate[1]+1))
      lista[c].susjedi.append((lista[c].koordinate[0]-1,lista[c].koordinate[1]))
      #***#
    if(lista[c].koordinate[0] in range (1,brojRedaka-1) and lista[c].koordinate[1] in range (1,brojStupaca-1)):
      lista[c].susjedi.append((lista[c].koordinate[0],lista[c].koordinate[1]-1))
      lista[c].susjedi.append((lista[c].koordinate[0]-1,lista[c].koordinate[1]))
      lista[c].susjedi.append((lista[c].koordinate[0],lista[c].koordinate[1]+1))
      lista[c].susjedi.append((lista[c].koordinate[0]+1,lista[c].koordinate[1]))
      #***#
'''
def popuniSusjede1(lista):
  for c in range(0,brojRedaka*brojStupaca):
    if(c==0):
      lista[c].susjedi.append(1)
      lista[c].susjedi.append(brojStupaca)
    elif(c==brojStupaca-1):
      lista[c].susjedi.append(c-1)
      lista[c].susjedi.append(c+brojStupaca)
    elif(c==brojStupaca*(brojRedaka-1)):
      lista[c].susjedi.append(c-brojStupaca)
      lista[c].susjedi.append(c+1)
    elif(c==brojRedaka*brojStupaca-1):
      lista[c].susjedi.append(c-brojStupaca)
      lista[c].susjedi.append(c-1)
    elif(c in range (1,brojStupaca)):
      lista[c].susjedi.append(c+1)
      lista[c].susjedi.append(c-1)
      lista[c].susjedi.append(c+brojStupaca)
    elif(c%brojStupaca==0 and c!=0 and c!=brojStupaca*(brojRedaka-1)):
      lista[c].susjedi.append(c+1)
      lista[c].susjedi.append(c+brojStupaca)
      lista[c].susjedi.append(c-brojStupaca)
    elif(c%brojStupaca==brojStupaca-1 and c!=brojStupaca-1 and c!=brojRedaka*brojStupaca-1):
      lista[c].susjedi.append(c-1)
      lista[c].susjedi.append(c-brojStupaca)
      lista[c].susjedi.append(c+brojStupaca)
    elif(c in range (brojStupaca*(brojRedaka-1)+1,brojRedaka*brojStupaca-1)):
      lista[c].susjedi.append(c-1)
      lista[c].susjedi.append(c+1)
      lista[c].susjedi.append(c-brojStupaca)
    else:
      lista[c].susjedi.append(c+1)
      lista[c].susjedi.append(c-1)
      lista[c].susjedi.append(c+brojStupaca)
      lista[c].susjedi.append(c-brojStupaca)


##########################
           
red=queue.Queue()
listaCelija1=[];

generirajCelije(brojRedaka,brojStupaca,listaCelija1)
popuniSusjede1(listaCelija1)

#+++++++++++++++++++++++++++++++++++++++++++++++#
#1
n=random.randint(0,brojRedaka*brojStupaca)

while(1):
  #3
  listaCelija1[n].posjeceno=True
  #2
  c=cell(listaCelija1[n].koordinate,n)
  red.put(c)
  #4
  neposjeceniSusjediCelije=[]
  for el in listaCelija1[n].susjedi:
    if(listaCelija1[el].posjeceno==False):
      neposjeceniSusjediCelije.append(el)
  if(len(neposjeceniSusjediCelije)==0):
    while(red.empty()==False):
      celija=red.get()
      br=celija.broj
      for elem in listaCelija1[br].susjedi:
        if(listaCelija1[elem].posjeceno==False):
          neposjeceniSusjediCelije.append(elem)
      if(len(neposjeceniSusjediCelije)!=0):
        break
  if(len(neposjeceniSusjediCelije)==0):
    break
  a=random.choice(neposjeceniSusjediCelije)

  #5
  listaCelija1[a].s.append(listaCelija1[n].koordinate)
  listaCelija1[n].s.append(listaCelija1[a].koordinate)

  #6
  n=a

  #7 petlja
#+++++++++++++++++++++++++++++++++++++++++++++++#

for item in listaCelija1:
  print(str(item.koordinate) + "*" + str(item.s))




