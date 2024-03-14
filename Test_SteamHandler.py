def Test_SteamHandler(steamUserName):

	#check steam username, make sure it's in bounds and constant through all the functions

	#API allows up to 32 and at least 2 characters
	if(steamUserName.size() > 32):
		#report name too large
	else if (steamUserName.size() < 2):
		#report name too small

	#run SteamUserName functions
	v1 = func1(steamUserName)
	v2 = func2(steamUserName)
	v3 = func3(steamUserName)
	v4 = func4(steamUserName)

	#Make sure SteamUserName isn't mutated
	if (v1.uName == v2.uName == v3.uName == v4.uName == steamUserName):
		#do nothing
	else: 
		#Report mutation

	#assuming all tests are working
