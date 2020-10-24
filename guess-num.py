import random
start = int(input('請決定隨機數字開始值： '))
end = int(input('請決定隨機數字結束值： '))
answer = random.randint(start,end)
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

 