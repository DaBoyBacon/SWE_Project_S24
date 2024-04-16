import unittest
#just to navigate back to test unit's directory
import sys
sys.path.append(sys.path[0]+"\\..\\..\\WorkingCode\\BackEnd\\PlayerSteamHandling")
#debug path
print(sys.path)
import AuthLimit

class TestSteamNameCheck(unittest.TestCase):
	def testAuthLimit(self):
		print("testing")
		
		c = AuthLimit.someTimer()
		c.start()
		c.inc()
		c.inc()
		c.inc()
		c.getinc()
		c.inc()
		c.inc()
		c.inc()
		c.getinc()
		
# throw's a fit if you don't put this
if __name__ == '__main__':
    unittest.main()