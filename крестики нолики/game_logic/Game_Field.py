class Field:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def create_field(self):
        return [['.' for _ in range(self.cols)] for _ in range(self.rows)]

    def show_field(self, main_field: list):
        for i in range(self.rows):
            for j in range(self.cols):
                print(main_field[i][j], end=' ')
            print()
