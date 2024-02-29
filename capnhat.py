import pygame  						# -- Import thư viện pygame để làm việc với đồ họa
from matran import MaTrận  			# -- Import MaTrận từ module matran
from dichuyen import DiChuyển  		# -- Import DiChuyển từ module dichuyen
from nhannut import NhấnNút  		# -- Import NhấnNút từ module nhannut
from hieuung import HiệuỨng

def CậpNhật(bànCờ, điềuKhiển, luồngSongSong,tácGiả,nútÂmThanh):

	luồngSongSong.CậpNhậtLuồngSongSong()
	# -- Hàm CậpNhật để điều khiển game và cập nhật trạng thái
	
	
	if TựDiChuyển(CậpNhật.FPS, bànCờ, luồngSongSong, điềuKhiển) == True:
		pygame.event.clear()
		
	for event in pygame.event.get():
		# -- Khi người dùng tắt cửa sổ game, thoát khỏi vòng lặp
		if event.type == pygame.QUIT:
			return True
			
		NhấnNút(bànCờ, điềuKhiển, luồngSongSong,nútÂmThanh,event.type == pygame.MOUSEBUTTONDOWN)
			
		if event.type == pygame.KEYDOWN:
			DiChuyển(bànCờ, event.key, điềuKhiển.checkbox[0].checked)
			# -- Khi phím 'o' được nhấn, tải ảnh mới
			if event.key == pygame.K_o:
				bànCờ.LấyẢnh()
				
				
	tácGiả.CậpNhật()
	HiệuỨng(CậpNhật.FPS)
	# -- Giới hạn frames per second (FPS) của game
	CậpNhật.FPS.tick(60) 
#----------------------------------------------------------------------------------------


# -- Khởi tạo đồng hồ đo thời gian cho FPS
CậpNhật.FPS = pygame.time.Clock()  
 







def TựDiChuyển(thờiGian, bànCờ, luồngSongSong, điềuKhiển):
	# -- Hàm TựDiChuyển để xử lý việc tự động di chuyển trong game
	TựDiChuyển.miligiây += thờiGian.get_time()
	if TựDiChuyển.miligiây >= 200:
		TựDiChuyển.miligiây = 0
			# -- Lấy giá trị mới từ đường đi
	if(len(luồngSongSong.dữLiệu) != 0 and luồngSongSong.trạngThái == "xong"):
		if(TựDiChuyển.miligiây == 0):
			trạngThái = luồngSongSong.dữLiệu.pop(0)
			bànCờ.cũ.insert(0,trạngThái[:])
			bànCờ.LấyGiáTrịMới(trạngThái) 
			điềuKhiển.bộĐếm[0].Tăng()
			bànCờ.print()
			print("  |\n  |\n  V\n---------")
		return True 
	
	return False
	
# -- Khởi tạo biến miligiây cho việc đếm thời gian
TựDiChuyển.miligiây = 0  
