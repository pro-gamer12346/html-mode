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