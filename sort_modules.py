from random import randint


def quick_sort(array):
	if len(array) <= 1:
		return array

	pivot_index = randint(0, len(array) - 1)
	pivot = array[pivot_index]
	#ERROR WITH PIVOTS NOT DEFINED...STRUCTURE PROBLEM!
	pivots.append(pivot)

	lesser, same, greater = [], [], []

	for element in array:
		if element == pivot:
			same.append(element)
		elif element < pivot:
			lesser.append(element)
		elif element > pivot:
			greater.append(element)

	return quick_sort(lesser) + same + quick_sort(greater)

def tidy_heap(heap, index):
	LEFT = (2 * index) + 1
	RIGHT = (2 * index) + 2

	large = index
	if LEFT < len(heap) and heap[large] < heap[LEFT]:
		large = LEFT
	if RIGHT < len(heap) and heap[large] < heap[RIGHT]:
		large = RIGHT

	if large != index:
		heap[index], heap[large] = heap[large], heap[index]
		tidy_heap(heap, large)
	return heap

def heap_sort(array):
	batch = []
	sort_array = []
	heap = array.copy()
	while heap:
		# Create the max heap.
		for i in range((len(heap)//2)-1, -1, -1):
			tidy_heap(heap, i)

		# Storing the max value in the sort array.
		sort_array.insert(0, heap[0])
		heap[0], heap[-1] = heap[-1], heap[0]
		heap.pop(-1)
		batch.append(heap + sort_array)
	return sort_array, batch