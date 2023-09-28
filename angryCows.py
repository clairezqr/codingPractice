#USACO 2016 January Bronze

# import sys
# sys.stdin = open("angry.in", 'r')
# sys.stdout = open("angry.out", 'w')

#calculate number of explosions at each position
def calculate(hayBale):
	allHayBales = list(hay_bales)
	allHayBales.remove(hayBale[0])
	counter = 1 #blast radius
	check = True #check if exploded
	explosions = 0
	while check:
		check = False
		for i in hayBale:
			for j in range(1, counter + 1):
				#check right side
				if (i + j) in allHayBales:
					allHayBales.remove(i + j)
					hayBale.append(i + j)
					explosions += 1
					check = True
				#check left side
				if (i - j) in allHayBales:
					allHayBales.remove(i - j)
					hayBale.append(i - j)
					explosions += 1
					check = True
			hayBale.remove(i)
		counter += 1
	return explosions + 1


N = int(input())
hay_bales = []
explosions = []

for i in range(N):
	hay_bales.append(int(input()))

hay_bales = tuple(hay_bales)
	
for i in hay_bales:
	explosions.append(calculate([i]))
print(max(explosions))