def main():
    
    #f = open("textfile.txt", "w+") # create and write
    #f = open("textfile.txt", "a") #appends


    #for i in range(10):
    #    f.write("Thia ia line " + str(i) + "\r\n")
    
    f = open("textfile.txt", "r") # reads file
    if f.mode == 'r':
        #contents = f.read()
        fl = f.readlines() #to add lines
        for x in fl:
            print(x)
        #print(contents)
    #f.close

if __name__ == "__main__":
    main()