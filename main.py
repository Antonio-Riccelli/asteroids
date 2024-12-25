import pygame
import sys

from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
	pygame.init()
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Shot.containers = (updatable, drawable, shots)


	Player.containers = (updatable, drawable)
	player = Player(x, y)

	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	asteroid_field = AsteroidField()
	
	clock = pygame.time.Clock()
	dt = 0
	print("Starting asteroids!")
	print("Screen width:", SCREEN_WIDTH)
	print("Screen height:", SCREEN_HEIGHT)
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while (True):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0, 0, 0))
		# player.draw(screen)

		time_since_last_tick = clock.tick(60)
		dt = time_since_last_tick / 1000
		# player.update(dt)
		for member in updatable:
			member.update(dt)
		for member in drawable:
			member.draw(screen)
		for member in asteroids:
			player_collision = member.check_collision(player)
			if player_collision == True:
				print("Game over!")
				sys.exit()
			for bullet in shots:
				bullet_collision = member.check_collision(bullet)
				if bullet_collision == True:
					bullet.kill()
					member.split()
		pygame.display.flip()

		
		

if __name__ == "__main__":
	main()
