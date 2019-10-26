from data import welcome
from data import loading
from data import login
from data import signup
from data import download
from data import pdf_csv_converter
from data import sorting
from data import bye
import sys
import time
from os import path
################################################################################
################################################################################
################################################################################
welcome.hola()
loading.text()
account = input('\n\n\tDo you have an account?(y/n) :')
if account == 'y':
	login.log()
	download.internet()
	pdf_csv_converter.table()
	sorting.calc()
	bye.caio()
elif account == 'n':
	signup.sign()
	login.log()
	download.internet()
	pdf_csv_converter.table()
	sorting.calc()
	bye.caio()
else:
	print('\n\n\tWrong Choice!!!! Try again!')


