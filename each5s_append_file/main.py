import time
i=0
while i<100:
    i+=1
    time.sleep(5)
    file = r'auto_create.txt'
    with open(file, 'a+') as f:
        f.write(str(i)+'\n') 


