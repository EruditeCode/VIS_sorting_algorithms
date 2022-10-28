from random import randint

class Sort:
	def __init__(self, array, choice):
		self.array = array
		self.choice = choice
		self.status = False
		self.frames = [array.copy()]
		self.item_log = []

	def run_sort(self):
		if self.choice == "bubble":
			self.bubble_sort_frames(self.array)
		elif self.choice == "quick":
			self.quick_sort_frames(self.array)
		elif self.choice == "heap":
			self.heap_sort_frames(self.array)
		self.status = True

	def bubble_sort_frames(self, array):
		sort = False
		while sort == False:
			sort = True
			for i in range(0, len(array) - 1):
				if array[i] > array[i + 1]:
					array[i], array[i + 1] = array[i + 1], array[i]
					self.frames.append(array.copy())
					sort = False

	def quick_sort_frames(self, array):
		self.quick_sort(array)
		for pivot in self.item_log:
			low, same, high = [], [], []
			for value in self.frames[-1]:
				if value < pivot:
					low.append(value)
				elif value == pivot:
					same.append(value)
				elif value > pivot:
					high.append(value)
			self.frames.append(low + same + high)

	def quick_sort(self, array):
		if len(array) <= 1:
			return array

		pivot_index = randint(0, len(array) - 1)
		pivot = array[pivot_index]
		self.item_log.append(pivot)

		lesser, same, greater = [], [], []
		for element in array:
			if element == pivot:
				same.append(element)
			elif element < pivot:
				lesser.append(element)
			elif element > pivot:
				greater.append(element)

		return self.quick_sort(lesser) + same + self.quick_sort(greater)

	def heap_sort_frames(self, array):
		sort_array = []
		heap = array.copy()
		while heap:
			# Create the max heap.
			for i in range((len(heap)//2)-1, -1, -1):
				self.tidy_heap(heap, i, sort_array)

			# Storing the max value in the sort array.
			sort_array.insert(0, heap[0])
			heap[0], heap[-1] = heap[-1], heap[0]
			heap.pop(-1)
		self.frames.append(heap + sort_array)

	def tidy_heap(self, heap, index, sort_array):
		LEFT = (2 * index) + 1
		RIGHT = (2 * index) + 2

		large = index
		if LEFT < len(heap) and heap[large] < heap[LEFT]:
			large = LEFT
		if RIGHT < len(heap) and heap[large] < heap[RIGHT]:
			large = RIGHT

		if large != index:
			heap[index], heap[large] = heap[large], heap[index]
			self.frames.append(heap + sort_array)
			self.tidy_heap(heap, large, sort_array)
		return heap
