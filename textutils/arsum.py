#created by vishnu

from django.http import HttpResponse


# Complete the diagonalDifference function below.
def diagonalDifference(request):
	sum=0
	f1= input("Enter number 1")
	f2= input("Enter number 2")
	sum=f1-f2
	return HttpResponse(sum)
    
