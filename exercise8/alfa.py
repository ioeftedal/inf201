import meshio

from .common import _fast_forward_over_blank_lines

msh = meshio.read("simple.msh")

points = msh.points
cells = msh.cells

# print(points)

# cell = cells[1].data[222]

# for cell in cells:
#     print(cell)

# for i in range(69):
#     print(cells[0].data[i])


environ = line[1:].strip()

for cell in cells:
    if environ = 
