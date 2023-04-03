class Taxicab:
    """

    """
    def __init__(self, x, y):
        """

        :param x:
        :param y:
        :param odom:
        """
        self._x_coord = x
        self._y_coord = y
        self.od = 0


    def get_x_coord(self):
        """

        :return:
        """
        return self._x_coord

    def get_y_coord(self):
        """

        :return:
        """
        return self._y_coord

    def move_x(self, new_x):
        """

        :param new_x:
        :return:
        """
        self._x_coord += new_x
        self.od += abs(new_x)


    def move_y(self, new_y):
        """

        :param new_y:
        :return:
        """
        self._y_coord += new_y
        self.od += abs(new_y)


    def get_odometer(self):
        """

        :return:
        """
        return self.od




cab = Taxicab(5, -8)
cab.move_x(3)
cab.move_y(-4)
cab.move_x(-1)
print(cab.get_odometer())




