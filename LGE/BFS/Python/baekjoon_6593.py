from collections import deque

NZ, NX, NY = map(int, input().split())
print(f"NZ ,NX, NY = {NZ, NX, NY}")
q = deque()


# maps = [[0 for col in range(NY)] for row in range(NX)]
maps2 = [0]*NZ
# maps = [[0 for col in range(NY)] for row in range(NX)] for depth in range(NZ)

# a.append(maps)
# a.append(maps)
# a.append(maps)
# print(a)

for z in range(NZ):
	maps = [[0 for col in range(NY)] for row in range(NX)]
	for i in range(NX+1):
		temp = list(map(str, input()))
		if(temp == []):
			print("continue")
			continue
		else:
			maps[i] = temp
			# print(f"maps[{i}] = {maps[i]}")
	print(f"maps = {maps}, z = {z}")
	maps2[z] = maps
	print(f"maps2[0] = {maps2[0]}")
	print(f"maps2[1] = {maps2[1]}")
	print(f"maps2[2] = {maps2[2]}")
	
print(maps2)
# for z in range(NZ):
# 	for x in range(NX):
# 		print(maps2[z][x])
# 	print()

# for z in range(NZ):
# 	for i in range(NX):
# 		temp = list(map(str, input()))
# 		if temp == []:
# 			continue
# 		else:
# 			maps[z][i] = temp
		
# print(maps)
# print(maps[2][3][4])


# for i in range(NZ):
# 	print(maps[i])
# 	print()
