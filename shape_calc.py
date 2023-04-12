
from dataclasses import dataclass
from typing import Union

@dataclass
class Rectangle:
    
    width: int
    height: int

    def set_width(self, width: int) -> None:
      
        self.width = width

    def set_height(self, height: int) -> None:
        
        self.height = height

    def get_area(self) -> int:
       
        return self.width * self.height

    def get_perimeter(self) -> int:
        
        return 2 * self.width + 2 * self.height

    def get_diagonal(self) -> Union[int, float]:
       
        return pow(pow(self.width, 2) + pow(self.height, 2), 0.5)

    def get_picture(self) -> str:
        
        if not (self.width or self.height) > 50:
            picture: str = ("*" * self.width + "\n") * self.height
            picture

            return picture
        else:
            return "Too big for picture."

    def get_amount_inside(self, shape) -> int:
       
        return self.get_area() // shape.get_area()


class Square(Rectangle):

    def __init__(self, side: int) -> None:
        self.width = side
        self.height = side

    def set_side(self, side: int) -> None:
       
        self.width = side
        self.height = side

    def __repr__(self) -> str:
        return self.__class__.__qualname__ + f"(side={self.width!r})"
