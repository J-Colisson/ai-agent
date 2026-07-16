
import unittest
from functions.write_file import write_file


print (write_file("calculator", "lorem.txt","wait, this isn't lorem ipsum"))
print (write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print (write_file("calculator", "/tmp/temp.txt", "this sould not be allowed"))


class Test_get_files_info(unittest.TestCase):
    def setUp(self) -> None:
        self.get_files_info = get_files_info()
