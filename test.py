import sys
import math

# Don't let the machines win. You are humanity's last hope...

node = '0'

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

def formatCellVal(val):
    if val == node:
        return f"{x} {y}"
    else:
        return f"-1 -1"

def tryGetVal(grid, x, y):
    try:
        return formatCellVal(grid[y][x])
    except:
        return None

grid = []

for i in range(height):
    line = input()  
    row = []
    for y in line:
        row.append(y)
    
    grid.append(row)


print(grid, file=sys.stderr)

for y in range(height):
    for x in range(width):
        current = tryGetVal(grid, x,y)
        
        if current != None and current == node:
            
    
#print(f'input is {line}', file=sys.stderr)
 
#
    
    
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
    

# Three coordinates: a node, its right neighbor, its bottom neighbor