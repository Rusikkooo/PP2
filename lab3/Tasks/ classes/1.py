class My_class:
    def __init__(self):
        self.text = ""
    def getString(self):
        self.text = input("Please enter :")
    def  printString(self):
        print(self.text.upper())
a = My_class()
a.getString()
a.printString()