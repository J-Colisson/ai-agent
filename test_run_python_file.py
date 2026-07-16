
import unittest
from functions.run_python_file import run_python_file


print (run_python_file("calculator", "main.py"))
print (run_python_file("calculator", "main.py", ["3 + 5"]))
print (run_python_file("calculator", "tests.py"))
print (run_python_file("calculator", "../main.py"))
print (run_python_file("calculator", "nonexistent.py"))
print (run_python_file("calculator", "lorem.txt"))


class Test_get_files_info(unittest.TestCase):
    def setUp(self) -> None:
        self.get_files_info = get_files_info()
