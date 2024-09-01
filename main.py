import cal_module

print(cal_module.add(2,3))

# fp = open("sample.txt",'r+')
# fp.write("Sunildd")
# #fp.seek(0)
# print(fp.seekable())
# print(fp.tell())
# print(fp.read())

# fp = open("sample.txt",'a')
# print(fp.tell())
# fp.write("varikala")
# fp.close()
# fp = open("sample.txt",'r')
# print(fp.read())
# os.mkdir('new-dir')
# import os
# print(os.getcwdb())
#methods in os module are:
''' 
  create a directory -> os.mkdir(name)
  rename a directory -> os.rename(d1,d2)
                       -> os.renames(d1,'pathd2'
  delete a directory -> od.rmdir(dir_name)-> if the contents in it is empty only
                 length of it =  os.listdir(dir_name) = 0 - > delete
    os.getcwd(dir_name)
    os.chdir(d1,d2)
    
    All Methods on os module are
    os.mkdir(dn)
    os.rename(d1,d2)
    os.renames(d1,'pathd2')
    os.rmdir(d1)
    os.listdir(dn)
    od.getcwd()
    os.chdir()
    os.path.isdir(dn)
    os.path.getsize(dname)
    os.path.getmtime()
    os.path.getatime()    

    All Methods in filecmp module
    d = filecmp.dircmp(d1,d2,hide=[],ignore=[])
    d.report()
    d.report_partial_closure()
    d.report_full_closure()


    All Methods in tempfile module
    mkdtemp()
    TempDirectory()


    Methods for shutil module

    shutil.rmtree()
    shuil.copytree(s,d)
    shutil.move(s,d)->source,destination
    '''

# dic ={1:'a'}
# print(dic)

# dic1 = {}
# for key,value in dic.items():
#     dic1[value] = key
# print(dic1)

n = 23
days = 365
pro = 1
for i in range(0,n):
    pro *= (days - i) / days
pro = 1 - pro
print("%.4f"%pro)