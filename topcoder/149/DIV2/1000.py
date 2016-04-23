
# Problem Statement
#
# Market differentiation in its simplest form is a system of charging different prices to different customers for the same product. To maximize the total sales revenue, we would like to charge each customer individually, charging the highest price that that customer would be willing to pay. Usually we have to divide the customers into a few groups, and charge the same price to everyone in a group (e.g. business class, economy class, etc.).
# We have a list of all the potential customers for our product and the most that each customer is willing to pay. We have decided to differentiate them into four or fewer (non-overlapping) groups. Everyone within each group will be offered the same price. Our goal is to choose the groups and prices optimally to maximize our total sales revenue.
# Create a class Pricing that contains a method maxSales that takes a tuple (integer) price containing the highest price that each potential customer is willing to pay, and returns the maximum sales revenue we can generate by differentiating our customers into four or fewer groups.
# Definition
#
# Class:
# Pricing
# Method:
# maxSales
# Parameters:
# tuple (integer)
# Returns:
# integer
# Method signature:
# def maxSales(self, price):

# Limits
#
# Time limit (s):
# 2.000
# Memory limit (MB):
# 64
# Constraints
# -
# price must contain between 1 and 50 elements inclusive
# -
# each element of price must be between 0 and 1000 inclusive
# Examples
# 0)

#
# {9,1,5,5,5,5,4,8,80}
# Returns: 120
# Charge 80 to the one customer willing to pay 80.
# Charge 8 to the 2 customers willing to pay 8 or 9.
# Charge 5 to the 4 customers willing to pay 5.
# Charge 4 to the one customer willing to pay 4.
# Total sales revenue = 1*80 + 2*8 + 4*5 + 1*4. (We can put the customer who is willing to pay 1 into any of these groups since he will not buy anything at these prices.)
# 1)

#
# {17,50,2}
# Returns: 69
# We use just three groups, each containing one customer. We charge each customer the most she is willing to pay. Total sales revenue = 1*17 + 1*50 + 1*2
# 2)

#
# {130,110,90,13,6,5,4,3,0}
# Returns: 346
# Charge each of the 4 customers willing to pay between 4 and 13 a price of 4, thereby getting a total of 16 from them. Then charge the most we can to each of the three customers who are willing to pay a lot. 4*4 + 90 + 110 + 130 = 346
# This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.

# solved after reading the editorial


class Pricing(object):
	def maxSales(self, price):
		price = sorted(price)
		ret = 0

		for i in range(len(price)):
			for j in range(len(price)):
				for k in range(len(price)):
					for m in range(len(price)):
						rev = 0
						for n in range(len(price)):
							if price[n] >= price[m]:
								rev += price[m]
							elif price[n] >= price[k]:
								rev += price[k]
							elif price[n] >= price[j]:
								rev += price[j]
							elif price[n] >= price[i]:
								rev += price[i]
						print ret, rev
						ret = max(ret, rev)

		print ret
		print price


# Pricing().maxSales((130,110,90,13,6,5,4,3,0))
# Pricing().maxSales((9,1,5,5,5,5,4,8,80))
Pricing().maxSales((1,2,3))