class Opertaion:
    def sum(self,n1,n2):
        Result=n1+n2
        print("sum=",Result)
    def sub(self,n1,n2):
        Subresult=n1-n2
        print("sub=",Subresult)
class Operationwithmul(Opertaion):
    def mul(self,n1,n2):
        mulresult=n1*n2
        print("mul=",mulresult)

def main():
    OPmul=Operationwithmul()
    OPmul.mul(2,4)
    OPmul.sub(6, 3)
    OPmul.sum(10, 12)

if __name__ == '__main__': main()