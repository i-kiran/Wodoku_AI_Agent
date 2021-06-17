import sys
import random
import enchant 
import time
from itertools import chain 
d = enchant.Dict("en_US") 
alphabets = []

class MainClass():
    def __init__(self, alphabets,input_matrix, matrix_size, n_subcols, n_subrows):
        self.input_matrix = input_matrix
        self.matrix_size = matrix_size
        self.n_subcols = n_subcols
        self.n_subrows = n_subrows
        self.domain = {}
        self.setdomain()
    
    def valid(self, alpha, i, j):
        row = (i//3)*3
        col = (j//3)*3
        for a in range(9):
            if (a != j and self.input_matrix[i][a] == alpha):
                    return 0
        for b in range(9):
            if (b != i):
                #print('b',b,'j',j)
                if(self.input_matrix[b][j] == alpha):
                    return 0

        for x in range(row, row+3):
            for y in range(col, col+3):
                if (x != i and y != j and self.input_matrix[x][y]== alpha):
                        return 0
        return 1       
    def count_clashes(self, alpha, i, j) :
        row = (i//3)*3
        col = (j//3)*3        
        n_clashes = 0
        for a in range(9):
            if (a != j and self.input_matrix[i][a] == alpha):
                    n_clashes = n_clashes+1
        for b in range(9):
            if (b != i):
                if(self.input_matrix[b][j] == alpha):
                    n_clashes = n_clashes+1
        for y in range(row, row+3):
            for x in range(col, col+3):
                if (y != i and x != j and self.input_matrix[y][x]== alpha):
                        n_clashes = n_clashes+1
        return n_clashes
        
    def setdomain(self):
        valid_domain = []
        for i in range(9):
            for j in range(9):
                if (self.input_matrix[i][j] == '*'):
                    valid_domain=[]
                    for alpha in alphabets:
                        if self.valid(alpha, i, j):
                            valid_domain.append(alpha)
                    self.domain[(i,j)] = valid_domain
    

    def min_conflicts(self):
        for i in range(100000):
            vals={}
            clashes = []
            num_clashes = 0
            m_val = 9223372036854775807
            lst = []
            for (i,j), alpha in self.domain.items():
                val = self.valid(self.input_matrix[i][j], i, j)
                n = random.random()
                if(val !=  1):
                    clashes.append((i,j))
                    num_clashes = num_clashes+1
                elif ( n < 0.03):
                    clashes.append((i,j))
            if(num_clashes == 0):
                return 1
            i, j = random.choice(clashes)
            alphabets = self.domain.get((i,j))
            for a in alphabets:
                vals[a] = self.count_clashes(a, i, j)
            for k,v in sorted(vals.items(), key=lambda item: item[1]):
                vals[k] = v
            for key, val in vals.items():
                if (val <= m_val):
                    lst.append(key)
                    m_val = val
                elif (n < 0.03):
                    lst.append(key)
            self.input_matrix[i][j] = random.choice(lst)
        return 0

    def display(self):
        
        flatten_list = list(chain.from_iterable(input_matrix))
        #print('==============',flatten_list)
        listToStr = ' '.join(map(str, flatten_list))
        listToStr =  listToStr.replace(" ", "")
        #print('sssssssss:',listToStr)

        f = open("solution.txt", "w")
        i=0
        for x in listToStr:
            if(i%9==0):
                f.write('\n')
            f.write(x)
            i+=1
        f.write('\n\nMeaningful words if any : ')
        r0=r1=r2=r3=r4=r5=r6=r7=r8=""
        count = 0
        for a in listToStr:
            if(count%9==0):
                r0+=a
            elif(count%9==1):
                r1+=a
            elif(count%9==2):
                r2+=a
            elif(count%9==3):
                r3+=a
            elif(count%9==4):
                r4+=a
            elif(count%9==5):
                r5+=a
            elif(count%9==6):
                r6+=a
            elif(count%9==7):
                r7+=a
            elif(count%9==8):
                r8+=a
            count+=1
        if(d.check(r0)==True):
            f.write(r0)
        elif(d.check(r0)==True):
            f.write(r1)
        elif(d.check(r2)==True):
            f.write(r2)
        elif(d.check(r3)==True):
            f.write(r3)
        elif(d.check(r4)==True):
            f.write(r4)
        elif(d.check(r5)==True):
            f.write(r5)
        elif(d.check(r6)==True):
            f.write(r6)
        elif(d.check(r7)==True):
            f.write(r7)
        elif(d.check(r8)==True):
            f.write(r8)
        else:
            f.write('\n')
            f.write('None in columns')

        count=0
        c0=c1=c2=c3=c4=c5=c6=c7=c8=""
        for a in listToStr:
            if(count >=0 and count <=8):
                c0+=a
            elif(count >=9 and count <=17):
                c1+=a
            elif(count >=18 and count <=26):
                c2+=a
            elif(count >=27 and count <=35):
                c3+=a
            elif(count >=36 and count <=44):
                c4+=a
            elif(count >=45 and count <=53):
                c5+=a
            elif(count >=54 and count <=62):
                c6+=a
            elif(count >=63 and count <=71):
                c7+=a
            elif(count >=72 and count <=80):
                c8+=a
            count+=1
        if(d.check(c0)==True):
            f.write(c0)
        if(d.check(c0)==True):
            f.write(c1)
        if(d.check(c2)==True):
            f.write(c2)
        if(d.check(c3)==True):
            f.write(c3)
        if(d.check(c4)==True):
            f.write(c4)
        if(d.check(c5)==True):
            f.write(c5)
        if(d.check(c6)==True):
            f.write(c6)
        if(d.check(c7)==True):
            f.write(c7)
        if(d.check(c8)==True):
            f.write(c8)
        d1 = d2 = ""
        count=0
        for a in listToStr:
            if(count%10==0):
                d1+=a
            elif(count%8==0):
                d2+=a
            count+=1
        if(d.check(d1)==True):
            f.write(d1)
        if(d.check(d2)==True):
            f.write(d2)
    
        f.close()
        #printing o/p
        for y in range(9):
            print('| ', end='')
            if y!= 0 and y%3 == 0:
                for j in range(9):
                    print(' * ', end='')
                    if (j + 1) <9 and (j + 1)%3== 0:
                        print(' - ', end='')   
                print(' |')
                print('| ', end='')
            for x in range(self.matrix_size):
                if x!=0 and x %3== 0:
                    print(' | ', end='')
                digit = str(self.input_matrix[y][x]) if len(str(self.input_matrix[y][x])) > 1 else ' ' + str(self.input_matrix[y][x])
                print('{0} '.format(digit), end='')
            print(' |')
def removeDup(string): 
    u = '' 
    for x in string: 
        if not(x in u): 
            u = u + x 
    return u 
if __name__ == "__main__":
    start_time = time.time()
    a=''
    matrix_size = n_rows = n_cols = 9
    ip=''#get matrix in i/p form from file
    with open("input.txt",'r') as f:
        ip = f.read().replace('\n','') #input
    #print(ip)
    #range of possible values
    for i in ip:
        if(i!='*'):
            a+=i
    a= removeDup(a)
    alphabets=list(a)
    mat=[]
    for i in ip:
        mat.append(i)
    #print('matrix',mat)
    row_size = 0
    input_matrix = []
    list1=[]
    #forming a 2D array
    for i in mat:
        list1.append(i)
        row_size+=1
        if(row_size >= 9 ):
            input_matrix.append(list1)
            list1=[]
            row_size = 0

    #print('i/p:',input_matrix)
    #print('i/p:',input_matrix[8][0])
    n_subrows = 3
    n_subcols = 3 
    solution = MainClass(alphabets,input_matrix, matrix_size, n_subrows, n_subcols)
    success = solution.min_conflicts()
    search_time=time.time()
    print('search_time',search_time-start_time)
    if success == True:
        print('Wordoku solution:')
    else:
        print('No solution')
    solution.display()
    total_time=time.time()
    print('total_time',total_time-start_time)