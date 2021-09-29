class employee:
	def __init__(self, name, emp, staff):
		self.name = name
		self.emp = emp
		self.staff = staff
	
	
	def calcPay(self):
		hour = float(input("Сколько часов отработал: "))
		return hour * self.staff
		
		
	def __str__(self):
		return f"Name: {self.name}\nСпециальность: {self.emp}\nОклад: {self.staff}\nЗарплата: {self.calcPay()}"


person = employee('Mikle', 'стрелок', 112.56)
print(person)
