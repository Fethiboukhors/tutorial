class car:
    def __init__(self,**Kwargs):
        self.Data=Kwargs
    def getowner(self):
        print("owner is me",self.Data["Name"])
        print("Model is",self.Data["Model"])

def main():
    mycar=car(Name="Fethi",Model="207")
    #mycar.Setowner("Fethi")
    mycar.getowner()
    bnoutcar=car(Name="Bnout",Model="301")
    #bnoutcar.Setowner("bnout")
    bnoutcar.getowner()


if __name__ == '__main__': main()