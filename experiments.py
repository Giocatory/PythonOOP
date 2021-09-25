import math
import sys

x1_str, y1_str, x2_str, y2_str = sys.stdin.read().split()

x1 = int(x1_str)
y1 = int(y1_str)
x2 = int(x2_str)
y2 = int(y2_str)

print(f"{math.sqrt((x2-x1)**2 + (y2-y1)**2):.2f}")