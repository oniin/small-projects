import random

#shuffle func
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter1=chr(random.randint(97,122))
lowercaseLetter2=chr(random.randint(97,122))
digit1=chr(random.randint(48,57))
digit2=chr(random.randint(48,57))
puncuationsign1=chr(random.randint(33,38))
puncuationsign2=chr(random.randint(33,38))

#sum and shuffle
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + puncuationsign1 + puncuationsign2
password = shuffle(password)

#Ouput
with open("passes.txt", "a") as external_file:
  print(password, file=external_file)
  external_file.close()