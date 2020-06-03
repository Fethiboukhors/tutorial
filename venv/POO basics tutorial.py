class car:
    def getowner(self):
        print("owner is me",self._Name)
    def Setowner(self,Name):
        self._Name=Name

def main():
    mycar=car()
    mycar.Setowner("Fethi")
    mycar.getowner()
    bnoutcar=car()
    bnoutcar.Setowner("bnout")
    bnoutcar.getowner()


if __name__ == '__main__': main()