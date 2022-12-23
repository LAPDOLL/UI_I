# opening the file in read mode
my_file = open("terrorist.txt", "r")
  
# reading the file
data = my_file.read( )
  
# replacing end of line('/n') with ' ' and # splitting the text it further when '.' is seen.
data_into_list = data.replace('\n', ' ').split(".")
  
# printing the data
print(data_into_list)
my_file.close()
              
def tabulate(data_into_list):
	line_num = 1
	for line in data_to_list:
	                      	if line_num == 1:
	                      		A = list(line)
	                      	if line_num == 2:
	                      		B = list(line)
	                      	if line_num == 3:
	                      		C = list(line)
	                      	if line_num == 4:
	                      		A = list(line)
	                      	if line_num == 5:
	                      		B = list(line)
	                      	if line_num == 6:
	                      		C = list(line)
	                      	if line_num == 7:
	                      		A = list(line)
	                      	if line_num == 8:
	                      		B = list(line)
	                      	if line_num == 9:
	                      		C = list(line)
	                      	if line_num == 10:
	                      		D = list(line)
	                      		
	                      	line_num += 1
	                      	
	from tabulate import tabulate
	# assign data
	mydata = [
                       [1,A,sum(A),3]
                       [2,B,sum(B),None]
                       [3,C,sum(C),1]
                       [4,D,sum(D),6]
                       [5,E,sum(E),9]
                       [6,F,sum(F),4]
                       [7,G,sum(G),None]
                       [8,H,sum(H),None]
                       [9,I,sum(I),5]
                       [10,J,sum(J),None]
                                                         ]
     # create header
      headers = ["S_N","listofnum","sum","duplicateID"]
      
      # display table
      print(tabulate(mydata, headers, tablefmt="grid"))

def plot(tabulate(data_into_list)):
	import matplotlib.pyplot as plt
	
	plt.plot(S_N,duplicateID)
	plt.show( )
	