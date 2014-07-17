# Merge Sort 
# Joe Johnston <jjohn@taskboy.com>

class MergeSort:
	def __init__(self):
		self.tmp = None
		pass
	
	def merge(self, list, pos1_first, pos1_last, pos2_first, pos2_last):
		idx = pos1_first
		save_first = idx
		
		while ((pos1_first <= pos1_last) and (pos2_first <= pos2_last)):
			if (list[pos1_first] < list[pos2_first]):
				self.tmp[ idx ] = list[ pos1_first ]
				pos1_first = pos1_first + 1
			elif (list[pos1_first] > list[pos2_first]):
				self.tmp[ idx ] = list[ pos2_first ]
				pos2_first = pos2_first + 1
			else:
				# for this test, ignore
				pass
			idx = idx + 1
			
		# Handle any remaining
		while (pos1_first <= pos1_last):
			self.tmp[ idx ] = list[ pos1_first ]
			pos1_first = pos1_first + 1
			idx = idx + 1
		
		while (pos2_first <= pos2_last):
			self.tmp[ idx ] = list[ pos2_first ]
			pos2_first = pos2_first + 1
			idx = idx + 1
		
		# Copy tmp array back to original list
		idx = save_first
		while (idx <= pos2_last):
			list[ idx ] = self.tmp[ idx ]
			idx = idx + 1
						
	def sort_list(self, list, first=0, last=None):
		if (self.tmp == None):
			self.tmp = list[:]
			
		if (last == None):
			last = len(list) - 1
		
		if first < last:
			mid = int((first + last) / 2)
			self.sort_list(list, first, mid)
			self.sort_list(list, mid + 1, last)
			self.merge(list, first, mid, mid + 1, last)
			
		return list
			