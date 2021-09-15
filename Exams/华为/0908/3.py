import collections


class Compile:
    def calc(self, modules,target):
        def dfs(name):
            if modules[name]==0:
                return -1
            time,depend,visited,compileTime=modules[name]
            if compileTime!=-1:
                return compileTime
            if visited==1:
                return -1
            modules[name][2]=1
            maxVal=0
            for i in depend:
                tmp=dfs(i)
                if tmp==-1:
                    return -1
                if tmp>maxVal:
                    maxVal=tmp
            modules[name][3]=time+maxVal
            return time+maxVal
        return dfs(target)



com = Compile()
target = input().strip()
modules = collections.defaultdict(int)
index = 0
while True:
    try:
        line = input().strip().split(',')
        name,time=line[0],int(line[1])
        depend = line[2:]
        modules[name]=[time,depend,0,-1]
    except:
        break
# {'module1': ['10', 0], 'module2': ['5', 1], 'module3': ['10', 2, 'module1', 'module2']}
res = com.calc(modules,target)
print(res)
