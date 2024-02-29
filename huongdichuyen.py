
def SangTrái(bànCờ, chỉKiểmTra: bool) -> bool:
	if bànCờ.số0[0] - 1 < 0:
		return False
	if chỉKiểmTra == True:
		return True
	

	giáTrị = bànCờ.get(bànCờ.số0[0] - 1, bànCờ.số0[1])
	bànCờ.set(bànCờ.số0[0], bànCờ.số0[1], giáTrị)
	bànCờ.set(bànCờ.số0[0] - 1, bànCờ.số0[1], 0)
	bànCờ.số0 = (bànCờ.số0[0] - 1, bànCờ.số0[1])
	return True

# ------------------------------------------------------------------------------------------------------


def SangPhải(bànCờ, chỉKiểmTra: bool) -> bool:
	if bànCờ.số0[0] + 1 >= bànCờ.cộtTốiĐa:
		return False
	if chỉKiểmTra == True:
		return True
	

	giáTrị = bànCờ.get(bànCờ.số0[0] + 1, bànCờ.số0[1])
	bànCờ.set(bànCờ.số0[0], bànCờ.số0[1], giáTrị)
	bànCờ.set(bànCờ.số0[0] + 1, bànCờ.số0[1], 0)
	bànCờ.số0 = (bànCờ.số0[0] + 1, bànCờ.số0[1])
	return True


# ------------------------------------------------------------------------------------------------------


def LênTrên(bànCờ, chỉKiểmTra: bool) -> bool:
	if bànCờ.số0[1] - 1 < 0:
		return False
	if chỉKiểmTra == True:
		return True
	

	giáTrị = bànCờ.get(bànCờ.số0[0], bànCờ.số0[1] - 1)
	bànCờ.set(bànCờ.số0[0], bànCờ.số0[1], giáTrị)
	bànCờ.set(bànCờ.số0[0], bànCờ.số0[1] - 1, 0)
	bànCờ.số0 = (bànCờ.số0[0], bànCờ.số0[1] - 1)
	return True


# ------------------------------------------------------------------------------------------------------


def XuốngDưới(bànCờ, chỉKiểmTra: bool) -> bool:
	if bànCờ.số0[1] + 1 >= bànCờ.hàngTốiĐa:
		return False
	if chỉKiểmTra == True:
		return True
	

	giáTrị = bànCờ.get(bànCờ.số0[0], bànCờ.số0[1] + 1)
	bànCờ.set(bànCờ.số0[0], bànCờ.số0[1], giáTrị)
	bànCờ.set(bànCờ.số0[0], bànCờ.số0[1] + 1, 0)
	bànCờ.số0 = (bànCờ.số0[0], bànCờ.số0[1] + 1)
	return True