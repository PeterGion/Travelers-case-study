import sys
#print('enter something: ')
# get input from standard input, STDIN, one line at a time
for line in sys.stdin:
    line = line.strip() #remove leading and trailing whitespaces
    words = line.split() #split the line into words and returns as a list
    for word in words:
        #write the results to standard output, STDOUT
        print (word,"\t",1) #Emit key = word and value = 1