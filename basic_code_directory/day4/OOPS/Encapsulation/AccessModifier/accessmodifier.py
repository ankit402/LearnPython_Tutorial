# 🟢 1. Public Members
# Can be accessed from anywhere (inside or outside the class).
#
# No underscore (_) or double underscore (__) is used.

# ✅ Example:

class Person:
    def __init__(self, name):
        self.name = name  # public variable

    def get_name(self):
        return self.name

# Access from outside
p = Person("Ankit")
print(p.name)         # ✅ allowed
print(p.get_name())   # ✅ allowed

# 🟡 2. Protected Members (_name)
# Indicated with a single underscore (_).
#
# Should be accessed only within the class or subclasses.
#
# Not strictly enforced, just a convention.

# ✅ Example:

class Person:
    def __init__(self, name):
        self._name = name  # protected variable

class Student(Person):
    def get_name(self):
        return self._name   # ✅ allowed in subclass

# Access from outside
s = Student("Ankit")
print(s.get_name())    # ✅ allowed
print(s._name)         # ⚠️ allowed, but not recommended

# 🔴 3. Private Members (__name)
# Starts with double underscore __.
# Cannot be accessed directly outside the class.
# Python does name mangling (e.g., _Person__name internally).

# ✅ Example with Getter/Setter:

class Person:
    def __init__(self, name):
        self.__name = name  # private variable

    def get_name(self):     # getter
        return self.__name

    def set_name(self, value):  # setter
        self.__name = value

# Access from outside
p = Person("Ankit")
print(p.get_name())     # ✅ allowed via getter

p.set_name("Rahul")     # ✅ allowed via setter
print(p.get_name())     # Rahul

# # print(p.__name)       ❌ Error: 'Person' object has no attribute '__name'
# 📌 Summary Table
# Access Level	Syntax	Access Location	Enforced?	Example Name
# Public	name	Everywhere	No	self.name
# Protected	_name	Class + Subclass only	No	self._name
# Private	__name	Class only (via name mangling)	Yes*	self.__name