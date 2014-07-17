from MergeSort import MergeSort

list = data = [ 100, 300, 50, 200, 150, 25, 10 ];

print("Original list: " + ",".join(map(str, list)) + "\n")

M = MergeSort()

sorted_list = M.sort_list(list)

print("Sorted list: " + ",".join(map(str, sorted_list)) + "\n")

