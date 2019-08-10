
with open('result.txt') as fp:
    
    line = fp.readline()
    while line:
        if line != '\n':
           print('Time when error occurred is : {}'.format(line.strip()))
           print('Error is :')
           for i in range(0, 4):
               line = fp.readline()
               print(line.strip())
           print('-------------------------------------------------')

        line = fp.readline()
           
