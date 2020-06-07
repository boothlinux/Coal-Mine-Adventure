
class Person:

	def __init__(self, name, age, favourite_foods):
		self.name = name
		self.age = age
		self.favourite_foods = favourite_foods
	
	def birth_year(self):
		return 2020 - self.age

people = [Person("Ed", 24, ["hotdogs", "jawbreakers"])
	, Person("Edd", 29, ["broccoli"])
	, Person("Eddy", 27, ["cocoa puffs", "soap"])]

age_sum = 0
year_sum = 0
for person in people:
	age_sum = age_sum + person.age
	year_sum = year_sum + person.birth_year()
	
print("The average age is: " + str(int(age_sum / len(people))))
print("The average birth year is: " + str(int(year_sum / len(people))))
