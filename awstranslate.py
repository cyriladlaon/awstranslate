import sys
# print(sys.argv[1])
lines = []
with open(sys.argv[1], 'r') as f:
	lines = f.readlines()

valid_lines = []

for line in lines:
    if line.strip().startswith('//'):
    	continue
    valid_lines.append(line)
valid_lines[0] = '{'
if valid_lines[-2][-1] == ',':
	valid_lines[-2] = valid_lines[-2][:-1]

with open('vern.json', 'w') as f:
	f.writelines(valid_lines)