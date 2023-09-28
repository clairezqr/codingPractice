#CCC 2012 S3

N = int(input())
sensor_readings = {}
sensors = []

for i in range(N):
	sensors.append(int(input()))
sensors.sort()

while len(sensors) != 0:
	#find frequency
	frequency = sensors.count(sensors[0])
	#order by frequency
	if frequency in sensor_readings:
		sensor_readings[frequency].append(sensors[0]) 
	else:
		sensor_readings[frequency] = [sensors[0]]
	
	del sensors[:frequency]
#sort frequencies	
frequencies = sorted(sensor_readings.keys(), reverse = True)

if len(sensor_readings[frequencies[0]]) == 1:
	if len(sensor_readings[frequencies[1]]) == 1:
		answer = abs(sensor_readings[frequencies[0]][0] - sensor_readings[frequencies[1]][0])
	else:
		temp_1 = abs(sensor_readings[frequencies[0]][0] - max(sensor_readings[frequencies[1]]))
		temp_2 = abs(sensor_readings[frequencies[0]][0] - min(sensor_readings[frequencies[1]]))
		if temp_1 > temp_2:
			answer = temp_1
		else:
			answer = temp_2
else:
	answer = max(sensor_readings[frequencies[0]]) - min(sensor_readings[frequencies[0]])

print(answer)