def hola():
	from datetime import datetime
	from datetime import date
	now = datetime.now()
	current_time = now.strftime("%H")
	new_time = int(current_time)
	if new_time >= 6 and new_time < 12 :
		print('\n\n\n\n\t\tGood Morning\n\n')
	if new_time >= 12 and new_time < 16 :
		print('\n\n\n\n\t\tGood Afternoon\n\n')
	if new_time >= 16 and new_time < 22 :
		print("\n\n\n\n\t\tGood Evening\n\n")
	if new_time >= 22 and new_time < 6 :
		print('\n\n\n\n\t\t\tA good sleep is always good for your health!!\n\n')
	n_time =now.strftime("%H:%M:%S")
	today = date.today()
	d2 = today.strftime("%B %d, %Y")
	print(f'\n\tToday is {d2} and its {n_time}')

