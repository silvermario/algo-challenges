class Time(object):
	def whatTime(self, seconds):
		self.hours = seconds / 3600
		print self.hours
		self.minutes = (seconds - self.hours * 3600 ) / 60
		print self.minutes
		self.seconds = seconds - self.hours * 3600 - self.minutes * 60
		return "%s:%s:%s" % (self.hours, self.minutes, self.seconds)


print Time().whatTime(0)