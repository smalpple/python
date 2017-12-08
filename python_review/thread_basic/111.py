filename = '111.txt'
f=open('111.txt','r')
new_line = ""
for line in f.readlines():
    #print(line)
    line = line.strip('\n')
    x = line.split(" ")
    #print(x)
    d = open('222.txt', 'a')
    for i in range(1,len(x)):
        new_line = x[i]+"   "+x[0]
        print(new_line)
        d.write(new_line+'\n')
    d.close()
f.close()

