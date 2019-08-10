from exception_file import Exceptions
from traceback import format_exc

class random:
    def __init__(self):
        self.e = Exceptions()
        
    def file(self, name):
        try:
            with open(name) as f:
                print('file has been successfully opened')
        except:
            self.e.fileNotFound(format_exc())

    def zero(self, a, b):
        try:
            print('Result after division is ', a / b)
        except:
            self.e.zeroDivision(format_exc())

    def index(self, array, i):
        try:
            print('Value at index positions is ',array[i])
        except:
            self.e.indexError(format_exc())

    def value(self, var):
        try:
            print('You have entered integer ',int(var))
        except:
            self.e.valueError(format_exc())

def main():
    r = random()
    while True:
        print('Enter your choice...')
        print('1 for opening a file')
        print('2 for division')
        print('3 for accessing element of an array')
        print('4 for entering an integer as input')
        print('5 for exit')
        ch = int(input('Enter a number : '))
        if ch == 1:
            print('Enter name of the file')
            name = input()
            r.file(name)
            print('\n')
        elif ch == 2:
            print('Enter two numbers...')
            a, b = map(int, input().split())
            r.zero(a, b)
            print('\n')
        elif ch == 3:
            print('Enter an array..')
            ar = list(map(int, input().split()))
            print('Enter index position')
            i = int(input())
            r.index(ar, i)
            print('\n')
        elif ch == 4:
            nm = input('Enter an integer : ')
            r.value(nm)
            print('\n')
        elif ch == 5:
            break
        else:
            print('Wrong choice!')
            print('\n')

if __name__ == '__main__':
    main()
