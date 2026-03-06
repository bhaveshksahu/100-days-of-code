# Date: 2026-03-07
# Topic: class_basics

# OOP Basics
class Student:
    def __init__(self, name, branch, year):
        self.name   = name
        self.branch = branch
        self.year   = year
    def introduce(self):
        print(f"Hi! I am {self.name}, {self.year} year {self.branch} student.")

s = Student("Bhavesh", "AI/ML", 1)
s.introduce()
