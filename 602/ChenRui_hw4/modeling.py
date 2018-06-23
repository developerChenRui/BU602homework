# Copyright 2017 ChenRui ruirui@bu.edu
class Polynomial():

    def __init__(self,sequence=[]):
        self.coefficients = {}
        for i in range(len(sequence)):
            self.coefficients[len(sequence)-1-i] = sequence[i]
     

    def __add__(self,sequence):
        a=Polynomial()
        ans={}
        for i in self.coefficients:
            ans[i] = self.coefficients[i]
        value = sequence.coefficients if hasattr(sequence,'coefficients') else Polynomial(sequence)
        for i in value:
            if self.coefficients.__contains__(i):
                ans[i] =self.coefficients[i]+value[i]   
            else:
                ans[i]=value[i]
        a.coefficients=ans
        return a
    
    def __len__(self):
        return len(self.coefficients)
    def __sub__(self,sequence):
        value = sequence if hasattr(sequence,'coefficients') else Polynomial(sequence)
 #       print(value.coefficients)
        for i in value.coefficients:
            value[i] = 0-value[i]
        return (self+value)
    
    def __mul__(a,b):
        ans = {}
        k=Polynomial()
        for i in a.coefficients:
            for j in b.coefficients:
                if ans.__contains__(i+j):
                    ans[i+j]= a[i]*b[j]+ans[i+j]
                else:
                    ans[i+j]=a[i]*b[j]
        k.coefficients=ans
        return k
    
    def __eq__(a,b):
        a_value = a.coefficients if hasattr(a,'coefficients') else Polynomial(a).coefficients
        b_value = b.coefficients if hasattr(b,'coefficients') else Polynomial(b).coefficients
        if len(a_value) != len(b_value):
            return False
        for i in a_value:
            if a_value[i]!=b_value[i]:
                return False
        return True
    
    def __getitem__(self,index):
        if self.coefficients.__contains__(index):
            return self.coefficients[index]
        else:
            return 0
            
#        
    def __setitem__(self,index,value):
        self.coefficients[index]=value
        
#                
    def eval(self,value):
        ans = 0
        for i in self.coefficients:
            ans+=self.coefficients[i]*(value**(i))
        return ans
#    
    def deriv(self):   
        ans={}
        temp ={}
        for i in self.coefficients:
            temp[i]=self.coefficients[i]
        a=Polynomial()
        for i in temp:
            temp[i]=temp[i]*(i)
            if i!=0:
                ans[i-1]=temp[i]
        a.coefficients=ans
        return a 


def main():
    "write your test code here"
    z = Polynomial([1,2,3])
    h = Polynomial([1,2,3])
    
    

#    print([1,2,3]+Polynomial([1,2,3])) ????????????/
if __name__=="__main__":
	main()
