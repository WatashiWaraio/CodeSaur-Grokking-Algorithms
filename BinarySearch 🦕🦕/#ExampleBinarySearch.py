#ExampleBinarySearch

"""Suposse you have a sorted list of  names, and you're searching through it using binary search.
What's the maximum number of steps it would take?"""


def binary_search(names,Search):
	low = 0
	high = len(names) - 1 

	while low <= high:
		mid = (low + high) // 2
		mid_name = names[mid]

		if mid_name == Search:
			return mid 
		elif mid_name > Search:
			high = mid - 1
		else:
			low = mid + 1
	return None
names = ["Adam", "Alex", "Alice", "Anna", "Ben", "Bill", "Brian", "Carla", "Chris", "Daniel",
         "David", "Emily", "Emma", "Eric", "Ethan", "Grace", "Hannah", "Jack", "James", "John",
         "Kate", "Laura", "Lily", "Lucas", "Mark", "Mary", "Matthew", "Michael", "Natalie",
         "Nathan", "Olivia", "Owen", "Paul", "Peter", "Rachel", "Rebecca", "Richard", "Robert",
         "Sarah", "Sophia", "Steven", "Thomas", "William", "Zoe"]

print(binary_search(names, "Alex")) 
print(binary_search(names, "Sophia"))



