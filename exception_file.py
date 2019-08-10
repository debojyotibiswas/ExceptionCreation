from datetime import datetime as d

class Exceptions:

    def fileNotFound(self,value):
        with open('result.txt','a') as fp:
            now = d.now()
            dt = now.strftime("%d/%m/%Y %H:%M:%S")
            fp.write(dt)
            fp.write('\n')
            fp.write(value)
            fp.write('\n')
    
    def zeroDivision(self,value):
        with open('result.txt','a') as fp:
            now = d.now()
            dt = now.strftime("%d/%m/%Y %H:%M:%S")
            fp.write(dt)
            fp.write('\n')
            fp.write(value)
            fp.write('\n')

    def indexError(self,value):
        with open('result.txt','a') as fp:
            now = d.now()
            dt = now.strftime("%d/%m/%Y %H:%M:%S")
            fp.write(dt)
            fp.write('\n')
            fp.write(value)
            fp.write('\n')

    def valueError(self,value):
        with open('result.txt','a') as fp:
            now = d.now()
            dt = now.strftime("%d/%m/%Y %H:%M:%S")
            fp.write(dt)
            fp.write('\n')
            fp.write(value)
            fp.write('\n')

