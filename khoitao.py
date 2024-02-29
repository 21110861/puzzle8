import pygame
from matran import MaTrận
from nut import Nút
from checkbox import CheckBox
from bodem import BộĐếm
from number import Number
from hieuung import HiệuỨng
from dieukhien import ĐiềuKhiển
from banner import Banner
from nhac import Nhạc
def KhởiTạo(tiêuĐề):

	pygame.init()
	pygame.mixer.init()

	# Lấy kích thước của toàn màn hình
	ngangPM = 1310
	dọcPM = 720
	scr = pygame.display.set_mode( (ngangPM, dọcPM) )

	pygame.display.set_caption( tiêuĐề )

	my_font = pygame.font.Font("ARIAL.TTF", 20)
	my_font_20 = pygame.font.Font("ARIAL.TTF", 20)
	Nút.âmThanh = pygame.mixer.Sound("click.mp3")
	
	"""chiều dọc,chiều ngang"""
	bànCờ = MaTrận((350,10), 3, 3,my_font)

	bànCờ.TạoẢnh()
	
	điềuKhiển = ĐiềuKhiển(
		Nút((20,310),(100,40) , "UCS" 	, pygame.Color("black") , pygame.Color("white") , my_font),
		Nút((20,370),(100,40) , "BFS" 	, pygame.Color("black") , pygame.Color("white") , my_font),
		Nút((20,430),(100,40) , "A*"	, pygame.Color("black") , pygame.Color("white") , my_font),
		Nút((20,490),(100,40) , "LDFS"	, pygame.Color("black") , pygame.Color("white") , my_font),
		Nút((150,250),(100,40) , "Greedy", pygame.Color("black") , pygame.Color("white") , my_font),
		Nút((150,310),(100,40) , "IDS-10", pygame.Color("black") , pygame.Color("white") , my_font),
		Nút((150,370),(100,40) , "Tremaux+", pygame.Color("black") , pygame.Color("white") , my_font_20),
		Nút((20,250),(100,40) , "Ảnh" 	, pygame.Color("black") , pygame.Color("white") , my_font),
		Nút((150,430),(100,40) , "Đảo" 	, pygame.Color("black") , pygame.Color("white") , my_font),
		Nút((150,490),(100,40) , "RESET", pygame.Color("black") , pygame.Color("white") , my_font),
		Nút((500,dọcPM-100),(100,40),"BACK",pygame.Color("black") , pygame.Color("white") , my_font),
		Nút((700,dọcPM-100),(100,40),"NEXT",pygame.Color("black") , pygame.Color("white") , my_font),
	 Number((10,70),bànCờ.hàngTốiĐa,bànCờ.cộtTốiĐa,my_font),
		
		
	  BộĐếm((10,550), pygame.Color("black"), 					my_font),
		CheckBox(10,180,20,20, "Đảo phím di chuyển",pygame.Color("red"),my_font),
		CheckBox(10,210,20,20, "Số đơn giản",pygame.Color("red"),my_font),
	)
	tácGiả = Banner(0,dọcPM-40,ngangPM,"\u25C4\u25BA 21110861 - Trần Hoàng Anh Tú \u25C4\u25BA 21110354 - Đoàn Nhựt Quang Vinh \u25C4\u25BA 21110358 - Tào Chí Vỹ ",
	pygame.Color("black"),my_font)
	nútÂmThanh = Nhạc(20,20,30)
	return bànCờ, scr , điềuKhiển,tácGiả,nútÂmThanh


