"""
Daily GitHub Auto-Commit Script
"""

import os
import random
import datetime
import subprocess

REPO_PATH = r"C:\Users\Bhavesh Sahu\100-days-of-code"
YOUR_NAME  = "bhaveshksahu"
YOUR_EMAIL = "sbhaveshkumar133@gmail.com"

PYTHON_SNIPPETS = [
    ("fibonacci", '''# Fibonacci Series
def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result
print(fibonacci(10))
'''),
    ("list_comprehension", '''# List Comprehension
squares = [x**2 for x in range(1, 11)]
evens   = [x for x in range(20) if x % 2 == 0]
print("Squares:", squares)
print("Evens:", evens)
'''),
    ("decorator", '''# Decorators
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start  = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time()-start:.4f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))
print(slow_sum(1000000))
'''),
    ("class_basics", '''# OOP Basics
class Student:
    def __init__(self, name, branch, year):
        self.name   = name
        self.branch = branch
        self.year   = year
    def introduce(self):
        print(f"Hi! I am {self.name}, {self.year} year {self.branch} student.")

s = Student("Bhavesh", "AI/ML", 1)
s.introduce()
'''),
    ("recursion", '''# Recursion
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(factorial(6))
print(flatten([1, [2, [3, [4]], 5]]))
'''),
    ("binary_search", '''# Binary Search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

data = list(range(0, 100, 5))
print("Index of 45:", binary_search(data, 45))
'''),
    ("lambda_filter", '''# Lambda, Map, Filter
nums    = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
doubled = list(map(lambda x: x * 2, nums))
odds    = list(filter(lambda x: x % 2 != 0, nums))
print("Doubled:", doubled)
print("Odds:", odds)
'''),
    ("exception_handling", '''# Exception Handling
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero!"
    except TypeError as e:
        return f"Type error: {e}"

print(safe_divide(10, 2))
print(safe_divide(10, 0))
'''),
    ("generator", '''# Generators
def countdown(n):
    while n > 0:
        yield n
        n -= 1

def squares():
    n = 1
    while True:
        yield n * n
        n += 1

print(list(countdown(5)))
gen = squares()
print([next(gen) for _ in range(8)])
'''),
    ("sorting", '''# Sorting Algorithms
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

data = [64, 25, 12, 22, 11]
print("Bubble:", bubble_sort(data[:]))
print("Insertion:", insertion_sort(data[:]))
'''),
]


def run(cmd, cwd):
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, shell=True)
    if result.returncode != 0:
        print(f"[ERROR] {result.stderr.strip()}")
    return result.returncode == 0


def daily_commit():
    today       = datetime.date.today()
    name, code  = random.choice(PYTHON_SNIPPETS)

    folder   = os.path.join(REPO_PATH, "daily", str(today))
    os.makedirs(folder, exist_ok=True)

    filepath = os.path.join(folder, f"{name}.py")
    with open(filepath, "w") as f:
        f.write(f"# Date: {today}\n# Topic: {name}\n\n")
        f.write(code)

    print(f"[+] Created: {filepath}")

    run(f'git config user.name "{YOUR_NAME}"',       REPO_PATH)
    run(f'git config user.email "{YOUR_EMAIL}"',     REPO_PATH)
    run("git add .",                                 REPO_PATH)
    run(f'git commit -m "daily: {name} — {today}"', REPO_PATH)

    if run("git push", REPO_PATH):
        print(f"[✓] Pushed: {name} for {today}")
    else:
        print("[✗] Push failed.")


if __name__ == "__main__":
    daily_commit()