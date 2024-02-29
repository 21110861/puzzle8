from collections import deque
from hotrothuattoan import *

# lưu ý: nhờ thuật toán Đảo ma trận luôn cho đường đi nên ta không cần 
# xử lý trường hợp BFS không tìm thấy lời giải
def BFS(bànCờGốc,kếtQuả,bộĐếm):
	print("bfs")
	# -- Tạo một tập hợp để theo dõi các trạng thái đã xem
	đãĐệQuy = set()

	# -- Tạo hàng đợi với trạng thái ban đầu và danh sách bước
	queue = deque([(bànCờGốc.maTrận[:], [])])

	while queue and  kếtQuả.trạngThái == "chạy":
		# -- Lấy trạng thái và danh sách bước từ đầu hàng đợi
		maTrậnHiệnTại, kếtQuả.dữLiệu = queue.popleft()

		# -- Nếu trạng thái hiện tại đã được xếp đúng, in ra thông báo và trả về danh sách bước
		if XếpĐúng(maTrậnHiệnTại):
			bộĐếm.TínhBộNhớ("BFS       ",đãĐệQuy,len(kếtQuả.dữLiệu))
			kếtQuả.trạngThái = "xong"
			return
		# -- Thêm trạng thái hiện tại vào tập đã đệ quy
		if tuple(maTrậnHiệnTại) not in đãĐệQuy:
			đãĐệQuy.add(tuple(maTrậnHiệnTại))

			 # -- Thêm các trạng thái kế tiếp vào hàng đợi với danh sách bước mới
			for hướng in CácHướngKhảThi(maTrậnHiệnTại, bànCờGốc.cộtTốiĐa, bànCờGốc.hàngTốiĐa):
				queue.append((hướng, kếtQuả.dữLiệu + [hướng]))
