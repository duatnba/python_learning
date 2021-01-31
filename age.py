#迴圈練習
age=input('請輸入您的年齡：')
grade=[{'str':'社會人士','old':'22'},{'str':'大學生','old':'18'},{'str':'高中生','old':'15'},{'str':'國中生','old':'12'},{'str':'小學生','old':'6'},{'str':'嬰幼兒','old':'0'}]
for i in grade:
	if age>=i['old']:
		print('您的身份為',i['str'])
		break
	else:
		continue