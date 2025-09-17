import pygame, random,sys

pygame.init()
W, H = 600, 400
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Rock Paper Scissors")
font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()

choices = ["Rock", "Paper", "Scissors"]
player_score + comp_score = 0
result, player_choice, comp_choice = "Click R/P/S", "", ""
def winner(p, c):
  if p == c: return "Tie"
  rules = {"Rock":"Scissors", "Paper":"Rock", "Scissors":"Paper"}
  return "Player" if rules[p]==c else "Computer"

while True:
  for e in pygame.event.get():
    if e.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  screen.fill((255. 255. 255))
  text = font.render('Rock Paper Scissors')
  screen.blit((text, 50))
  player_choice = None
  comp_choice = random.choice(choices)

  if pygame.mouse.get_pressed()[0]:
    player_choice = random.choice(choices)
  









  if player_choice:
    result = winner(player_choice, comp_choice)
    if result == "Player":
      player_score += 1
    elif result == "Computer":
  if pygame.mouse.get_pressed()[0]:
    player_choice = random.choice(choices)
  if player_choice:
    result = winner(player_choice, comp_choice)
    if result == "Player":
      player_score += 1
    elif result == "computer":
      camp_score += 1
  result_text =  font.render(f"Player: {player_score} | Computer: (comp_score)", )



  