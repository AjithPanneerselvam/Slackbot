import sys

arguments = sys.argv
#command = .split()
file_name= arguments[1]	
source = open(file_name, 'r')
content = source.read()
print content
