
import unittest
from utils import extractURL
 
class TestUtils(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_valid_url(self):
        url = "https://api.github.com/repos/mavam/stat-cookbook/commits/cba2407f4a86c0a040fe0473615f9987ab108b9c"

        self.assertEqual(extractURL(url), "https://api.github.com/repos/mavam/stat-cookbook")
 
if __name__ == '__main__':
    unittest.main()