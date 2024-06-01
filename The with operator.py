filt_name ='textFile2.txt'

with open('textFile2.txt', mode='r', encoding='utf8') as file:
   for line in file:
       print(line, end='')
