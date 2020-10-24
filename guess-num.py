import random

answer = random.randint(1,100)
while True:
	guess = int(input('請猜看看數字：'))
	if guess > answer:
		print('你猜得比答案大')
	elif guess < answer:
		print('你猜得比答案小')
	else:
		print('終於猜對了!')
		break
 