import re
def check(inp): 
	if re.match(r'[a-zA-Z]{2}[0-9]{3}$', inp):
		pass
	else:
		print("\n\n\tOOPS!! You've entered the wrong Subject Code\n\n")
		