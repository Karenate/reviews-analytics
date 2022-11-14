# 留言分析程式 reviews-analytics
# 讀取留言檔
# 每1000筆印一次總數
# 計算留言平均長度

data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 1000 == 0: # $ 用來求餘數
			print(len(data))

print('--------------')
print('檔案讀取完了, 總共有', len(data), '筆資料') 

sum_len = 0
for d in data:
	sum_len += len(d) # sum_len = sum_len + len(d)

print('留言平均長度為', sum_len / len(data), '個字')