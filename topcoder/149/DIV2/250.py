
# Problem Statement
#
# In documents, it is frequently necessary to write monetary amounts in a standard format. We have decided to format amounts as follows:
# the amount must start with '$'
# the amount should have a leading '0' if and only if it is less then 1 dollar.
# the amount must end with a decimal point and exactly 2 following digits.
# the digits to the left of the decimal point must be separated into groups of three by commas (a group of one or two digits may appear on the left).
# Create a class FormatAmt that contains a method amount that takes two int's, dollars and cents, as inputs and returns the properly formatted String.
# Definition
#
# Definition
#
# Class:
# FormatAmt
# Method:
# amount
# Parameters:
# integer, integer
# Returns:
# string
# Method signature:
# def amount(self, dollars, cents):
#
# Time limit (s):
# 2.000
# Memory limit (MB):
# 64
# Notes
# -
# One dollar is equal to 100 cents.
# Constraints
# -
# dollars will be between 0 and 2,000,000,000 inclusive
# -
# cents will be between 0 and 99 inclusive
# Examples
# 0)

#
# 123456
# 0
# Returns: "$123,456.00"
# Note that there is no space between the $ and the first digit.
# 1)

#
# 49734321
# 9
# Returns: "$49,734,321.09"

# 2)

#
# 0
# 99
# Returns: "$0.99"
# Note the leading 0.
# 3)

#
# 249
# 30
# Returns: "$249.30"

# 4)

#
# 1000
# 1
# Returns: "$1,000.01"

# This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.

# 135 points


class FormatAmt(object):
	# def amount_2(self, dollars, cents):
	# 	result = ['$']
	# 	dollars_temp = []
	# 	for i,digit in enumerate(str(dollars)[::-1]):
	# 		if i > 0 and i % 3 == 0:
	# 			dollars_temp.append(",")
	# 		dollars_temp.append(digit)

	# 	result += dollars_temp[::-1] + ["."]

	# 	if len(str(cents)) == 1:
	# 		result.append("0")
	# 	result.append(str(cents))
		
	# 	return "".join(result)

	def amount(self, dollars, cents):	# slightly more efficient ;)
		return '${:,}{:.02}'.format(dollars, cents * 0.01)


print FormatAmt().amount(1000,1)

