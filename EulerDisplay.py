from Tkinter import *
from dill.source import getsource
    class  EulerDisplay
         def showResult(self, description, result, code):
            newtop = Toplevel()
            showcode = False
            def closeWin():
                newtop.withdraw()
            def showCode(self):
                showcode = True
                codebloc = Text(newtop)
                codebloc.insert(INSERT, "code goes here")
                print "heres code: "
                print code
                codebloc.insert(INSERT, code)
                codebloc.insert(END, "")
                codebloc.pack()
            close = Button(newtop, text = "Close", command = closeWin)
            close.pack()
            code = Button(newtop, text = "Show Code", command = showCode)
            code.pack()
            text = Text(newtop)
            text.insert(INSERT, description)
            text.insert(INSERT, "\n")
            text.insert(END, result)
            text.pack()
            if showcode:
                text.insert(END, code)
            newtop.mainloop()
            
        def p1(self):
            sum  = 0
            #begin code _BEGIN_
            for x in xrange(1, 1000):
                if x % 3 == 0 or x % 5 == 0:
                    sum += x
            #_END_ end code
            result = "Sum = " + str(sum)
            allcode = getsource(p1)
            start = allcode.index("_BEGIN_") + len("_BEGIN_") + 1
            end = allcode.index("_END_", start) - 2
            code = str("".join(map(str, allcode[start:end])))
            print code
            showResult("Problem 1: Find sum of all the multiples of 3 or 5 below 1000",
                                        result, code)
        def p2(self):
                description = "Problem 2:  Find the sum of all even numbers within the Fibonacci sequence,"
                description += " not exceeding four million."
                sum = 0
                
