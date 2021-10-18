class PasswordException(Exception):
	def __init__(self,info):
		print(info)
pwd=input("Enter password :")
if len(pwd)<8:
	raise PasswordException("Minimum 8 characters")
else: 
	print("ok")
