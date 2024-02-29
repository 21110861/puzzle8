def CácHướngKhảThi(maTrậnHiệnTại, cộtTốiĐa, hàngTốiĐa):
	# -- Danh sách lưu trữ các trạng thái mới khả thi
	cácKhảNăng = [] 
	# -- Danh sách lưu trữ các hướng di chuyển cho số 0
	hướng = []  
	số0 = maTrậnHiệnTại.index(0)
	x, y = số0 % cộtTốiĐa, số0 // cộtTốiĐa

	# -- Kiểm tra các hướng di chuyển có hợp lệ và thêm vào danh sách hướng
	if y > 0:
		hướng.append(-cộtTốiĐa)
	if y < hàngTốiĐa - 1:
		hướng.append(cộtTốiĐa)
	if x > 0:
		hướng.append(-1)
	if x < cộtTốiĐa - 1:
		hướng.append(1)

	# -- Tạo các trạng thái mới bằng cách di chuyển số 0 và thêm vào danh sách các khả năng
	for move in hướng:
		new_index = số0 + move
		if 0 <= new_index < cộtTốiĐa * hàngTốiĐa:
			maTrận = maTrậnHiệnTại[:]
			maTrận[số0], maTrận[new_index] = maTrận[new_index], maTrận[số0]
			cácKhảNăng.append(maTrận)

	return cácKhảNăng

def XếpĐúng(maTrận) -> bool:
	for i in range(len(maTrận)):
		if i != maTrận[i]:
			return False
	return True

def TínhF(tổngSốÔ , maTrận , level):
	return TínhH(tổngSốÔ, maTrận) + level

def TínhH(tổngSốÔ, maTrận):

	h_value = 0
	for i in range(tổngSốÔ):
		if(maTrận[i] != 0):
			if maTrận[i] != i:
				h_value += 1
	return h_value

def TínhKĩH(tổngSốÔ,maTrận):
	h_value = 0
	for i in range(tổngSốÔ):
		if maTrận[i] != i:
			h_value += 100
	for i in range(maTrận.index(0)):
		h_value += maTrận[i]
	return h_value