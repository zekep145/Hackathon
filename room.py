

class MeetingRoom:

	Name = "Shift"
	IsOccupied = 0
	IsBooked = 0
	BookerName = "Alex"
	PersonInRoom = ""
	WebExInfo = ""
	WebExPhone = "12072400694"


	def SetOccupiedState(self):
		if(self.IsOccupied == 0):
			self.IsOccupied = 1
			print("Meeting room \"{0}\" is now occupied".format(self.Name))
		else:
			self.IsOccupied = 0
			print("Meeting room \"{0}\" is now empty".format(self.Name)) 
