import os 

def search(str,dir='.'):
    for x in os.listdir(dir):
        temp = os.path.join(os.path.abspath(dir),x)
	if os.path.isdir(temp):
	   search(str,temp)
        if os.path.isfile(temp):
           if x.find(str) != -1:
	      print(x,'->',temp)
search('test')
