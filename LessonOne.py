print("hello World")
print("This is a line and a number: ", 5)
print("escaping \"things\" is easy")
print('or just do "this" ')

print(3+5)
print(3*5)
print(3/5)
print(3-5)
print(3**5)

thisBeAVariable = "poop"
print(thisBeAVariable)

var1 = 55
print(var1)

var2 = 66
print('adding two vars:', var1+var2)

# while loop

condition = 1

while condition < 10:
    print('cond is: ', condition)
    condition+=1


# for loop

exampleList = [1,5,6,6,2,1,5,2,1,4]

for item in exampleList:
    print(item)

for x in range(90,100):
    print(x)


x = 4
y = 23

if x < y:
    print("x is less than y")
else:
    print("nah b, x be greater than y")



x = 34
y = 23
z = 84

if x < y:
    print("x is less than y")
elif x > z:
    print("x is greater than z")
else:
    print('the truth lies in the middle')


def imDre(name):
    if name=="dre":
        print("Listen to the play by play")
    else:
        print("POP POP POP")

imDre("dre")
imDre("eazy")


def addition(var1, var2):
    print('the value is: ', var1+var2)


addition(3,5)

# bleepBloop()  #this will not work due to being undefined in its current position

def bleepBloop():
    varX = "scope var"
    print(varX)


bleepBloop()


def simpleAdditio(num1, num2, num3):
    print('the sum is: ', num1+num2)


simpleAdditio(num1=4, num3=3, num2=2)


# print(varX)  # this will error out due to scope issues


# default params

def someFunc(num1, num2, num3=45):
    print('the sum is: ', num1+num2+num3)

someFunc(4,6)   # should be 55

someFunc(4,6,12) # should be 22

def someStrFunc(num1, num2, word="cat"):
    print('the sum is: ', num1+num2)
    print('the word is: ', word)
    print('doing this: ', printCat("meow"))

def printCat(noise):
    print("cat says: ", noise)

someStrFunc(4,2)
someStrFunc(5,3,'dog')


# "global" and local vars

someVar = 6

def example():
    print(someVar)
    print(someVar+4)
    # someVar+=6 # this will not work
    global someVar  # use the global keyword to modify the var
    someVar+= 6
    print(someVar)

example()

# you can do a whole bunch of things like:
    # pass the global to the function as a param
    # create a new variable in the function that gets the value of global var


# writing to a file

text = 'this is a file'

writeFile = open('someFile.txt', 'w')
writeFile.write(text)
writeFile.close()

appendFile = open('someFile.txt', 'a')
appendFile.write(' this is appended text')
appendFile.write('\nHere it is on a new line')
appendFile.close()

# reading from a file

readFile = open('someFile.txt', 'r').read()
print(readFile)
readFile = open('someFile.txt', 'r').readlines()    # puts the read content into an array
print(readFile)

# classes

class functionZ:

    def sum(x,y):
        print('sum is: ', x+y)
    def multi(x,y):
        print('sum is: ', x*y)

functionZ.sum(5,2)
functionZ.multi(4,3)

# Accessing URLs

# import urllib.request
#
# x = urllib.request.urlopen('https://www.google.com/')
# print(x.read())

# import urllib.request
# import re
#
# url = 'http://pythonprogramming.net/parse-website-using-regular-expressions-urllib/'
#
# req = urllib.request.Request(url)
# resp = urllib.request.urlopen(req)
# respData = resp.read()
# paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))
# for eachP in paragraphs:
#     print(eachP)
#

import subprocess

subprocess.call('ls',shell=True)
subprocess.call('python3 someScript.py "Hello Darkness, my old friend"', shell=True)
adj = 'cuck'
name = 'Larry'
print('You\'re a',adj,name)