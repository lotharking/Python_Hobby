#Esta a modo de metodo, quitar la identacion en caso de querer usar
import numpy as np

class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        x=[]
        out=[]
        ini=low
        for i in range(low,high+1):
            x.append(ini)
            ini=ini + 1

        x=np.array(x)
        for i in range(len(x)):
            y=x[i]
            nueve= int(y/(pow(10,9)))
            ocho=  int((y-nueve*pow(10,9))/pow(10,8))
            siete= int((y-nueve*pow(10,9)-ocho*pow(10,8) )/pow(10,7))
            seis=  int((y-nueve*pow(10,9)-ocho*pow(10,8)-siete*pow(10,7))/pow(10,6))
            cinco= int((y-nueve*pow(10,9)-ocho*pow(10,8)-siete*pow(10,7)-seis*pow(10,6))/pow(10,5))
            cuatro=int((y-nueve*pow(10,9)-ocho*pow(10,8)-siete*pow(10,7)-seis*pow(10,6)-cinco*pow(10,5))/pow(10,4))
            tres=int((y-nueve*pow(10,9)-ocho*pow(10,8)-siete*pow(10,7)-seis*pow(10,6)-cinco*pow(10,5)-     cuatro*pow(10,4))/pow(10,3))
            dos= int((y-nueve*pow(10,9)-ocho*pow(10,8)-siete*pow(10,7)-seis*pow(10,6)-cinco*pow(10,5)-cuatro*pow(10,4)-tres*pow(10,3))/pow(10,2))
            uno= int((y-nueve*pow(10,9)-ocho*pow(10,8)-siete*pow(10,7)-seis*pow(10,6)-cinco*pow(10,5)-cuatro*pow(10,4)-tres*pow(10,3)-dos*pow(10,2))/pow(10,1))
            cero=int((y-nueve*pow(10,9)-ocho*pow(10,8)-siete*pow(10,7)-seis*pow(10,6)-cinco*pow(10,5)-cuatro*pow(10,4)-tres*pow(10,3)-dos*pow(10,2)-uno*pow(10,1))/pow(10,0))
            if uno !=0:
                cont=1
            if dos !=0:
                cont=2
            if tres !=0:
                cont =3
            if cuatro !=0:
                cont=4
            if cinco !=0:
                cont=5
            if seis !=0:
                cont=6
            if siete !=0:
                cont=7
            if(ocho !=0):
                cont=8
            if nueve != 0:
                cont=9
            if cont==9:
                if nueve+1==ocho and ocho+1==siete and siete+1==seis and seis+1==cinco and cinco+1==cuatro and cuatro+1==tres and tres+1==dos and dos+1==uno and uno+1==cero:
                    out.append(y)
            if cont==8:
                if ocho+1==siete and siete+1==seis and seis+1==cinco and cinco+1==cuatro and cuatro+1==tres and tres+1==dos and dos+1==uno and uno+1==cero:
                    out.append(y)
            if cont==7:
                if siete+1==seis and seis+1==cinco and cinco+1==cuatro and cuatro+1==tres and tres+1==dos and dos+1==uno and uno+1==cero:
                    out.append(y)
            if cont==6:
                if seis+1==cinco and cinco+1==cuatro and cuatro+1==tres and tres+1==dos and dos+1==uno and uno+1==cero:
                    out.append(y)
            if cont==5:
                if cinco+1==cuatro and cuatro+1==tres and tres+1==dos and dos+1==uno and uno+1==cero:
                    out.append(y)
            if cont==4:
                if cuatro+1==tres and tres+1==dos and dos+1==uno and uno+1==cero:
                    out.append(y)
            if cont==3:
                if tres+1==dos and dos+1==uno and uno+1==cero:
                    out.append(y)
            if cont==2:
                if dos+1==uno and uno+1==cero:
                    out.append(y)
            if cont==1:
                if uno+1==cero:
                    out.append(y)
        return out

