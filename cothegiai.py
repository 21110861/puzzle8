from matran import MaTrận

def CóThểGiảiĐược(bànCờ):
	return True
	# Count inversions in given puzzle
	invCount = getInvCount(bànCờ)
 
	# If grid is odd, return true if inversion
	# count is even.
	if (bànCờ.len & 1):
		return ~(invCount & 1)
 
	else:	# grid is even
		pos = bànCờ.hàngTốiĐa - bànCờ.số0[1]
		if (pos & 1):
			return ~(invCount & 1)
		else:
			return invCount & 1


def getInvCount(bànCờ):
	arr=bànCờ.maTrận
	inv_count = 0
	for i in range(bànCờ.len- 1):
		for j in range(i + 1,bànCờ.len):
			# count pairs(arr[i], arr[j]) such that 
			# i < j and arr[i] > arr[j]
			if (arr[j] and arr[i] and arr[i] > arr[j]):
				inv_count+=1
		 
	 
	return inv_count