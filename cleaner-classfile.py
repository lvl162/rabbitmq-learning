import os

# filelist = [ f for f in os.listdir('')  ]
# for f in filelist:
#     print(f)
#     # os.remove(os.path.join(mydir, f))

def traversal(dir="./"):
    if os.path.isdir(dir):
        filelist = [ os.path.join(dir, f) for f in os.listdir(dir) ]
        print(filelist)
        for f in filelist:
            traversal(f)
    else:
        if (dir.endswith('.class')):
            print("+++", dir)   
            os.remove(dir)
            # return
traversal()
    

