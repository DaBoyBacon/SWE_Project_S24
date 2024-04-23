import unittest
<<<<<<< HEAD
import time
=======
>>>>>>> fa9bebe213e8349a7337ac6a4c4dd263b62b5854
#just to navigate back to test unit's directory
import sys
sys.path.append(sys.path[0]+"\\..\\..\\WorkingCode\\BackEnd\\PlayerSteamHandling")
#debug path
print(sys.path)
import AuthLimit

class TestSteamNameCheck(unittest.TestCase):
	def testAuthLimit(self):
		print("testing")
		
<<<<<<< HEAD
		c = AuthLimit.APILimiter()
		c.incCt()
		c.incCt()
		c.incCt()
		self.assertEqual(c.getinc(), 3)
		c.incCt()
		c.incCt()
		c.incCt()
		self.assertEqual(c.getinc(), 6)
		#time.sleep(65)
		self.assertEqual(c.getinc(), 0)
=======
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
>>>>>>> fa9bebe213e8349a7337ac6a4c4dd263b62b5854
		
# throw's a fit if you don't put this
if __name__ == '__main__':
    unittest.main()