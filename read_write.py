#Contants 
READ_TEST_PATH = "read_test.txt"

#Method1: Using readline
def read1(path):
	f = open(path, 'r')
	line = f.readline() 
	while line:
		print(line)
		line = f.readline()
	f.close()



#Method2: Using for loop and read 
def read2(path):
	lines = open(path,'r')
	for  line in lines:
		print(line)
	lines.close()

def main():
	
	print("---------Read Method 1-----------")
		

	read1(READ_TEST_PATH)
	

	print("---------Read Method 2-----------")

	read2(READ_TEST_PATH)




if __name__ == "__main__":
	print("------READ_WRITE_TEMPLATE_START---------")
	main()
