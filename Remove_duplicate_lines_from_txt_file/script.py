import hashlib
import sys

try:
	fileName = sys.argv[1]
except:
	print('You didn\'t supply a valid filename.')
	exit()

input_file = open(fileName, "r")

#define your output path
output_file = open('E:/output.txt', "w")

lines_seen_so_far = set()

for line in input_file:
  
  hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
  
  if hashValue not in lines_seen_so_far:
    output_file.write(line)
    lines_seen_so_far.add(hashValue)

output_file.close()
input_file.close()

print("duplicate lines removed successfully")
