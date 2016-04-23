
# Problem Statement
#
# You are writing firmware for an exercise machine. Each second, a routine in your firmware is called which decides whether it should display the percentage of the workout completed. The display does not have any ability to show decimal points, so the routine should only display a percentage if the second it is called results in a whole percentage of the total workout.
# Given a string time representing how long the workout lasts, in the format "hours:minutes:seconds", return the number of times a percentage will be displayed by the routine. The machine should never display 0% or 100%.
# Definition
#
# Class:
# ExerciseMachine
# Method:
# getPercentages
# Parameters:
# string
# Returns:
# integer
# Method signature:
# def getPercentages(self, time):

# Limits
#
# Time limit (s):
# 2.000
# Memory limit (MB):
# 64
# Constraints
# -
# time will be a string formatted as "HH:MM:SS", HH = hours, MM = minutes, SS = seconds.
# -
# The hours portion of time will be an integer with exactly two digits, with a value between 00 and 23, inclusive.
# -
# The minutes portion of time will be an integer with exactly two digits, with a value between 00 and 59, inclusive.
# -
# The seconds portion of time will be an integer with exactly two digits, with a value between 00 and 59, inclusive
# -
# time will not be "00:00:00".
# Examples
# 0)

#
# "00:30:00"
# Returns: 99
# The standard 30 minute workout. Each one percent increment can be displayed every 18 seconds.
# 1)

#
# "00:28:00"
# Returns: 19
# The 28 minute workout. The user completes 5 percent of the workout every 1 minute, 24 seconds.
# 2)

#
# "23:59:59"
# Returns: 0
# This is the longest workout possible, given the constraints. No percentages are ever displayed on the screen.
# 3)

#
# "00:14:10"
# Returns: 49

# 4)

#
# "00:19:16"
# Returns: 3

# This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.
from time import *

class ExerciseMachine(object):

	def time_in_seconds(self, time):
		time_struct = strptime(time, "%H:%M:%S")
		time_in_seconds = time_struct.tm_hour * 3600 + time_struct.tm_min * 60 + time_struct.tm_sec
		return time_in_seconds

	def getPercentages(self, time):
		time_in_seconds = self.time_in_seconds(time)
		self.counter = 0
		one_percent = time_in_seconds / 100.0
		for second in range(1, time_in_seconds):
			if (round((second * 1.0 ) % one_percent,2) == round(one_percent, 2)) or (second * 1.0 ) % one_percent == 0.0: #floating point numbers error hack
				self.counter += 1
		#print (one_percent)
		return self.counter

	def getPercentages2(self, time): # one of submitted python codes
		t = self.time_in_seconds(time)
		x = 0
		for percent in  range(1,100):
			if percent * t % 100 == 0:
				x += 1
		return x

	def getPercentages3(self, time): # after studying this match editorial
		from fractions import gcd
		t = self.time_in_seconds(time)
		return gcd(t, 100) - 1


print ExerciseMachine().getPercentages("00:30:00")
print ExerciseMachine().getPercentages("23:59:59")
print ExerciseMachine().getPercentages("00:28:00")
print ExerciseMachine().getPercentages("00:19:16")

print ExerciseMachine().getPercentages3("00:30:00")
print ExerciseMachine().getPercentages3("23:59:59")
print ExerciseMachine().getPercentages3("00:28:00")
print ExerciseMachine().getPercentages3("00:19:16")