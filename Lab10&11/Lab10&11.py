import CustomExceptions
import Shapes

try:
    triangle = Shapes.RightAngleTriangle()
    print(triangle.get_area())
except CustomExceptions.LengthNotDefined as e:
    print(e)
