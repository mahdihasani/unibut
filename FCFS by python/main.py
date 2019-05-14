import re,time
from datetime import datetime

CommandList=[]


source=open('input.conf','r')
CommandList=source.readlines()

total=0
def do(command,delay):
    global total
    global CommandList
    total+=delay
    print("process {} working...".format(command)+" start at    "+str(datetime.now().time()))
    try:
        while(delay!=0):
            time.sleep(1)
            print(datetime.now().time())
            delay-=1
        print("process {} complete".format(command)+" at    "+str(datetime.now().time()))        
    except:
        CommandList.append(command+':'+str(delay)+'\n')
        print(command+' go to ready list!')





if __name__ == "__main__":
    
    for item in CommandList:
        
        line=re.search('(.*)(:)(.*)(\\n)',item)
        CommandName=line.group(1)
        CommandTime=line.group(3)
        do(CommandName,int(CommandTime))
    print("total time :"+str(total))
            
    Expectation=(total-int(re.search('(.*)(:)(.*)(\\n)',CommandList[0]).group(3))/len(CommandList))
    Response=0

    print("average expectation time :"+str(Expectation))
    print("Average response time :"+str(Response))
    stop=input()

