class Person:
    def __init__(self, name, age, born):
        self.name = name
        self.age = age
        self.born = born
    def greeting(self):
        print("My name is {0}, I am {1} years old, and I am from {2}".format(self.name,self.age,self.born))

def main():
    input_name = input("What's your name? ")
    input_age = input("How old are you? ")
    input_born = input("Where are you come from? ")
    p1 = Person(input_name, input_age, input_born)
    p1.greeting()

if __name__ == "__main__":
    main()