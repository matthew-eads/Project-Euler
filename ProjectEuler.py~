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
def p8():
    description = "Find the thirteen adjacent digits in the following"
    description += " 1000-digit number whith the greatest product"
    number = "73167176531330624919225119674426574742355349194934"
    number += "96983520312774506326239578318016984801869478851843"
    number += "85861560789112949495459501737958331952853208805511"
    number += "12540698747158523863050715693290963295227443043557"
    number += "66896648950445244523161731856403098711121722383113"
    number += "62229893423380308135336276614282806444486645238749"
    number += "30358907296290491560440772390713810515859307960866"
    number += "70172427121883998797908792274921901699720888093776"
    number += "65727333001053367881220235421809751254540594752243"
    number += "52584907711670556013604839586446706324415722155397"
    number += "53697817977846174064955149290862569321978468622482"
    number += "83972241375657056057490261407972968652414535100474"
    number += "82166370484403199890008895243450658541227588666881"
    number += "16427171479924442928230863465674813919123162824586"
    number += "17866458359124566529476545682848912883142607690042"
    number += "24219022671055626321111109370544217506941658960408"
    number += "07198403850962455444362981230987879927244284909188"
    number += "84580156166097919133875499200524063689912560717606"
    number += "05886116467109405077541002256983155200055935729725"
    number += "71636269561882670428252483600823257530420752963450"
    description += str(number)
    #_BEGIN_
    #not coded
    #_END_
    result = number
    code = getCode("p7")
    showResult(description, result, code)

B1= Button(top, text = "Problem 1", command = p1)
B2 = Button(top, text = "Problem 2", command = p2)
B3 = Button(top, text = "Problem 3", command = p3)
B4 = Button(top, text = "Problem 4", command = p4)
B5 = Button(top, text = "Problem 5", command = p5)
B6 = Button(top, text = "Problem 6", command = p6)
B7 = Button(top, text = "Problem 7", command = p7)
B8 = Button(top, text = "Problem 8", command = p8)
B1.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()
B6.pack()
B7.pack()
B8.pack()

top.mainloop()
