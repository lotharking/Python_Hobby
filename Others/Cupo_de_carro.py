#lo comentado es como metodo
import numpy as np
##class Solution(object):
##    def majorityElement(self, nums):
##        """
##        :type nums: List[int]
##        :rtype: List[int]
##        """
##        out=[]
##        
##        for i in range (len(nums)):
##            count=0
##            a=nums[i]
##            for j in range(len(nums)):
##                if(a==nums[j]):
##                    count+=1
##            if(count>=3):
##                if nums[i] not in out:
##                    out.append(nums[i])
##        if(out==[]):
##            for i in range (len(nums)):
##                count=0
##                a=nums[i]
##                for j in range(len(nums)):
##                    if(a==nums[j]):
##                        count+=1
##                if(count>=2):
##                    if nums[i] not in out:
##                        out.append(nums[i])
##                
##        return out
out=[]
nums=[1,1,1,3,3,2,2,2]


for i in range (len(nums)):
    count=0
    a=nums[i]
    for j in range(len(nums)):
        if(a==nums[j]):
            count+=1
    if(count>=3):
        if nums[i] not in out:
            out.append(nums[i])
if(out==[]):
    for i in range (len(nums)):
        count=0
        a=nums[i]
        for j in range(len(nums)):
            if(a==nums[j]):
                count+=1
        if(count>=2):
            if nums[i] not in out:
                out.append(nums[i])
print(out)
