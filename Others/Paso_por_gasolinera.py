#Esta a modo de metodo lo comentado, sin comentar esta el metodo funcional
##class Solution(object):
##    def canCompleteCircuit(self, gas, cost):
##        """
##        :type gas: List[int]
##        :type cost: List[int]
##        :rtype: int
##        """
##        z=-1
##        x=1
##        y=0
##        while(x==1):
##            out=0
##            d=y
##            e=d
##            for i in range(len(gas)):
##                if (i==0):
##                    if (d==len(gas)-1):
##                        out=gas[d]-cost[d]
##                        if(out<0):
##                            z=-1
##                            break
##                        else:
##                            z=0
##                        out=out+gas[0]
##                        d=0
##                    else:
##                        out=gas[d]-cost[d]
##                        if(out<0):
##                            z=-1
##                            break
##                        else:
##                            z=0
##                        out=out+gas[d+1]
##                        d+=1
##                else:
##                    if (d==len(gas)-1):
##                        out+=-cost[d]
##                        if(out<0):
##                            z=-1
##                            break
##                        else:
##                            z=0
##                        out=out+gas[0]
##                        d=0
##                    else:
##                        out+=-cost[d]
##                        if(out<0):
##                            z=-1
##                            break
##                        else:
##                            z=0
##                        out=out+gas[d+1]
##                        d+=1
##            if(y<len(gas)-1):
##                y+=1
##            else:
##                x=0
##            if (z==0):
##                break
##
##        if(z==-1):
##            return -1
##        if (z==0):
##            return e


gas  = [2,3,4]
cost = [3,4,3]
##gas  = [5,1,2,3,4]
##cost = [4,4,1,5,1]
z=-1
x=1
y=0
while(x==1):
    out=0
    d=y
    e=d
    for i in range(len(gas)):
        if (i==0):
            if (d==len(gas)-1):
                out=gas[d]-cost[d]
                if(out<0):
                    z=-1
                    break
                else:
                    z=0
                out=out+gas[0]
                d=0
            else:
                out=gas[d]-cost[d]
                if(out<0):
                    z=-1
                    break
                else:
                    z=0
                out=out+gas[d+1]
                d+=1
        else:
            if (d==len(gas)-1):
                out+=-cost[d]
                if(out<0):
                    z=-1
                    break
                else:
                    z=0
                out=out+gas[0]
                d=0
            else:
                out+=-cost[d]
                if(out<0):
                    z=-1
                    break
                else:
                    z=0
                out=out+gas[d+1]
                d+=1
    if(y<len(gas)-1):
        y+=1
    else:
        x=0
    if (z==0):
        break

if(z==-1):
    print("-1")
##    return -1
if (z==0):
    print(e)
##    return e
