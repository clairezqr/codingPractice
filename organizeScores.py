#practice: read file

scores_file = open("student_scores.txt","r")
scores = {}

line = scores_file.readline()

while line:
	line = line.strip('\n').split()
	line[2] = int(line[2])
	
	#order by scores
	if line[2] in scores:
		scores[line[2]].append(f'{line[0]} {line[1]}')
	else:
		scores[line[2]] = [f'{line[0]} {line[1]}']
	line = scores_file.readline()

scores_file.close()

#sort scores with one or more students
for i in scores:
	if len(scores[i]) > 1:
		scores[i].sort()
		
order = sorted(scores.keys(), reverse = True)

for i in order:
	for j in scores[i]:
		print(f'{j:<30}{i:<40}')