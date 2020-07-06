print("""
*********************
To find out  your risk of death from coronavirus, please answer the questions below
*********************
""")
print("Are you a cigarette addict older than 75 years old?")
x=str(input("yes/no :")).lower()
if x=="yes":
    age=True
else:
    age=False
print("Do you have a severe chronic disease?")
y=str(input("yes/no :")).lower()
if y=="yes":
    chronic=True
else:
    chronic=False
print("Is your immune system too weak? ")
z=str(input("yes/no :")).lower()
if z=="yes":
    immune=True
else:
    immune=False

risk=(age or immune or chronic)
if (risk==True):
    print('You are in risky group')
else:
    print('You are not in risky group')
