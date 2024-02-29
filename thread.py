import threading

class SubThread:
	def __init__(self):
		self.trạngThái = "dừng"
		self.dữLiệu = []
		self.thread = None
		self.chiếmBộNhớ = 0
	def Tạo(self,hàm,bànCờ,bộĐếm):
		if(self.thread is None and self. trạngThái == "chạy"):
			self.thread = threading.Thread (target = hàm,args =(bànCờ,self,bộĐếm) )
			self.thread.start()

	def ĐổiTrạngThái(self):
		if(self.trạngThái == "chạy"):
			self.trạngThái = "dừng"
		else:
			self.trạngThái = "chạy"

	def CậpNhậtLuồngSongSong(self):
		if self.thread is not None:
			if(self.trạngThái == "chạy"):
				return
			self.thread.join()
			print("end thread")
			self.thread = None
			if(self.trạngThái == "dừng"):
				self.dữLiệu.clear()
				return
