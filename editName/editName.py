file_name = input('Введіть ім"я csv файлу який іпортуєие')

with open('import/arhiv.csv') as f:
  reader = csv.reader(f)
  for row in reader:
    autoCorectName(row[3])