from Tkinter import *
from dill.source import getsource
from functools import partial
from math import sqrt
from math import factorial

top = Tk()
def showResult(description, result, code):
    newtop = Toplevel()
    showcode = False
    def closeWin():
        newtop.withdraw()
    def showCode(code):
        showcode = True
        codebloc = Text(newtop)
        #codebloc.insert(INSERT, "code goes here")
        #print "heres code: "
        #print code
        codebloc.insert(INSERT, code)
        codebloc.insert(END, "")
        codebloc.pack()
    codefunc = partial(showCode, code)
    close = Button(newtop, text = "Close", command = closeWin)
    close.pack()
    code = Button(newtop, text = "Show Code", command = codefunc)
    code.pack()
    text = Text(newtop, height = 5, wrap = WORD)
    text.insert(INSERT, description)
    text.insert(INSERT, "\n")
    text.insert(END, result)
    text.pack()
    if showcode:
        text.insert(END, code)
    newtop.mainloop()

def getCode(func):
    allcode = getsource(eval(func))
    start = allcode.index("_BEGIN_") + len("_BEGIN_") + 1
    end = allcode.index("_END_", start) - 2
    code = str("".join(map(str, allcode[start:end])))
    return code

def p1():
    sum  = 0
    #begin code _BEGIN_
    for x in xrange(1, 1000):
        if x % 3 == 0 or x % 5 == 0:
            sum += x
    #_END_ end code
    result = "Sum = " + str(sum)
    code = getCode("p1")
    #print code
    showResult("Problem 1: Find sum of all the multiples of 3 or 5 below 1000",
                                result, code)
def p2():
    description = "Problem 2:  Find the sum of all even numbers within the Fibonacci sequence,"
    description += " not exceeding four million."
    #begin code _BEGIN_
    sum = 0
    n1 = 1
    n2 = 2
    while n1 < 4000000:
        if n1 % 2 == 0:
            sum += n1
        n2 += n1
        n1 = n2 - n1
    #_END_  end code
    result = "Sum = " + str(sum)
    code = getCode("p2")
    showResult(description, result, code)

def p3():
    description = "Problem 3: Find the largest prime factor of the number 600851475143"
    #_BEGIN_
    def isPrime(num):
        x = 2
        while x < sqrt(num):
            if num % x == 0:
                return False
            x += 1
        return True
    
    num = 600851475143
    primefactors = []
    i = 2
    while i < sqrt(num):
        if num %  i == 0:
            if isPrime(i):
                primefactors.append(i)
        i += 1
    #_END_
    result = "Largest prime factor is: " + str(max(primefactors))
    code = getCode("p3")
    showResult(description, result, code)
            
def p4():
    description = "Problem 4: Find the largest palindromic number which is the product of two 3-digit numbers"
     #_BEGIN_
    def isPalindrome(num):
        strnum = str(num)
        palindromic = True
        for x in xrange(0, len(strnum)/2):
            if strnum[x] != strnum[len(strnum) - x - 1]:
                palindromic = False
                break
        return palindromic
    i = 999
    j = 999
    palindromes = []
    while i > 0:
        while j > 0:
            if isPalindrome(i * j):
                palindromes.append(i * j)
            j -= 1
        i -= 1
        j = 999
    #_END_
    result = "Largest palindrome is: " + str(max(palindromes))
    code = getCode("p4")
    showResult(description, result, code)

def p5():
    description = "Find the smallest positive number evenly divisible by all the numbers"
    description += " from 1 to 20."
    #_BEGIN_
    def isDivisible(num):
        for x in xrange(1, 21):
            if num % x != 0:
                return False
        return True
    num = 20
    print factorial(20)
    while num < factorial(20):
        if isDivisible(num):
            break
        if num %1000000 == 0:
            print num
        num += 20
    #_END_
    result = "Smallest number divisible is: " + str(num)
    code = getCode("p5")
    showResult(description, result, code)

def p6():
    description = "Find the difference of the sum of the squares of the first hundred"
    description += " natural numbers and the square of the sum of the first hundred natural numbers."
    #_BEGIN_
    sum1 = 0
    sum2 = 0
    for x in xrange(1, 101):
        sum1 += x
        sum2 += x * x
    sum1 *= sum1
    diff = sum1 - sum2
    #_END_
    result = "Difference is: " + str(diff)
    code = getCode("p6")
    showResult(description, result, code)

def p7():
    description = "Find the 10001st prime number."
    #_BEGIN_
    primes = [2, 3]
    def isPrime(num):
        x = 2
        while x < sqrt(num):
            if num % x == 0:
                return False
            x += 1
        return True
    numprimes = 2
    i = 5
    interval = 2
    while numprimes < 10002:
        if isPrime(i):
            primes.append(i)
            numprimes += 1
        i += interval
    #_END_
    result = "10001st prime is: " + str(primes[10001])
    code = getCode("p7")
    showResult(description, result, code)

B1= Button(top, text = "Problem 1", command = p1)
B2 = Button(top, text = "Problem 2", command = p2)
B3 = Button(top, text = "Problem 3", command = p3)
B4 = Button(top, text = "Problem 4", command = p4)
B5 = Button(top, text = "Problem 5", command = p5)
B6 = Button(top, text = "Problem 6", command = p6)
B7 = Button(top, text = "Problem 7", command = p7)
B1.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()
B6.pack()
B7.pack()

top.mainloop()
