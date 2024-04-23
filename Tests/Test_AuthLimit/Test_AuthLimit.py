import unittest
import time
#just to navigate back to test unit's directory
import sys
sys.path.append(sys.path[0]+"\\..\\..\\WorkingCode\\BackEnd\\PlayerSteamHandling")
#debug path
print(sys.path)
import AuthLimit

class TestSteamNameCheck(unittest.TestCase):
	def testAuthLimit(self):
		
		### This next part
		### Is testing creating
		### and incrementing

		print("b4 setting scheduler")
		t_var = AuthLimit.AuthTimer()

		print("something's happening")
		t_var.inc()
		t_var.inc()
		t_var.inc()
		
		self.assertEqual(t_var.getinc(), 3)

		print("sleep for 10s")

		time.sleep(10)

		t_var.inc()
		t_var.inc()
		t_var.inc()
		
		
		self.assertEqual(t_var.getinc(), 6)

		print("Sleep for 60s")
		time.sleep(60)
		
		self.assertEqual(t_var.getinc(), 0)
		
		print(t_var.getinc())

		print("Can end :thumbs_up:")
		#time.sleep(65)
		
# throw's a fit if you don't put this
if __name__ == '__main__':
    unittest.main()
