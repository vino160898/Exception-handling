print("-----------first aproach--------------")
import traceback
try:	
	no1=int(input("Enter no "))
	no2=int(input("Enter no "))
	no3=input("Enter no ")
	print(no1/no2)
	print(no2+no3)
except (ZeroDivisionError,ValueError,TypeError) as msg:
	print("Error occurred" , msg)
except:
 	traceback.print_exc()
print("-----------second aproach--------------")
import traceback
import sys
no1=100
no2=0
try:
	print(no1/no2)
except:
	traceback.print_exception(*sys:exc_info())
