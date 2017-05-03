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
					power = 1000 - (100 * (abs(exitRow - j) + abs(exitCol - k)))
					
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
			if (fireCol + 1) <= (self.arrCol - 1):
				self.Matrix[fireRow][fireCol+1] -= 10
			if (fireCol - 1) >= 0:
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
			if (smokeCol + 1) <= (self.arrCol - 1):
				self.Matrix[smokeRow][smokeCol+1] -= 5
			if (smokeCol - 1) >= 0:
				self.Matrix[smokeRow][smokeCol-1] -= 5
				
	
				
	def escapePath(self, Row, Col):
		list = []
		
		print(Row, Col)
		
		if (self.Matrix[Row][Col] == 100):
			return "sueccess"
		
		if (Row - 1) >= 0 and (Col - 1) >= 0:
			list.append(self.Matrix[Row - 1][Col - 1])
		else:
			list.append(-100)
			
		if (Row - 1) >= 0:
			list.append(self.Matrix[Row - 1][Col])
		else:
			list.append(-100)
			
		if (Row - 1) >= 0 and (Col + 1) < self.arrCol:
			list.append(self.Matrix[Row - 1][Col + 1])
		else:
			list.append(-100)
			
		if (Col - 1) >= 0:
			list.append(self.Matrix[Row][Col - 1])
		else:
			list.append(-100)
			
		if (Col + 1) < self.arrCol:
			list.append(self.Matrix[Row][Col + 1])
		else:
			list.append(-100)
			
		if (Row + 1) < self.arrRow and (Col - 1) >= 0:
			list.append(self.Matrix[Row + 1][Col - 1])
		else:
			list.append(-100)
			
		if (Row + 1) < self.arrRow:
			list.append(self.Matrix[Row + 1][Col])
		else:
			list.append(-100)
			
		if (Row + 1) < self.arrRow and (Col + 1) < self.arrCol:
			list.append(self.Matrix[Row + 1][Col + 1])
		else:
			list.append(-100)
			
		maxPower = max(list)
		
		
		if (list.count(maxPower)) > 1:
			powerOfMax = 0
			movePosition = 0
			for i in range(0, 8):
				if (list[i] == max(list)):
					if (i == 0):
						list2 = []
						Row2 , Col2 = self.moveOne(Row, Col)

						if (Row2 - 1) >= 0 and (Col2 - 1) >= 0:
							list2.append(self.Matrix[Row2 - 1][Col2 - 1])
						else:
							list2.append(-100)
							
						if (Row2 - 1) >= 0:
							list2.append(self.Matrix[Row2 - 1][Col2])
						else:
							list2.append(-100)
							
						if (Row2 - 1) >= 0 and (Col2 + 1) < self.arrCol:
							list2.append(self.Matrix[Row2 - 1][Col2 + 1])
						else:
							list2.append(-100)
							
						if (Col2 - 1) >= 0:
							list2.append(self.Matrix[Row2][Col2 - 1])
						else:
							list2.append(-100)
							
						if (Col2 + 1) < self.arrCol:
							list2.append(self.Matrix[Row2][Col2 + 1])
						else:
							list2.append(-100)
							
						if (Row2 + 1) < self.arrRow and (Col2 - 1) >= 0:
							list2.append(self.Matrix[Row2 + 1][Col2 - 1])
						else:
							list2.append(-100)
							
						if (Row2 + 1) < self.arrRow:
							list2.append(self.Matrix[Row2 + 1][Col2])
						else:
							list2.append(-100)
							
						if (Row2 + 1) < self.arrRow and (Col2 + 1) < self.arrCol:
							list2.append(self.Matrix[Row2 + 1][Col2 + 1])
						else:
							list2.append(-100)
							
						if max(list2) > powerOfMax :
							powerOfMax = max(list2)
							movePosition = i
							
							
					if (i == 1):
						list2 = []
						Row2 , Col2 = self.moveTwo(Row, Col)

						if (Row2 - 1) >= 0 and (Col2 - 1) >= 0:
							list2.append(self.Matrix[Row2 - 1][Col2 - 1])
						else:
							list2.append(-100)
							
						if (Row2 - 1) >= 0:
							list2.append(self.Matrix[Row2 - 1][Col2])
						else:
							list2.append(-100)
							
						if (Row2 - 1) >= 0 and (Col2 + 1) < self.arrCol:
							list2.append(self.Matrix[Row2 - 1][Col2 + 1])
						else:
							list2.append(-100)
							
						if (Col2 - 1) >= 0:
							list2.append(self.Matrix[Row2][Col2 - 1])
						else:
							list2.append(-100)
							
						if (Col2 + 1) < self.arrCol:
							list2.append(self.Matrix[Row2][Col2 + 1])
						else:
							list2.append(-100)
							
						if (Row2 + 1) < self.arrRow and (Col2 - 1) >= 0:
							list2.append(self.Matrix[Row2 + 1][Col2 - 1])
						else:
							list2.append(-100)
							
						if (Row2 + 1) < self.arrRow:
							list2.append(self.Matrix[Row2 + 1][Col2])
						else:
							list2.append(-100)
							
						if (Row2 + 1) < self.arrRow and (Col2 + 1) < self.arrCol:
							list2.append(self.Matrix[Row2 + 1][Col2 + 1])
						else:
							list2.append(-100)
							
						if max(list2) > powerOfMax :
							powerOfMax = max(list2)
							movePosition = i
							
							
					if (i == 2):
						list2 = []
						Row2 , Col2 = self.moveThree(Row, Col)

						if (Row2 - 1) >= 0 and (Col2 - 1) >= 0:
							list2.append(self.Matrix[Row2 - 1][Col2 - 1])
						else:
							list2.append(-100)
							
						if (Row2 - 1) >= 0:
							list2.append(self.Matrix[Row2 - 1][Col2])
						else:
							list2.append(-100)
							
						if (Row2 - 1) >= 0 and (Col2 + 1) < self.arrCol:
							list2.append(self.Matrix[Row2 - 1][Col2 + 1])
						else:
							list2.append(-100)
							
						if (Col2 - 1) >= 0:
							list2.append(self.Matrix[Row2][Col2 - 1])
						else:
							list2.append(-100)
							
						if (Col2 + 1) < self.arrCol:
							list2.append(self.Matrix[Row2][Col2 + 1])
						else:
							list2.append(-100)
							
						if (Row2 + 1) < self.arrRow and (Col2 - 1) >= 0:
							list2.append(self.Matrix[Row2 + 1][Col2 - 1])
						else:
							list2.append(-100)
							
						if (Row2 + 1) < self.arrRow:
							list2.append(self.Matrix[Row2 + 1][Col2])
						else:
							list2.append(-100)
							
						if (Row2 + 1) < self.arrRow and (Col2 + 1) < self.arrCol:
							list2.append(self.Matrix[Row2 + 1][Col2 + 1])
						else:
							list2.append(-100)
							
						if max(list2) > powerOfMax :
							powerOfMax = max(list2)
							movePosition = i
							
							
					if (i == 3):
						list2 = []
						Row2 , Col2 = self.moveFour(Row, Col)

						if (Row2 - 1) >= 0 and (Col2 - 1) >= 0:
							list2.append(self.Matrix[Row2 - 1][Col2 - 1])
						else:
							list2.append(-100)
							
						if (Row2 - 1) >= 0:
							list2.append(self.Matrix[Row2 - 1][Col2])
						else:
							list2.append(-100)
							
						if (Row2 - 1) >= 0 and (Col2 + 1) < self.arrCol:
							list2.append(self.Matrix[Row2 - 1][Col2 + 1])
						else:
							list2.append(-100)
							
						if (Col2 - 1) >= 0:
							list2.append(self.Matrix[Row2][Col2 - 1])
						else:
							list2.append(-100)
							
						if (Col2 + 1) < self.arrCol:
							list2.append(self.Matrix[Row2][Col2 + 1])
						else:
							list2.append(-100)
							
						if (Row2 + 1) < self.arrRow and (Col2 - 1) >= 0:
							list2.append(self.Matrix[Row2 + 1][Col2 - 1])
						else:
							list2.append(-100)
							
						if (Row2 + 1) < self.arrRow:
							list2.append(self.Matrix[Row2 + 1][Col2])
						else:
							list2.append(-100)
							
						if (Row2 + 1) < self.arrRow and (Col2 + 1) < self.arrCol:
							list2.append(self.Matrix[Row2 + 1][Col2 + 1])
						else:
							list2.append(-100)
							
						if max(list2) > powerOfMax :
							powerOfMax = max(list2)
							movePosition = i
							
							
					if (i == 4):
						list2 = []
						Row2 , Col2 = self.moveFive(Row, Col)

						if (Row2 - 1) >= 0 and (Col2 - 1) >= 0:
							list2.append(self.Matrix[Row2 - 1][Col2 - 1])
						else:
							list2.append(-100)
							
						if (Row2 - 1) >= 0:
							list2.append(self.Matrix[Row2 - 1][Col2])
						else:
							list2.append(-100)
							
						if (Row2 - 1) >= 0 and (Col2 + 1) < self.arrCol:
							list2.append(self.Matrix[Row2 - 1][Col2 + 1])
						else:
							list2.append(-100)
							
						if (Col2 - 1) >= 0:
							list2.append(self.Matrix[Row2][Col2 - 1])
						else:
							list2.append(-100)
							
						if (Col2 + 1) < self.arrCol:
							list2.append(self.Matrix[Row2][Col2 + 1])
						else:
							list2.append(-100)
							
						if (Row2 + 1) < self.arrRow and (Col2 - 1) >= 0:
							list2.append(self.Matrix[Row2 + 1][Col2 - 1])
						else:
							list2.append(-100)
							
						if (Row2 + 1) < self.arrRow:
							list2.append(self.Matrix[Row2 + 1][Col2])
						else:
							list2.append(-100)
							
						if (Row2 + 1) < self.arrRow and (Col2 + 1) < self.arrCol:
							list2.append(self.Matrix[Row2 + 1][Col2 + 1])
						else:
							list2.append(-100)
							
						if max(list2) > powerOfMax :
							powerOfMax = max(list2)
							movePosition = i
							
							
					if (i == 5):
						list2 = []
						Row2 , Col2 = self.moveSix(Row, Col)

						if (Row2 - 1) >= 0 and (Col2 - 1) >= 0:
							list2.append(self.Matrix[Row2 - 1][Col2 - 1])
						else:
							list2.append(-100)
							
						if (Row2 - 1) >= 0:
							list2.append(self.Matrix[Row2 - 1][Col2])
						else:
							list2.append(-100)
							
						if (Row2 - 1) >= 0 and (Col2 + 1) < self.arrCol:
							list2.append(self.Matrix[Row2 - 1][Col2 + 1])
						else:
							list2.append(-100)
							
						if (Col2 - 1) >= 0:
							list2.append(self.Matrix[Row2][Col2 - 1])
						else:
							list2.append(-100)
							
						if (Col2 + 1) < self.arrCol:
							list2.append(self.Matrix[Row2][Col2 + 1])
						else:
							list2.append(-100)
							
						if (Row2 + 1) < self.arrRow and (Col2 - 1) >= 0:
							list2.append(self.Matrix[Row2 + 1][Col2 - 1])
						else:
							list2.append(-100)
							
						if (Row2 + 1) < self.arrRow:
							list2.append(self.Matrix[Row2 + 1][Col2])
						else:
							list2.append(-100)
							
						if (Row2 + 1) < self.arrRow and (Col2 + 1) < self.arrCol:
							list2.append(self.Matrix[Row2 + 1][Col2 + 1])
						else:
							list2.append(-100)
							
						if max(list2) > powerOfMax :
							powerOfMax = max(list2)
							movePosition = i
							
							
					if (i == 6):
						list2 = []
						Row2 , Col2 = self.moveSeven(Row, Col)

						if (Row2 - 1) >= 0 and (Col2 - 1) >= 0:
							list2.append(self.Matrix[Row2 - 1][Col2 - 1])
						else:
							list2.append(-100)
							
						if (Row2 - 1) >= 0:
							list2.append(self.Matrix[Row2 - 1][Col2])
						else:
							list2.append(-100)
							
						if (Row2 - 1) >= 0 and (Col2 + 1) < self.arrCol:
							list2.append(self.Matrix[Row2 - 1][Col2 + 1])
						else:
							list2.append(-100)
							
						if (Col2 - 1) >= 0:
							list2.append(self.Matrix[Row2][Col2 - 1])
						else:
							list2.append(-100)
							
						if (Col2 + 1) < self.arrCol:
							list2.append(self.Matrix[Row2][Col2 + 1])
						else:
							list2.append(-100)
							
						if (Row2 + 1) < self.arrRow and (Col2 - 1) >= 0:
							list2.append(self.Matrix[Row2 + 1][Col2 - 1])
						else:
							list2.append(-100)
							
						if (Row2 + 1) < self.arrRow:
							list2.append(self.Matrix[Row2 + 1][Col2])
						else:
							list2.append(-100)
							
						if (Row2 + 1) < self.arrRow and (Col2 + 1) < self.arrCol:
							list2.append(self.Matrix[Row2 + 1][Col2 + 1])
						else:
							list2.append(-100)
							
						if max(list2) > powerOfMax :
							powerOfMax = max(list2)
							movePosition = i
							
							
					if (i == 7):
						list2 = []
						Row2 , Col2 = self.moveEight(Row, Col)

						if (Row2 - 1) >= 0 and (Col2 - 1) >= 0:
							list2.append(self.Matrix[Row2 - 1][Col2 - 1])
						else:
							list2.append(-100)
							
						if (Row2 - 1) >= 0:
							list2.append(self.Matrix[Row2 - 1][Col2])
						else:
							list2.append(-100)
							
						if (Row2 - 1) >= 0 and (Col2 + 1) < self.arrCol:
							list2.append(self.Matrix[Row2 - 1][Col2 + 1])
						else:
							list2.append(-100)
							
						if (Col2 - 1) >= 0:
							list2.append(self.Matrix[Row2][Col2 - 1])
						else:
							list2.append(-100)
							
						if (Col2 + 1) < self.arrCol:
							list2.append(self.Matrix[Row2][Col2 + 1])
						else:
							list2.append(-100)
							
						if (Row2 + 1) < self.arrRow and (Col2 - 1) >= 0:
							list2.append(self.Matrix[Row2 + 1][Col2 - 1])
						else:
							list2.append(-100)
							
						if (Row2 + 1) < self.arrRow:
							list2.append(self.Matrix[Row2 + 1][Col2])
						else:
							list2.append(-100)
							
						if (Row2 + 1) < self.arrRow and (Col2 + 1) < self.arrCol:
							list2.append(self.Matrix[Row2 + 1][Col2 + 1])
						else:
							list2.append(-100)
							
						if max(list2) > powerOfMax :
							powerOfMax = max(list2)
							movePosition = i
							
							
			if (movePosition) == 0:
				return self.escapePath(Row - 1, Col - 1)
			
			elif (movePosition) == 1:
				return self.escapePath(Row - 1, Col)
				
			elif (movePosition) == 2:
				return self.escapePath(Row - 1, Col + 1)
				
			elif (movePosition) == 3:
				return self.escapePath(Row, Col - 1)
				
			elif (movePosition) == 4:
				return self.escapePath(Row, Col + 1)
				
			elif (movePosition) == 5:
				return self.escapePath(Row + 1, Col - 1)
				
			elif (movePosition) == 6:
				return self.escapePath(Row + 1, Col)
				
			elif (movePosition) == 7:
				return self.escapePath(Row + 1, Col + 1)
			else:
				return 0
			
			
		else:
			if (list.index(maxPower)) == 0:
				return self.escapePath(Row - 1, Col - 1)
			
			elif (list.index(maxPower)) == 1:
				return self.escapePath(Row - 1, Col)
				
			elif (list.index(maxPower)) == 2:
				return self.escapePath(Row - 1, Col + 1)
				
			elif (list.index(maxPower)) == 3:
				return self.escapePath(Row, Col - 1)
				
			elif (list.index(maxPower)) == 4:
				return self.escapePath(Row, Col + 1)
				
			elif (list.index(maxPower)) == 5:
				return self.escapePath(Row + 1, Col - 1)
				
			elif (list.index(maxPower)) == 6:
				return self.escapePath(Row + 1, Col)
				
			elif (list.index(maxPower)) == 7:
				return self.escapePath(Row + 1, Col + 1)
			else:
				return 0
		
	def moveOne(self, Row, Col):

		return Row - 1, Col - 1
	
	def moveTwo(self, Row, Col):

		return Row - 1, Col
	
	def moveThree(self, Row, Col):

		return Row - 1, Col + 1
	
	def moveFour(self, Row, Col):

		return Row, Col - 1
	
	def moveFive(self, Row, Col):

		return Row, Col + 1
	
	def moveSix(self, Row, Col):

		return Row + 1, Col - 1
	
	def moveSeven(self, Row, Col):

		return Row + 1, Col
	
	def moveEight(self, Row, Col):

		return Row + 1, Col + 1
	
	
			
a = FireEscape(4, 6)
a.exitMatrix(1)
a.fireMatrix(3)
#a.smokeMatrix(1)
a.escapePath(3, 4)
print(a.Matrix)
