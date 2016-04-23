# Definition
#
# Class:
# BinaryCode

# Method:
# decode

# Parameters:
# string

# Returns:
# tuple (string)

# Method signature:
# def decode(self, message):


class BinaryCode(object):

	#def decode_one(self, i, list, message):
	def is_valid(self, list):
		for value in list:
			if value in [0,1]:
				continue
			else:
				return 'NONE'
		if len(self.message) == 1 and int(self.message[0]) > 2:
			return 'NONE'
		if (len(list) >= 2):
			if (list[-1] + list[-2] != int(self.message[-1])):
				return 'NONE'
		return ''.join([str(item) for item in list])

	
	def decode(self, message):
		self.message = message
		self.p1 = [0]
		self.p2 = [1]
		self.q = [int(ch) for ch in (message)]

		for i, value in enumerate(message):
			if i == 0:
				pass
			elif i == 1:
				#self.p1[1] = self.q[0] - self.p1[0]
				self.p1.append(self.q[0] - self.p1[0])
				self.p2.append(self.q[0] - self.p2[0])
			else:
				#self.p1[i] = self.q[i - 1] - self.p1[i - 1] - self.p1[i - 2]
				self.p1.append(self.q[i - 1] - self.p1[i - 1] - self.p1[i - 2])
				self.p2.append(self.q[i - 1] - self.p2[i - 1] - self.p2[i - 2])

		#print self.p1, self.p2
		return self.is_valid(self.p1), self.is_valid(self.p2)

		
print BinaryCode().decode('123210122')
print BinaryCode().decode('123210120')
print BinaryCode().decode('3')
