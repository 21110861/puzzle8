import pygame
def TạoẢnh(ảnhvẽ,cộtTốiĐa,hàngTốiĐa,đườngDẫn="big.png"):
	print("???????????????")
	try:
		ảnh = []
		fullpic = pygame.image.load( đườngDẫn )
		width, height = fullpic.get_size()
		width = width/cộtTốiĐa
		height = height/hàngTốiĐa
		for y in range(hàngTốiĐa):
			for x in range(cộtTốiĐa):
			
				vùng = pygame.Surface((width, height))
				vùng.blit(fullpic, (0,0) , (x * width, y * height , width,height))
				vùng = pygame.transform.scale( vùng,(100,100) )
				ảnh.append (vùng)
				print(len(ảnh))
		
		for i in range(len(ảnh)):
			print("true")
			ảnhvẽ[i] = ảnh[i]
	except:
		ảnhvẽ