import numpy as np

def mem_man(f,out):
    fp1 = open(f,"r")
    fp2 = open(out,"w")
    i = 0
    frames = []
    a = fp1.readline()
    fp2.write("Logical address"+","+"Physica address\n")
    while(a != ""):
        off = int(a) % 4096
        pnum = int(int(a)/4096)
        if(pnum in frames):
            fnum = frames.index(pnum)
            padd = fnum*4096 + off
            fp2.write(str(int(a))+","+str(padd)+"\n")
        else:
            frames.append(pnum)
            fnum = frames.index(pnum)
            padd = fnum*4096 + off
            fp2.write(str(int(a))+","+str(padd)+"\n")
        a = fp1.readline()

mem_man("data.txt","output.txt")
