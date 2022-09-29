import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in range(len(sentence) - 1):
		if i == 'a':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items = self.items.append(item)

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		max_stock = 0
		max_index = 0
		for i in (len(self.items) - 1):
			max_stock = self.items[i].stock
			if max_stock < self.items[i+1].stock:
				max_stock = self.items[i+1].stock
				max_index = i+1
		return self.items[max_index]
		
		


	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		max_price = 0
		max_index = 0
		for i in (len(self.items) - 1):
			max_stock = self.items[i].price
			if max_stock < self.items[i+1].price:
				max_stock = self.items[i+1].price
				max_index = i+1
		return self.items[max_index]



# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

		self.warehouse1 = Warehouse([self.item1, self.item2, self.item3])
		self.warehouse2 = Warehouse([self.item1, self.item2, self.item3, self.item4])


	## Check to see whether count_a works
	def test_count_a(self):
		self.assertEqual(self.item1.count_a(self.item1.name), 0, "count_a Beer")
		self.assertEqual(self.item4.count_a(self.item4.name), 2, "Count a : fanta")



	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):

		self.assertEqual(self.warehouse1.add_item(self.item4)), self.warehouse2, "add_item warehouse1 --> 2")


	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):

		self.assertEqual(self.warehouse1.get_max_stock(),self.item3 )


	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		self.assertEqual(self.warehouse2.get_max_price(),self.item1)
	
		

def main():
	unittest.main()

if __name__ == "__main__":
	main()