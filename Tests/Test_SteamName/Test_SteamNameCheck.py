#just to navigate back to test unit's directory
import sys
sys.path.append(sys.path[0]+"\\..\\..")

#debug path
#print(sys.path)

from SteamNameCheck import SteamNameCheck
import unittest


#should run SteamNameCheck() with a good few test cases, designed to test that the inputted steam name is formatted to the API specs.
class TestSteamNameCheck(unittest.TestCase):
	def testSteamNameCheck(self):
		#check steam username, make sure it's in bounds of API needs

		# These should fail the name check
		testCasesFail = (
			"a",
			"z",
			"0",
			"I",
			"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",
			"this should be false because there are too many characters :)",
			"this will be the last \"I want to fail\" test that I'll do")
		
		# These should pass the name check
		testCasesPass = (
			"alex",
			"zoned0utG4mer",
			"UrMom'sUN",
			"SomethingInTheMiddle")
		
		# Go through Fail cases, make sure they fail
		for case in testCasesFail:
			# checks that UN check calls False
			self.assertEqual(SteamNameCheck(case), False)
			
		# Go through Pass cases, make sure they pass
		for case in testCasesPass:
			# check that UN check calls True
			self.assertEqual(SteamNameCheck(case), True)

# throw's a fit if you don't put this
if __name__ == '__main__':
    unittest.main()
