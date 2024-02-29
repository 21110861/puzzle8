import pygame
from capnhat import CậpNhật
from khoitao import KhởiTạo
from ve import Vẽ
from thread import SubThread


def main():
	

	bànCờ, scr, điềuKhiển,tácGiả,nútÂmThanh = KhởiTạo("puzzle")
	bànCờ.LấyGiáTrịMới( [1, 2, 5, 3, 4, 8, 0, 6, 7] )
	luồngSongSong = SubThread()
	
	muốnThoát = False
	while not muốnThoát:
	
		Vẽ( scr , bànCờ ,điềuKhiển,tácGiả,nútÂmThanh)

		muốnThoát = CậpNhật(bànCờ, điềuKhiển , luồngSongSong,tácGiả,nútÂmThanh)
	
	pygame.quit()
	
	if luồngSongSong.thread is not None:
		luồngSongSong.trạngThái = "dừng"
		luồngSongSong.thread.join()
###################################################################


if __name__ == "__main__":
	main()