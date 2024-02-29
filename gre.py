import heapq
from hotrothuattoan import *

# Lưu ý: Nhờ thuật toán Đảo ma trận luôn cho đường đi, nên ta không cần 
# xử lý trường hợp Greedy không tìm thấy lời giải.
def Greedy(bànCờGốc, kếtQuả, bộĐếm):
	print("greedy")

	# Danh sách hàng đợi ưu tiên để lưu trữ trạng thái và giá trị h tương ứng.
	heap = []

	# Tập hợp để theo dõi các trạng thái đã đệ quy.
	đãĐệQuy = set()

	# Tính giá trị h ban đầu cho ma trận ban đầu.
	h_đầu = TínhH(bànCờGốc.len, bànCờGốc.maTrận)

	# Đưa trạng thái ban đầu vào hàng đợi ưu tiên.
	heapq.heappush(heap, (h_đầu, bànCờGốc.maTrận[:], kếtQuả.dữLiệu))

	# Vòng lặp chính của thuật toán.
	while kếtQuả.trạngThái == "chạy":
		# Lấy trạng thái và giá trị h tối ưu từ hàng đợi ưu tiên.
		hĐangXét, maTrậnHiệnTại, kếtQuả.dữLiệu = heapq.heappop(heap)

		# Nếu giá trị h là 0, nghĩa là đã tìm thấy lời giải.
		if hĐangXét == 0:
			bộĐếm.TínhBộNhớ("Greedy   ",đãĐệQuy,len(kếtQuả.dữLiệu))
			kếtQuả.trạngThái = "xong"
			return

		# Kiểm tra xem trạng thái hiện tại đã được xét trước đó chưa.
		if tuple(maTrậnHiệnTại) in đãĐệQuy:
			continue
		đãĐệQuy.add(tuple(maTrậnHiệnTại))

		# Duyệt qua các hướng khả thi từ trạng thái hiện tại.
		for maTrậnKế in CácHướngKhảThi(maTrậnHiệnTại, bànCờGốc.cộtTốiĐa, bànCờGốc.hàngTốiĐa):
			h = TínhH(bànCờGốc.len, maTrậnKế)

			# Đưa trạng thái mới vào hàng đợi ưu tiên với giá trị h tương ứng.
			heapq.heappush(heap, (h, maTrậnKế, kếtQuả.dữLiệu + [maTrậnKế]))
