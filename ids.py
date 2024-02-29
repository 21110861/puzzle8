from hotrothuattoan import *

# Lưu ý: Nhờ thuật toán Đảo ma trận luôn cho đường đi, nên ta không cần 
# xử lý trường hợp IDS không tìm thấy lời giải.
def IDS(bànCờGốc,kếtQuả,bộĐếm):
	print("ids")
	giớiHạn = 10
	nextStack = [(0,bànCờGốc.maTrận[:], [])]
	# -- Tạo một tập hợp để theo dõi các trạng thái đã xem
	đãĐệQuy = set()

	while True:
		# -- Tạo ngăn xếp với trạng thái ban đầu và danh sách bước
		stack = nextStack[:]
		nextStack.clear()
		while stack and kếtQuả.trạngThái == "chạy":
			# -- Lấy trạng thái và danh sách bước từ đầu ngăn xếp
			độSâu,maTrậnHiệnTại, kếtQuả.dữLiệu = stack.pop()
			# -- Nếu trạng thái hiện tại đã được xếp đúng, in ra thông báo và trả về danh sách bước
			if XếpĐúng(maTrậnHiệnTại):
				bộĐếm.TínhBộNhớ("IDS        ",đãĐệQuy,len(kếtQuả.dữLiệu))
				kếtQuả.trạngThái = "xong"
				return

			# -- Thêm trạng thái hiện tại vào tập đã đệ quy
			if tuple(maTrậnHiệnTại) not in đãĐệQuy:
				đãĐệQuy.add(tuple(maTrậnHiệnTại))
				# -- Thêm các trạng thái kế tiếp vào ngăn xếp với danh sách bước mới
				for hướng in CácHướngKhảThi(maTrậnHiệnTại, bànCờGốc.cộtTốiĐa, bànCờGốc.hàngTốiĐa):
					if(độSâu + 1 < giớiHạn):
						stack.append((độSâu+1, hướng, kếtQuả.dữLiệu + [hướng]))
					else:
						nextStack.append((độSâu+1, hướng, kếtQuả.dữLiệu + [hướng]))
		giớiHạn = giớiHạn + 10