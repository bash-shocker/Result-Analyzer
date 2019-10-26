def table():
	import tabula
	print('\n\n\tConverting the downloaded PDF file to DATABASE.. Please wait, this might take a minute...')
	df = tabula.read_pdf("pec.pdf", encoding='utf-8', spreadsheet=True, pages='1-13')
	df.to_csv('pec.csv', encoding='utf-8')
	print('\n\n\tSuccessfully converted to Database..\n\n')