class Area:

    def __init__(self, figure_name):
        self.figure_name = figure_name

    # use appropriate decorator
    @classmethod
    def rhombus_area(cls, a, b):
        return .5 * a * b