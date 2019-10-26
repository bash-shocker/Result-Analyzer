def caio():
	import time
	import sys
	s = '.'
	sys.stdout.write( '\n\n\tYour session will be now signed out' )
	i=1
	while i<25:
		sys.stdout.write( s )
		sys.stdout.flush()
		time.sleep(0.05)
		i=i+1
	
	print('\n\n\n\n\n\tProgrammed by Advaith Narayan For College Of Engineering Pathanapuram\n\n')
	time.sleep(2)