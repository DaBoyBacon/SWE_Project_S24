import unittest
import time
#just to navigate back to test unit's directory
import sys
sys.path.append(sys.path[0]+"\\..\\..\\WorkingCode\\BackEnd\\PlayerSteamHandling")
#debug path
print(sys.path)
import AuthLimit

class TestAuthLimit(unittest.TestCase):
	def testAuthLimit(self):
		
		### This next part
		### Is testing creating
		### and incrementing

		#print("b4 setting scheduler") # debug
		self.t_var = AuthLimit.AuthTimer()
		
		for num in range(1,self.t_var.maxIncrVal+1):
			self.assertTrue(self.t_var.canInc())
			self.assertEqual(self.t_var.getInc(),num)
		#incr should equal its max val
		self.assertEqual(self.t_var.getInc(), self.t_var.maxIncrVal)
		self.assertFalse(self.t_var.canInc())

		print(f"incr to max: {self.t_var.getInc()}")
		print(f"sleep for {self.t_var.interval/6}s (some time b4 reset)") #terminal clarification

		time.sleep(self.t_var.interval/6)
		
		#still full
		self.assertEqual(self.t_var.getInc(), self.t_var.maxIncrVal)
		self.assertFalse(self.t_var.canInc())
		
		print(f"Still max: {self.t_var.getInc()}")

		print(f"Sleep for {self.t_var.interval}s (till reset)") #wait for the timer to reset (60s)
		
		time.sleep(self.t_var.interval)
		
		self.assertEqual(self.t_var.getInc(),0)
		
		print(f"Now 0: {self.t_var.getInc()}", )
		print("Can end :thumbs_up:")
		#time.sleep(65)

		

# throw's a fit if you don't put this
if __name__ == '__main__':
    unittest.main()
