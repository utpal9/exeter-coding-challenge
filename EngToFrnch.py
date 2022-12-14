import csv
import time
import os, psutil

start = time.time() # start time of program


### replacing word ###

l = []
freq = {}
listvalue = {}

reader = csv.reader(open('./french_dictionary.csv', 'r'))
d = {}
for row in reader:
   k, v = row
   d[k] = v


with open('t8_shakespeare.txt','r') as file:
    filedata = file.read()

with open('find_words.txt','r') as file:
   
    # reading each line    
    for line in file:
   
        # reading each word        
        for word in line.split():
   
            # displaying the words           
            l.append(word.lower())

for findtext in l:
    occurence = filedata.count(findtext)
    #print(findtext,end="")
    #print(occurence)
    freq[findtext] = occurence
    filedata = filedata.replace(findtext,d[findtext])
    with open('t8_shakespeare.txt', 'w') as file:
        file.write(filedata)
        '''occurence = filedata.count(findtext)
        freq[findtext] = occurence'''
         
        

         
### replacing word end ###



with open('frequency.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=freq.keys())
    writer.writeheader()
    writer.writerow(freq)


end = time.time() # end time of program

exectime = end - start # actual time consumption

process = psutil.Process(os.getpid()) # actual memory consumption in bytes .


print(freq)
print("execution time : ",exectime)
print("memory consumption : ",process.memory_info().rss)
print('done')
  
        
    
                        
                    
                    
                
            
