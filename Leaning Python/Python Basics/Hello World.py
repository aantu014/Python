#Hello

def main():
  print("Hello world")
  f=0
  print(f)
  # Redclare variable
  f="abc"
  print(f)
  #variables of different types cannot be combined
  print("this is a string " + str(123))

if __name__ == "__main__":
    main()

def somefucntion():
  global d #Makes variable global
  d="This is value for 'd' in function"
  print(d)

somefucntion()
print(somefucntion())
print(somefucntion) #Prints the value of the function

#functions that takes argument
def function2(arg1, arg2):
  print(arg1, " ", arg2)

  #function that has return value
def function3(x):
  return x*x*x
print("\n")
function2(25,7)
print(function2(10, 7))
print(function3(3)) #Prints int value of the function

def power(num , x=1):
  result = 1
  for i in range(x):
    result = result * num
  return result
  
print("\n")
print(power(2)) #2 to power of 1 is 2
print(power(2, 3)) #values have to be in order for arguments
print(power(x=3, num=2))

#function with variable number of agents
def multi_add(*args):
  result = 0
  for x in args:
    result = result + x
  return result

print(multi_add(1, 2, 3))

print("\n")

if (5 > 4):
  st="5 is greater than 4"
  print(st)
elif (5 == 4):
  st="5 is greater than 4"
  print(st)
else:
   st="5 is not greater than 4"
   print(st)

x=0
while (x<5):
  print(x)
  x=x+1
print("\n")
for x in range(5, 10):
  print(x)

print("\n")
# Array
days=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for d in days:
  print(d)

#Using enumerate function to get index counter
for i, d in enumerate(days):
  print(i,d)

for x in range(1,10):
  if (x==10): break # stop at 10
  if (x % 2 == 0): continue # skip even numbers
  print(x)