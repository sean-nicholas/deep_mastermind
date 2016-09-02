import random

class Game():
  colors = 6
  columns = 4
  solution = []

  def get_random_color(self):
    return random.randrange(0, self.colors)

  def init(self):
    self.solution = [self.get_random_color() for i in range(self.columns)]

  def assess(self, guess):
    color_counter = [0 for i in range(0, self.colors)]
    correct_position = 0
    correct_color = 0
    for column_index, column in enumerate(guess):
      for color, is_set in enumerate(column):
        if (is_set == 1):
          color_counter[color] += 1

          if (self.solution[column_index] == color):
            correct_position += 1

    for color in self.solution:
      color_counter[color] -= 1
      if (color_counter[color] >= 0):
        correct_color += 1
    
    correct_color -= correct_position
    
    return correct_color, correct_position

game = Game()
game.init()
assessment = game.assess([
  [1, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0, 0]
])
print(game.solution)
print(assessment)