from hotrothuattoan import *
import random
# lưu ý: nhờ thuật toán Đảo ma trận luôn cho đường đi nên ta không cần 
# xử lý trường hợp LDFS không tìm thấy lời giải

def LDFS(bànCờGốc,kếtQuả,bộĐếm):
	print("dfs")
	tốiĐa = 52
	while True:
		# -- Tạo ngăn xếp với trạng thái ban đầu và danh sách bước
		stack = [(bànCờGốc.maTrận[:], [],0)]
		# -- Tạo một tập hợp để theo dõi các trạng thái đã xem
		đãĐệQuy = set()
		while stack:
		
			if kếtQuả.trạngThái != "chạy":
				return
			# -- Lấy trạng thái và danh sách bước từ đầu ngăn xếp
			maTrậnHiệnTại, kếtQuả.dữLiệu, độSâu = stack.pop()
			# -- Nếu trạng thái hiện tại đã được xếp đúng, in ra thông báo và trả về danh sách bước
			if XếpĐúng(maTrậnHiệnTại):
				bộĐếm.TínhBộNhớ("LDFS      ",đãĐệQuy,len(kếtQuả.dữLiệu))
				kếtQuả.trạngThái = "xong"
				return

			# -- Thêm trạng thái hiện tại vào tập đã đệ quy
			if tuple(maTrậnHiệnTại) not in đãĐệQuy and độSâu < tốiĐa:
				đãĐệQuy.add(tuple(maTrậnHiệnTại))
				# -- Thêm các trạng thái kế tiếp vào ngăn xếp với danh sách bước mới
				hướngĐiĐược = CácHướngKhảThi(maTrậnHiệnTại, bànCờGốc.cộtTốiĐa, bànCờGốc.hàngTốiĐa)
				random.shuffle(hướngĐiĐược)

				for hướng in hướngĐiĐược:
					stack.append(( hướng, kếtQuả.dữLiệu + [hướng],độSâu+1))
		print("new deep")
		tốiĐa += 52