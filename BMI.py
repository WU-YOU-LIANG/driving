h = input('請輸入你的身高為幾公分 ')
h = int(h)
h = h / 100
w = input('請輸入你的體重為幾公斤 ')
w = int(w)

BMI = w / h / h

if BMI < 18.5:
	print('過輕')
elif BMI >= 18.5 and BMI < 24:
	print('正常')
elif BMI >= 24 and BMI < 27:
	print('過重')
elif BMI >= 27 and BMI < 30:
	print('輕度肥胖')
elif BMI >= 30 and BMI < 35:
	print('中度肥胖')
else:
	print('重度肥胖')
