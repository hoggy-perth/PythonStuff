#Program echos what you type once press enter 
#until you type q then enter 
#at which point it exits program with Exit message
import sys
for line in sys.stdin: 
    if 'q' == line.rstrip(): 
        break
    print(f'Input : {line}') 

print("Exit") 
