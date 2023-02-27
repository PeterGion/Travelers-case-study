import sys
 
last_key = None
running_total = 0
wordList = []
wordSet = set(wordList)

for line in sys.stdin:
   line = line.strip()
   this_key, value = line.split('\t',1)
   if last_key == this_key:  # but first output last key and total
       wordSet.add(value)
   else:  # begin processing new key
       if last_key:  # but first output last key and total
           print(last_key, "\t", wordSet)
       wordSet.clear()
       last_key = this_key


if last_key == this_key:
   print(last_key, "\t", wordSet)