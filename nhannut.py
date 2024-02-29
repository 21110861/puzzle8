import pygame
from matran import MaTrận
from ucs import UCS
from bfs import BFS
from astar import AStar
from ldfs import LDFS
from gre import Greedy
from ids import IDS
from tremaux import Tremaux
from nut import Nút

def NhấnNút(bànCờ: MaTrận ,điềuKhiển, luồngSongSong,nútÂmThanh,cóNhấpChuột) -> None:
	pos = pygame.mouse.get_pos()
	
	i = 0
	thuatToan = [UCS,BFS,AStar,LDFS,Greedy,IDS,Tremaux]
	
	while(i < 7):
		if( điềuKhiển.nút[i].Chạm(pos) == True and cóNhấpChuột):
			Nút.âmThanh.play()
			bànCờ.cũ = [bànCờ.maTrận[:]]
			điềuKhiển.bộĐếm[0].CậpNhật()
			luồngSongSong.ĐổiTrạngThái()
			print(luồngSongSong.trạngThái)
			luồngSongSong.Tạo(thuatToan[i],bànCờ,điềuKhiển.bộĐếm[0])
			return
		i += 1
		
	if( điềuKhiển.nút[i].Chạm(pos) == True and cóNhấpChuột): #Ảnh
		Nút.âmThanh.play()
		bànCờ.LấyẢnh()
		return
	i += 1
	
	if( điềuKhiển.nút[i].Chạm(pos) == True and cóNhấpChuột): #Đảo
		Nút.âmThanh.play()
		bànCờ.ĐảoNgẫuNhiên()
		bànCờ.cũ = [bànCờ.maTrận[:]]
		return
	i += 1

	if( điềuKhiển.nút[i].Chạm(pos) == True and cóNhấpChuột): #RESET
		Nút.âmThanh.play()
		bànCờ.maTrận = bànCờ.cũ.pop()
		bànCờ.cũ = [bànCờ.maTrận[:]]
		điềuKhiển.bộĐếm[0].CậpNhật()
		bànCờ.set0()
		return
	i += 1
	if( điềuKhiển.nút[i].Chạm(pos) == True and cóNhấpChuột): #BACK
		Nút.âmThanh.play()
		if bànCờ.id +1 < len(bànCờ.cũ):
			bànCờ.id += 1
			bànCờ.maTrận = bànCờ.cũ[bànCờ.id][:]
			điềuKhiển.bộĐếm[0].Giảm()
		return
	i += 1
	if( điềuKhiển.nút[i].Chạm(pos) == True and cóNhấpChuột): #NEXT
		Nút.âmThanh.play()
		if bànCờ.id -1 >= 0:
			bànCờ.id -= 1
			bànCờ.maTrận = bànCờ.cũ[bànCờ.id]
			điềuKhiển.bộĐếm[0].Tăng()
		return
	i += 1
	if( điềuKhiển.combo[0].Chạm(pos,cóNhấpChuột) == True  ):	# chỉnh kích thước
		Nút.âmThanh.play()
		bànCờ.KhởiTạoLại(điềuKhiển.combo[0].ngang,điềuKhiển.combo[0].dọc)
		return
	
	điềuKhiển.checkbox[0].Nhấn(cóNhấpChuột)		# check box
	bànCờ.dùngNềnSố = điềuKhiển.checkbox[1].Nhấn(cóNhấpChuột)		# check box
	
	nútÂmThanh.Chạm(pos,cóNhấpChuột)
