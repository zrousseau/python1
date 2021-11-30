class Bird:
    species = 'bird'
    beak_length = 3.2


    def __init__(self,name):
        self.name = name


    def change_wingspan(self, wingspan):
        self.wingspan = wingspan

    def get_wingspan(self):
        print("{}".format(self.wingspan))


    def chirp(self):
        print("Caw Caw I'm a widdle birdie called {}".format(self.name))


    def __str__(self):
        return print("The {},".format(self.species), "{}".format(self.name), "has a wingspan of {}".format(self.wingspan), "cm")


a = Bird('')
b = Bird('')

name1 = input("What would you like to name the first bird?")
name2 = input("What would you like to name the second bird")

a.name = name1
b.name = name2

try:
    a.change_wingspan(float(input("What is the wingspan of the first bird?")))
    b.change_wingspan(float(input("What is the wingspan of the second bird?")))
except:
    print("The wingspan you entered is not an number, a wingspan of 30cm has been applied")
    wingspan1 = 30
    wingspan2 = 30



print(a.__str__())
print(b.__str__())
print(help(a))