

# Python program to verify IP without using RegEx

# explicit function to verify IP
def isValidIP(s):

	# check number of periods
	if s.count('.') != 3:
		return 'Invalid Ip address'

	l = list(map(str, s.split('.')))

	# check range of each number between periods
	for ele in l:
		# if int(ele) < 0 or int(ele) > 255 or (i[0]=='0' and len(i)!=1):
		print(str(ele[0]) + " " + str(len(ele)))
		if int(ele) < 0 or int(ele) > 255 or (ele[0] == '0' and len(ele) != 1):
			return 'Invalid Ip address'

	return 'Valid Ip address'


# Driver Code
print(isValidIP('666.1.2.2'))

print(isValidIP('222.01.2.2'))
print(isValidIP('222.1.00.2'))