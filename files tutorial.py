def main():
    out=open("test.txt","n") #a means audit while n means new
    out.write("\nFethi Boukhors")
    out.write("\nGDG")
    out.close()
    readfile=open("test.txt","r")
    for line in readfile:
        print(line)
    readfile.close()


if __name__ == '__main__':main()