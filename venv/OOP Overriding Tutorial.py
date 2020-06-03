class parent:
    def sum(self,n1,n2):
        Result=n1+n2
        print("sum=",Result)
    def sub(self,n1,n2):
        Subresult=n1-n2
        print("sub=",Subresult)
class child(parent):
    def mul(self,n1,n2):
        mulresult=n1*n2
        print("mul=",mulresult)
    def sub(self,n1,n2):
        super().sub(n1,n2)
        #Subresult=n1-n2+5
        #print("sub=",Subresult)

def main():
    OPmul=child()
    OPmul.mul(2,4)
    OPmul.sub(6, 3)
    OPmul.sum(10, 12)

if __name__ == '__main__': main()