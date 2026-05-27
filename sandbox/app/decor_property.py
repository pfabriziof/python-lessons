# @property: Decorator used to define a method as a property (it can be accessed like an attribute)
#            Benefit: add additional logic when read, write or delete attributes.
#            Gives us getter, setter and a deleter methods.

class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self._width : int = width
        self._height : int = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"
    @property
    def height(self):
        return f"{self._height:.1f}cm"
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width should be greater than zero")
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height should be greater than zero")
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")
    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")

if __name__ == "__main__":
    rectangle = Rectangle(3,4)

    rectangle.width = 6
    rectangle.height = -1

    print(rectangle.width)
    print(rectangle.height)

    del rectangle.width
    del rectangle.height

    assert not hasattr(rectangle, 'width')
    assert not hasattr(rectangle, 'height')

