class myClass():
    def method1(self):
        print("myClass method1")

    def method2(self, someString):
        print("myClass method2 " + str(someString))

#inherets from myClass
class anotherclass(myClass):
    def method1(self):
        myClass.method1(self) #Call inherated function *output will display*
        print("anotherClass method1")

    def method2(self, someString):
        print("anotherClass method2 ") #argument is not being used

def main():
    c=myClass() #makes an instance of class
    c.method1()
    c.method2("This is a string")

    c2=anotherclass()
    c2.method1()
    c2.method2("This is a string")

if __name__ == "__main__":
    main()        