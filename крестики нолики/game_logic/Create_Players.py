class Player:
    def __init__(self, name_player):
        self.name_player = name_player
        self.row = 0
        self.col = 0

    def player_choice(self, row, col):
        self.row = row
        self.col = col

    def __str__(self):
        return f"игрок с именем \"{self.name_player}\""
