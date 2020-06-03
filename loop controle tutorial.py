def main():
    word="python"
    for letter in word: #loop control
        if(letter=='t'):
            continue #this means if you find the letter 't' just continue without printing it
        elif(letter=='o'):
            break #break means if you find this letter finish the loop
        elif(letter=='y'):
            pass #pass is used as don't do anything if you find this just continue
        print(letter)



if __name__ == '__main__':main()