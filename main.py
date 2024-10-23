#tarana

def encoded(pass_string):
	encoded_string = ''
	int_list = [int(x) for x in pass_string]
	for i in range(len(int_list)):
		int_list[i]+=3
		encoded_string+=str(int_list[i])
	return encoded_string

if __name__ == "__main__":
	is_running = True	
	while is_running:
		print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
		operation = input("Please enter an option: ")
		
		if operation == '1':
			num_string = str(input("Please enter your password to encode: "))
			ans = encode(num_string)
        		print("Your password has been encoded and stored!")
		elif operation == '0':
			is_running = False 
