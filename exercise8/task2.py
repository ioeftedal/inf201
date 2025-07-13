from abc import ABC, abstractmethod

import meshio


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Cell(ABC):
    def __init__(self, index: int, points) -> None:
        super().__init__()
        self.index = index
        self._points = points
        self._neighbors = []

    @abstractmethod
    def border_check(self) -> bool:
        pass

    @abstractmethod
    def neighbor_check(self, cell) -> bool:
        pass

    def neighbor_add(self, neighbor):
        self._neighbors.append(neighbor)


class Line(Cell):
    def __init__(self, index, points) -> None:
        super().__init__(index, points)

    def neighbor_check(self, cells) -> None:
        for cell in cells:
            for points in cell:
                if (self.x, self.y) == points:
                    neighbor_add.append(cell)

    def border_check(self) -> bool:
        for neighbor in self._neighbors:
            if type(neighbor) == Line:
                return True
        return False


class Triangle(Cell):
    def __init__(self, index, points) -> None:
        super().__init__(index, points)


class Mesh:
    def __init__(self, cells, points) -> None:
        self.cells = cells
        self.points = points
        pass


msh = meshio.read("simple.msh")

points = msh.points
cells = msh.cells

cell = cells[1].data[222]

print(cell)
print(cells[1].type)
