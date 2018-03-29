for yindex,y in enumerate(grid):
    for xindex,x in enumerate(y):
        if x == node:
           current = f"{xindex} {yindex}"
           print(f"current={current}", file=sys.stderr)
           
           #right
           right = "-1 -1"
           if (len(y)-1) >= (xindex+1) and y[xindex+1] == node:
               right = f"{xindex+1} {yindex}"
           print(f"right={right}", file=sys.stderr)
           
           #bottom
           bottom = "-1 -1"
           if (len(grid)-1) >= (yindex + 1) and grid[yindex + 1][xindex] == node:
               bottom = f"{xindex} {yindex+1}"
           print(f"bottom={bottom}", file=sys.stderr)
        
           
           print(f"{current} {right} {bottom}")
           