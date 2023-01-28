import csv

id = ''
lastname = ''	
lastname2	= ''
firstname	= ''
midlname	= ''
yearBirth	= ''
placeBirth = ''
city_B = ''
nationality = ''
socialBackground = ''
politicalAffiliation = ''
education = ''
activity = ''
residence = ''
workPlace = ''
familyMembers = ''
whenArrested = ''
whoConvicted = ''
familyPunishment = ''
furtherFate = ''
whenRehabilitated = ''
death = ''
caseNumber = ''
notes = ''
foto = ''
url = ''

# Зробити всі слова з першої великої літери, а інші з маленької
def toFirstBigLeter(str):
  return str.title()

# Шукає по списку помилкових імен і якщо знаходить то віддає правильну версію
def autoCorectName(name):
  with open('import/name.csv') as f:
    reader = csv.reader(f)
    for row in reader:
      if (row[0] == name):
        print(f'Ім"я {name} змінено на {row[1]}')
        return row[1]

# Отримує данні з файлу на видаляє всі повтори та записує в файл для 
def findRepeat(reader):
  data = []
  for row in reader:
    if data.count([row[3]]) > 0:
      pass
    else:
      data.append([row[3]])
      print(f'Додано {row[3]}')
  
  with open('import/name.csv', 'w') as f:
    writer = csv.writer(f)
    for i in range(len(data)):
      print(data[i])
      writer.writerow(data[i])

with open('import/arhiv.csv') as f:
  reader = csv.reader(f)
  # for row in reader:
  #   autoCorectName(row[3])
  

  
      
