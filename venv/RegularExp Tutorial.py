import re

def main():
    readfile=open("regFile.txt","r")
    for line in readfile:
        if re.search("(F|M)a",line):
            print(line)
    readfile.close()


if __name__ == '__main__':main()