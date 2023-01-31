def drive1():
  input("How old are you?\n")
  print("Still taking the bus!")

def feelgood():
  print("I'm glad you're feeling well,", name)
  age = input("How old are you?\n")
  if int(age) > 18:
    print("You are ready to drive.")
  else:
    print("Still taking the bus!")


def feelbad():
  print("Have some time to yourself to recharge!")
  drive1()



def convo():
  global name
  name = input('What is your name?\n')
  print("Nice to meet you,", name)
  
  mood = input('How are you doing today?\n')
  if mood == 'Good':
    feelgood()
  elif mood == "I'm great":
    feelgood()
  elif mood == "I'm good":
    feelgood()
  elif mood == "Fine":
    feelgood()
  elif mood == "Bad":
    feelbad()
  elif mood == "Not okay":
    feelbad()
  elif mood == "I'm not feeling good":
    feelbad()
  else:
    print("I see!")
    drive1()


answer = input('Hi, this is Pchatbot, can I talk to you?\n')

if answer == 'y':
  convo()
elif answer == 'Y':
  convo()
elif answer == 'n':
  print('Okay! Talk to you soon!')
elif answer == 'N':
  print('Okay! Talk to you soon!')
