class FireEscape:
	
	def __init__(self, arrRow, arrCol):
		self.arrRow = arrRow
		self.arrCol = arrCol
		self.Matrix = [[0 for x in range(arrCol)] for y in range(arrRow)]
		
	def exitMatrix(self, numberOfExit):
		
		for i in range(0, numberOfExit):
			exitRow = int(input("逃離出口(列):"))
			exitCol = int(input("逃離出口(行):"))
			for j in range(0, self.arrRow):
				for k in range(0, self.arrCol):
					power = 100 - (10 * (abs(exitRow - j) + abs(exitCol - k)))
					
					maxPower = max(self.Matrix[j][k], power)
					self.Matrix[j][k] = maxPower
	
	def fireMatrix(self, numberOfFire):
		for i in range(0, numberOfFire):
			fireRow = int(input("火災點(列):"))
			fireCol = int(input("火災點(行):"))
			
			self.Matrix[fireRow][fireCol] = 0
			if (fireRow + 1) <= (self.arrRow - 1):
				self.Matrix[fireRow+1][fireCol] -= 10
			if (fireRow - 1) >= 0:
				self.Matrix[fireRow-1][fireCol] -= 10
			if(fireCol + 1) <= (self.arrCol - 1):
				self.Matrix[fireRow][fireCol+1] -= 10
			if(fireCol - 1) >= 0:
				self.Matrix[fireRow][fireCol-1] -= 10
	
	def smokeMatrix(self, numberOfSmoke):
		for i in range(0, numberOfSmoke):
			smokeRow = int(input("煙點(列):"))
			smokeCol = int(input("煙點(行):"))
			
			self.Matrix[smokeRow][smokeCol] -= 5
			if (smokeRow + 1) <= (self.arrRow - 1):
				self.Matrix[smokeRow+1][smokeCol] -= 5
			if (smokeRow - 1) >= 0:
				self.Matrix[smokeRow-1][smokeCol] -= 5
			if(smokeCol + 1) <= (self.arrCol - 1):
				self.Matrix[smokeRow][smokeCol+1] -= 5
			if(smokeCol - 1) >= 0:
				self.Matrix[smokeRow][smokeCol-1] -= 5
			
a = FireEscape(3, 4)
a.exitMatrix(1)
a.fireMatrix(1)
a.smokeMatrix(1)
print(a.Matrix)
