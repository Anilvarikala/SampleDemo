
file_name = 'a.txt'
f = open(file_name,'r')
l = f.read().splitlines()
l1 = ['h','k',""]
for i in l1:
    l.append(i)
f.close()
f = open(file_name,'w+')
for i in l:
    f.write(i+'\n')
f.seek(0)

print(f.read())
f.close()