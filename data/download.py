def internet():
	import time
	import urllib.request
	try:
		print('\n\n\tDownloading required PDF from KTU Official Website\n')
		url = "https://bashshocker.000webhostapp.com/pec.pdf"
		urllib.request.urlretrieve(url, 'pec.pdf')
		print('\n\n\tFile downloaded successfully')
	except:
		print('\n\n\tPlease connect to the internet!')
		print('\n\n\tExiting...')
		time.sleep(5)
		quit()
					