def sign():
	import base64
	print('\n\n\t\tSIGNUP MENU')
	checking = True
	while checking:
		output_file1 = 'usernames.encrypted'
		output_file2 = 'passwords.encrypted'
		username = input('\n\n\tEnter your username : ')
		password = input('\n\n\tEnter your password : ')
		enc_u = str.encode(username)
		enc_p = str.encode(password)
		username_enc = base64.b64encode(enc_u)
		password_enc = base64.b64encode(enc_p)
		dec_u = username_enc.decode()
		dec_p = password_enc.decode()
		def check():
			    with open('usernames.encrypted') as f:
			        datafile = f.readlines()
			    found = False  
			    for line in datafile:
			        if dec_u in line:
			           
			            return True
			    return False 

		
		if check() :
				print('\n\n\tUsername already exists! Try another one')
				checking = True
		else:
			break


	with open(output_file1, 'a') as f:
	    f.write(dec_u)
	    f.write('\n')
	with open(output_file2, 'a') as m:
	    m.write(dec_p)
	    m.write('\n')
	print(f'\n\n\t{username} is successfully signed up!!')
