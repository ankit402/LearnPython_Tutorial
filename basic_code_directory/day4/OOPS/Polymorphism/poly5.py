#  "Create a base class named `Person` with private attributes `name` and `age`.
#  Add methods to get and set these attributes.
#  Create a derived class named `Student` that adds an attribute `student_id`.
#  Create an object of the `Student` class and test the encapsulation.\n",

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

        @property
        def get_name(self):
            return self.__name

        @property
        def get_age(self):
            return self.__age

        @property
        def set_name(self, value):
            self.__name = value

        @property
        def set_age(self, value):
            self.__age = value

class Student(Person):
    def __init__(self,name , age , student_id):
        super().__init__(self, student_id)
        self.__student_id = student_id

    def get_student_id(self):
        return self.__student_id

c1= Student('ankit', 32 , "121")
c1.get_student_id()