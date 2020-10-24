import random

answer = random.randint(1,100)
count = 0
while True:
	guess = int(input('請猜看看數字：'))
	count += 1
	if guess > answer:
		print('你猜得比答案大')
	elif guess < answer:
		print('你猜得比答案小')
	else:
		print('終於猜對了!')
		print('你總共猜了', count, '次')
		break
	print('你總共猜了', count, '次')

 