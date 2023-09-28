#USACO 2021 December Bronze

N = int(input())
string = input()
lonely = 0
cows = []
start = 3

for i in range(N):
	if i == 0:
		temp = 1
	else:
		if string[i] == string[i - 1]:
			temp += 1
		else:
			cows.append(temp)
			temp = 1
cows.append(temp)
#print(cows)			

for i in range(len(cows)):
	left = 0
	right = 0
	cow = 0
	if cows[i] > 1:
		if i != len(cows) - 1:
			lonely += cows[i + 1] - 1
				
	else:
		if i != 0:
			left = cows[i - 1]
		if i != len(cows) - 1:
			right = cows[i + 1]
		cow = left + right + 1
		#print(cow)

		if cow > 3:
			cow_min = min(left, right)
			if cow_min >= 3:
				for j in range(2, cow_min + 1):
					lonely += j + 1
				start = cow_min + 2
			for j in range(start, cow + 1):
				if cow - cow_min >= j:
					lonely += cow_min + 1
				else:
					lonely += cow_min + 1 - (j - (cow - cow_min))
		elif cow == 3:
			lonely += 1
		
print(lonely)