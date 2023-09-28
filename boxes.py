#CCC 2007 S2
#organize dimensions & calculate volume
def organizeSize():
	for j in range(3):
		box[j] = int(box[j])
	box.sort()
	volume = box[0] * box[1] * box[2]
	return volume

#box input
n = int(input())
sizes = {}
for i in range(n):
	box = input().split()
	volume = organizeSize() 
	if volume in sizes:
		sizes[volume].append(box)
	else:
		sizes[volume] = [box]

all_volumes = sorted(sizes.keys())


m = int(input())
for i in range(m):
	#items input
	box = input().split()
	volume = organizeSize()
	start = -1
	#check volume
	for j in range(len(all_volumes)):
		if all_volumes[j] >= volume:
			start = j
			break
	if start == -1:
		print('Item does not fit.')
	else:
		#check dimensions
		check = False
		for j in all_volumes[start:]:
			if check:
				break
			for k in sizes[j]:
				if k[0] >= box[0] and k[1] >= box[1] and k[2] >= box[2]:
					print(j)
					check = True
					break
		if check == False:
			print('Item does not fit.')