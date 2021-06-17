import time
from copy import deepcopy
from collections import OrderedDict 
import enchant 
d = enchant.Dict("en_US") 

''' *************************************defining positions for game*******************************************'''
columns = '123456789' #using 1to9 for column numbering
rows    = 'ABCDEFGHI' #using AtoEfor row numbering
div_columns=('123','456','789')
div_rows = ('ABC','DEF','GHI')
alphabets=''
matrix  =  []
def matrix_generator(row, col):
	m_gen =  [r+c for r in row for c in col]
	return m_gen
'''**************************************defining the csp**************************************************'''
class csp:
	def __init__ (self,ip,matrix):
		self.variables = matrix #variables = all positions of the game matrix
		i = 0
		self.domain= {}
		for v in self.variables:
			if ip[i]!='*':
				self.domain[v] = ip[i]
			else:
				self.domain[v] = alphabets
			i = i + 1
		j=0
		self.val = {}
		for v in self.variables:
			if ip[j]!='*':
				self.val[v] = ip[j]
			else:
				self.val[v] = alphabets
			j = j + 1
		self.r_c_s_matrix = []
		for c in columns:
			self.r_c_s_matrix.append(matrix_generator(rows, c))
		for r in rows:
			self.r_c_s_matrix.append(matrix_generator(r,columns))
		for d_c in div_columns:
			for d_r in div_rows:
				self.r_c_s_matrix.append(matrix_generator(d_r,d_c))

		self.zone = {}
		for m in matrix:
			self.zone[m] = [x for x in self.r_c_s_matrix if m in x]
		self.neighbors = {}
		for m in  matrix:
			self.neighbors[m] = (((set(sum (self.zone[m],[])))- set([m])))
		
		self.constraints=[]
		for v in self.variables:
			for n in self.neighbors[v]:
				self.constraints.append((v,n))
''' ********************************************BACKTRACK*************************************'''
def BacktrackingSearch(csp):
	return Backtrack({},csp)
#recursive backtrack
def Backtrack(assignment, csp):
	
	if (complete(assignment) == True):#if the matrix becomes complete then return assignment
		return assignment
	var = MRV(assignment, csp)#using MRV approach choose next variable
	domain = deepcopy(csp.val)
	for value in csp.val[var]:
		if (consistent(var, value, assignment, csp)==True):#check consistency of each 
			assignment[var] = value
			inferences = {}
			inferences = inference(assignment, inferences, csp, var, value)
			if inferences!= "false":
				result = Backtrack(assignment, csp)
				if result!="false":
					return result
			del assignment[var]
			csp.val.update(domain)

	return "false"

def complete(assignment): #checks if assignment is complete
	return set(assignment.keys())==set(matrix)


def MRV(assignment, csp):#select nxt var using MRV
	var_next = dict((matrix, len(csp.val[matrix])) for matrix in csp.val if matrix not in assignment.keys()) #constains the keys that arenot yet assigned
	return min(var_next, key=var_next.get)#choosing the variable with fewest legal values


def consistent(var, value, assignment, csp):#checks consistency
	for neighbor in csp.neighbors[var]:
		if neighbor in assignment.keys() and assignment[neighbor]==value:	 
			return False
	return True

def inference(assignment, inferences, csp, var, value):#inference check
	inferences[var] = value
	for neighbor in csp.neighbors[var]:
		if neighbor not in assignment and value in csp.val[neighbor]:
			if len(csp.val[neighbor])==1:
				return "false"

			remaining = csp.val[neighbor].replace(value, "")
			if len(remaining)==1:
				flag = Inference(assignment, inferences, csp, neighbor, remaining)
				if flag=="false":
					return "false"

	return inferences

def show(val):#grid view
    for r in rows:
    	if r in 'DG':
    		print ("******************************************")
    	for c in columns:
    		if c in '47':
    			print (' | ', val[r+c], ' ',end=' ')
    		else:
    			print (val[r+c], ' ',end=' ')
    	print (end='\n')

def convert_to_string(val):#to generate the string representation for writing into file
	val1 = ""
	for variable in matrix:
		val1=val1+val[variable]
	return val1


def removeDup(string):#removes duplicates 
    u = '' 
    for x in string: 
        if not(x in u): 
            u = u + x 
    return u
'''**************************************main************************************'''
if __name__ == "__main__":
	start_time = time.time()
	
	ip=''
	with open("input.txt",'r') as f:
		ip = f.read().replace('\n','')
	for i in ip:
		if(i!='*'):
			alphabets+=i
	alphabets= removeDup(alphabets) #to generate the values in domain set
	matrix = matrix_generator(rows , columns)
	game = csp(ip,matrix)
	solution = BacktrackingSearch(game)
	search_time = time.time()
	print('search_time:',search_time-start_time)

	if solution!="false":
		show(solution)
		s = convert_to_string(solution)
		i=0
		f = open("solution.txt", "w")
		#print(s)
		for x in s:
			if(i%9==0):
				f.write('\n')
			f.write(x)
			i+=1
		f.write('\n\nMeaningful words if any:')
		#checks for meaningful words
		r0=r1=r2=r3=r4=r5=r6=r7=r8=""
		count = 0
		for a in s:
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
		for a in s:
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
		elif(d.check(c0)==True):
			f.write(c1)
		elif(d.check(c2)==True):
			f.write(c2)
		elif(d.check(c3)==True):
			f.write(c3)
		elif(d.check(c4)==True):
			f.write(c4)
		elif(d.check(c5)==True):
			f.write(c5)
		elif(d.check(c6)==True):
			f.write(c6)
		elif(d.check(c7)==True):
			f.write(c7)
		elif(d.check(c8)==True):
			f.write(c8)
		else:
			f.write('\n')
			f.write('None in columns')

		d1 = d2 = ""
		count=0
		for a in s:
			if(count%10==0):
				d1+=a
			elif(count%8==0):
				d2+=a
			count+=1
		if(d.check(d1)==True):
			f.write(d1)
		elif(d.check(d2)==True):
			f.write(d2)
		else:
			f.write('\n')
			f.write('None in diagonals')
	else:
		print ("Couldnot solve")
	f.close()
	total_time=time.time()
	print('total_time',total_time-start_time)
	
	