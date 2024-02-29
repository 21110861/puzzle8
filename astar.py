from hotrothuattoan import *
import heapq

# lưu ý: nhờ thuật toán Đảo ma trận luôn cho đường đi nên ta không cần 
# xử lý trường hợp A* không tìm thấy lời giải
def AStar(bànCờGốc, kếtQuả, bộĐếm):
	print("a*")
	heap = []  # danh sách hàng đợi ưu tiên
	đãĐệQuy = set()  # Tập hợp lưu trữ các trạng thái đã duyệt qua

	levelstart = 0
	fvaluedau = TínhF(bànCờGốc.len, bànCờGốc.maTrận, 0)
	heapq.heappush(heap, (fvaluedau, levelstart, bànCờGốc.maTrận[:], kếtQuả.dữLiệu))

	# Trong khi trạng thái của kết quả là "chạy"
	while kếtQuả.trạngThái == "chạy":
		fhientai, levelhientai, matranhientai, kếtQuả.dữLiệu = heapq.heappop(heap)

		# Nếu bàn cờ hiện tại đã được sắp xếp đúng
		if XếpĐúng(matranhientai):
			bộĐếm.TínhBộNhớ("AStar      ",đãĐệQuy,len(kếtQuả.dữLiệu))
			kếtQuả.trạngThái = "xong"
			return

		# Nếu trạng thái hiện tại đã được duyệt qua, bỏ qua
		if tuple(matranhientai) in đãĐệQuy:
			continue
		đãĐệQuy.add(tuple(matranhientai))

		# Duyệt qua các trạng thái kế tiếp có thể đi được từ trạng thái hiện tại
		for matranTiep in CácHướngKhảThi(matranhientai, bànCờGốc.cộtTốiĐa, bànCờGốc.hàngTốiĐa):
			levelTiep = levelhientai + 1
			fTiep = TínhF(bànCờGốc.len, matranTiep, levelTiep)
			heapq.heappush(heap, (fTiep, levelTiep, matranTiep, kếtQuả.dữLiệu + [matranTiep]))