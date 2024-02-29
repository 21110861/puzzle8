from queue import PriorityQueue
from hotrothuattoan import *

# Lưu ý: Nhờ thuật toán Đảo ma trận luôn cho đường đi, nên ta không cần 
# xử lý trường hợp UCS không tìm thấy lời giải.
def UCS(bànCờGốc, kếtQuả, bộĐếm):
	print("ucs")

	# Tập hợp để theo dõi các trạng thái đã đệ quy.
	đãĐệQuy = set()

	# Hàng đợi ưu tiên để lưu trữ chi phí và danh sách các ma trận tương ứng.
	pq = PriorityQueue()

	# Đưa trạng thái ban đầu vào hàng đợi ưu tiên với chi phí là 0.
	pq.put((0, bànCờGốc.maTrận[:],[]))

	# Vòng lặp chính của thuật toán.
	while not pq.empty() and kếtQuả.trạngThái == "chạy":
		# Lấy chi phí và danh sách ma trận từ hàng đợi ưu tiên.
		chiPhí, maTrậnHiệnTại,kếtQuả.dữLiệu = pq.get()
		# Nếu ma trận hiện tại đã sắp xếp đúng, kết thúc thuật toán.
		if XếpĐúng(maTrậnHiệnTại):
			# Loại bỏ ma trận ban đầu khỏi danh sách để trả về đường đi chính xác.
			kếtQuả.trạngThái = "xong"
			bộĐếm.TínhBộNhớ("UCS       ",đãĐệQuy,len(kếtQuả.dữLiệu))
			return
		# Kiểm tra xem trạng thái hiện tại đã được xét trước đó chưa.
		if tuple(maTrậnHiệnTại) in đãĐệQuy:
			continue
		đãĐệQuy.add(tuple(maTrậnHiệnTại))

		# Duyệt qua các hướng khả thi từ trạng thái hiện tại.
		for hướng in CácHướngKhảThi(maTrậnHiệnTại, bànCờGốc.cộtTốiĐa, bànCờGốc.hàngTốiĐa):
			# Đưa trạng thái mới vào hàng đợi ưu tiên với chi phí tăng lên 1.
			pq.put((chiPhí + 1, hướng,kếtQuả.dữLiệu + [hướng]))
