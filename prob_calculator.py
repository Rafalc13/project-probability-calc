import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for color, count in kwargs.items():
      self.contents.extend([color] * count)
    #print(color, count, self.contents)

  def draw(self, numb):
    draws = []
    if numb > len(self.contents):
      return self.contents
    for i in range(numb):
      ball = random.choice(self.contents)
      self.contents.remove(ball)
      draws.append(ball)
      #remove = self.contents.pop(int(random.random() * len(self.contents)))
      #draws.append(remove)
      #print(self.contents, draws, numb)
    return draws



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  goal = 0
  for i in range(num_experiments):
    expected_copy = copy.deepcopy(expected_balls)
    copy_hat = copy.deepcopy(hat)
    draw_balls = copy_hat.draw(num_balls_drawn)
    for color in draw_balls:
      if color in expected_copy and expected_copy[color] > 0:
        expected_copy[color] -= 1
    if all(v == 0 for v in expected_copy.values()):
      goal += 1

  return goal / num_experiments



    
