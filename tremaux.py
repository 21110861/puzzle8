from hotrothuattoan import *
from collections import defaultdict 
# Lưu ý: Nhờ thuật toán Đảo ma trận luôn cho đường đi, nên ta không cần 
# xử lý trường hợp HDFS không tìm thấy lời giải.
# Hàm thực hiện thuật toán DFS kết hợp với heuristics để giải MxN puzzle.
def Tremaux(bànCờGốc, kếtQuả, bộĐếm):
	print("hill")
	# Sao chép ma trận ban đầu để không làm thay đổi giá trị gốc.
	maTrậnHiệnTại = bànCờGốc.maTrận[:]
	# Tạo một từ điển để theo dõi các trạng thái đã đệ quy.
	đãĐệQuy = defaultdict(int)

	# Vòng lặp chính của thuật toán.
	while kếtQuả.trạngThái == "chạy":
		# Nếu ma trận hiện tại đã được sắp xếp đúng, kết thúc thuật toán.
		if XếpĐúng(maTrậnHiệnTại):
			bộĐếm.TínhBộNhớ("Tremaux ",đãĐệQuy,len(kếtQuả.dữLiệu))
			kếtQuả.trạngThái = "xong"
			return

		# Kiểm tra và cập nhật số lần xuất hiện của ma trận hiện tại trong đãĐệQuy.
		đãĐệQuy[tuple(maTrậnHiệnTại)] += 1
		# Khởi tạo biến cho ma trận tối ưu và giá trị h tối ưu.
		tốiƯuMaTrận, tốiƯuH = None, 999999

		# Duyệt qua các hướng khả thi từ ma trận hiện tại.
		for maTrậnKế in CácHướngKhảThi(maTrậnHiệnTại, bànCờGốc.cộtTốiĐa, bànCờGốc.hàngTốiĐa):
			h = TínhH(bànCờGốc.len, maTrậnKế)

			# Nếu ma trận đã nằm trong đãĐệQuy, cập nhật giá trị h theo số lần đã đệ quy.
			if tuple(maTrậnKế) in đãĐệQuy:
				h = đãĐệQuy[tuple(maTrậnKế)] * 2 + h

			# Nếu giá trị h mới tốt hơn giá trị h tối ưu hiện tại, cập nhật tối ưu.
			if(h < tốiƯuH):
				tốiƯuH, tốiƯuMaTrận = h, maTrậnKế

		# Thêm ma trận tối ưu vào đường đi.
		kếtQuả.dữLiệu += [tốiƯuMaTrận]

		# Cập nhật trạng thái hiện tại của ma trận.
		maTrậnHiệnTại = tốiƯuMaTrận
