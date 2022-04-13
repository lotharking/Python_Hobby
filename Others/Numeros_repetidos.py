class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        out = False
        a=0
        ac=0
        cont=[]

        for i in range(len(trips)):
            a+=trips[i][0]
        for i in range(len(trips)):
            ac=a
            fin=trips[i][2]
            ini=trips[i][1]
            for j in range(len(trips)):
                if (fin<=trips[j][1]):
                    ac-=trips[j][0]
            cont.append(ac)
                
        if (a<=capacity):
            out=True
        return out
