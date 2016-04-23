
# Problem Statement
#
# Create a class DivisorDigits containing a method howMany which takes an integer number and returns how many digits in number divide evenly into number itself.
# Definition
#
# Class:
# DivisorDigits
# Method:
# howMany
# Parameters:
# integer
# Returns:
# integer
# Method signature:
# def howMany(self, number):

# Limits
#
# Time limit (s):
# 2.000
# Memory limit (MB):
# 64
# Notes
# -
# No number is divisible by 0.
# Constraints
# -
# number will be between 10000 and 999999999.
# Examples
# 0)

#
# 12345
# Returns: 3
# 12345 is divisible by 1, 3, and 5.
# 1)

#
# 661232
# Returns: 3
# 661232 is divisible by 1 and 2.
# 2)

#
# 52527
# Returns: 0
# 52527 is not divisible by 5, 2, or 7.
# 3)

#
# 730000000
# Returns: 0
# Nothing is divisible by 0. In this case, the number is also not divisible by 7 or 3.
# This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.

# 223 points without looking at editorials

class DivisorDigits(object):
	def howMany(self, number):
		count = 0
		for digit in str(number):
			if int(digit) != 0 and number % int(digit) == 0:
				count += 1
		return count


print DivisorDigits().howMany(730000000)