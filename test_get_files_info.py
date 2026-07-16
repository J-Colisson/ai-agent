
import unittest
from functions.get_files_info import get_files_info


print (get_files_info("calculator", "."))
print (get_files_info("calculator", "pkg"))
print (get_files_info("calculator", "/bin"))
print (get_files_info("calculator", "../"))

class Test_get_files_info(unittest.TestCase):
    def setUp(self) -> None:
        self.get_files_info = get_files_info()
