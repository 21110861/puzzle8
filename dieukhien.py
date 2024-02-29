from nut import Nút
from bodem import BộĐếm
from number import Number
from checkbox import CheckBox

class ĐiềuKhiển:
	def __init__(self ,*argvs):
		self.điềuKhiển = [i for i in argvs]
		self.nút = []
		self.bộĐếm = []
		self.combo = []
		self.checkbox = []
		for i in self.điềuKhiển:
			if( isinstance(i, Nút)):
				self.nút.append(i)
			elif ( isinstance(i, BộĐếm)):
				self.bộĐếm.append(i)
			elif( isinstance(i, Number)):
				self.combo.append(i)
			elif( isinstance(i, CheckBox)):
				self.checkbox.append(i)
				
	def CậpNhậtHiệuỨng(self,thờiGian):
		if thờiGian[0] >= 100:
			thờiGian[0] = 0
	def Vẽ(self, mànHình):
		for i in self.điềuKhiển:
			i.Vẽ(mànHình)