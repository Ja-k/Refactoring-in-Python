import sys
import os.path
import subprocess
import urllib.request
from urllib.parse import urlparse
import re
argList = sys.argv

if len(argList) == 3:
    if os.path.exists(argList[2]):
        if re.match('https?://(?:www)?(?:[\w-]{2,255}(?:\.\w{2,6}){1,2})(?:/[\w&%?#-]{1,300})?',argList[1]):
            o = urlparse(argList[1])
            ss = o.path
            sss = ss.split("/")
            for t in sss:
                if t.endswith(".java"):
                    # print(t)
                    javafilename = t[:len(t)-5]
                    #print(javafilename)
        else:
            sys.exit("The url is not valid !!!")
    else:
        sys.exit("The local File does not Exist !!!")
else:
    sys.exit("Number of Argumets are not Correct !!!")

           
        
remote_dir = "C:\\Users\\HP x360\\Desktop\\"+javafilename+".java"
remoteFile = urllib.request.urlretrieve(argList[1],remote_dir)

outfile = []
with open(argList[2],'r') as lFile:
    with open(remote_dir,'r+') as rFile:
        for line in rFile.readlines():
            if "public class " in line:
               outfile.append(line)
               for l in lFile:
                   outfile.append(l)
               continue
            outfile.append(line)    
       # print(outfile)
     
with open(remote_dir, 'w') as rrFile:
    for line in outfile:
        rrFile.write(line)
        
outputfile = []        
        
with open(argList[2],'r') as sFile:                    
    with open(remote_dir,'r+') as rFile:
        for line in sFile.readlines():
            if "static String " in line:
                end = line.find("(")
                count = end
                while line[count] != " ":
                    count-=1
                #print(count,end)
                methodName = line[count+1:end+1]
                for r in rFile.readlines():
                    if "System.out.println(" in r:
                        e = r.find("(")
                        s = r.find(";")
                        le = len(r)
                        
                        if (s-e) >= 2:
                            rr= r.replace(r,r[:e+1]+methodName+r[e+1:le-2]+")"+r[le-2:])
                            outputfile.append(rr)
                            continue
                                             
                    outputfile.append(r)
                    
                    
with open(remote_dir,'w') as outputs:
    for i in outputfile:
        outputs.write(i)
        
                    
compout = subprocess.getoutput("javac "+javafilename+".java")

if len(compout) > 1:
    with open("C:\\Users\\HP x360\\Desktop\\COMP_ERR.txt",'w') as compileerror:
        compileerror.write(compout)
        
else:
    run = subprocess.getoutput("java "+javafilename)
    if re.match("Exception ",run):
        with open("C:\\Users\\HP x360\\Desktop\\ERROR.txt",'w') as error:
            error.write(run)
            print(run)
            
    else:
        with open("C:\\Users\\HP x360\\Desktop\\OUTPUT.txt",'w') as output:
            output.write(run)
            print(run)
