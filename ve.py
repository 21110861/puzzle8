import pygame
from matran import MaTrận

def Vẽ(mànHình, bànCờ, điềuKhiển,tácGiả,nútÂmThanh):
	mànHình.fill(pygame.Color("white"))
	bànCờ.Vẽ(mànHình)
	điềuKhiển.Vẽ(mànHình)
	tácGiả.Vẽ(mànHình)
	nútÂmThanh.Vẽ(mànHình)
	pygame.display.flip() 

