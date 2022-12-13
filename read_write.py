#Contants 
READ_TEST_PATH = "read_test.txt"
WRITE1_PATH = "write_test1.txt"

#Read Method1: Using readline
def read1(path):
	f = open(path, 'r')
	line = f.readline() 
	while line:
		print(line)
		line = f.readline()
	f.close()



#Read Method2: Using for loop and read 
def read2(path):
	lines = open(path,'r')
	for  line in lines:
		print(line)
	lines.close()


#Write Method1: Overriate entire file
def write1(path,content):
	f = open(path, 'w')
	f.write(content)
	f.close() 

#Write Method2: Add content to the file 
def write2(path, content):
	f = open(path, 'a')
	f.write(content)
	f.close()

def main():
	
	print("---------Read Method 1-----------")
		

	read1(READ_TEST_PATH)
	

	print("---------Read Method 2-----------")

	read2(READ_TEST_PATH)

	print("---------Write overwrite entire file --------")
	test_lines = "Line 1\nLine 2\nWrite 1\nWrite 2"
	write1(WRITE1_PATH, test_lines) 


	print("---------Write add to file --------")
	test_lines2 = "\nAppend 1\nAppend 2\nOver"
	write2(WRITE1_PATH, test_lines2)





if __name__ == "__main__":
	print("------READ_WRITE_TEMPLATE_START---------")
	main()
