import os,sys
path=sys.argv[-1]
os.listdir(path)
print(path)
for filename in os.listdir(path):
    fnew = str(filename.split(".")[0])+"."+str(filename.split(".")[1])+".csv"
    os.rename(os.path.join(path, filename),os.path.join(path, fnew))
    print(filename,fnew )
