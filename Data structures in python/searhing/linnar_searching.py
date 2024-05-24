
num = [24,34,6,2,63,46,72,55,552,22,42,52,64]

target = 72

count = 0
for i in range(len(num)):
  if num[i] == target:
    count = i
    break

if count == 0:
  print("target is not found")
else:
  print(f'targer is count in the list at {count}th index')