def log():
	import base64
	import time
	print('\n\n\t\tLOGIN MENU')
	checking = True
	while checking:
		username = input('\n\n\tEnter your username : ')
		enc_u = str.encode(username)
		password = input('\n\n\tEnter your password : ')
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

		def check2():
		    with open('passwords.encrypted') as m:
		        datafile1 = m.readlines()
		    found = False  
		    for line1 in datafile1:
		        if dec_p in line1:
		            
		            return True
		    return False  

		if check() and check2() :
			print(f'\n\n\tWelcome {username}!!')
			checking = False
		else:
			print('\n\n\tOOPS Password/Username is incorrect try again!!')
			checking = True