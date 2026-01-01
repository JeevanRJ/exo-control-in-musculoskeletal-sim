import os

def WriteValue(context,Value,filename):
	filelocation = os.path.join(filename)
		
	with open(filelocation, 'w') as f:
		f.write("%s" %Value)
	
	t=Value
	
	return t