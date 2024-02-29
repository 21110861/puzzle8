def HiệuỨng(thờiGian):
	for i in range(len(HiệuỨng.danhSách)):
		miliGiây,hiệuỨng = HiệuỨng.danhSách[i]
		miliGiây[0] += thờiGian.get_time()
		hoànThành = hiệuỨng(miliGiây)
		if hoànThành == True:
			HiệuỨng.danhSách.pop(i)


HiệuỨng.danhSách = []