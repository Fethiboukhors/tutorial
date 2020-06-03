class car:
    def __init__(self,Name):
        self._Name=Name
    def getowner(self):
        print("owner is me",self._Name)

def main():
    mycar=car("Fethi")
    #mycar.Setowner("Fethi")
    mycar.getowner()
    bnoutcar=car("Bnout")
    #bnoutcar.Setowner("bnout")
    bnoutcar.getowner()


if __name__ == '__main__': main()