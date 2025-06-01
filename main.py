import pygame
from player import Player
from asteroid import Asteroid
from constants import *
from asteroidfield import *
from circleshape import CircleShape
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()
    shot = pygame.sprite.Group()

    Shot.containers = (updatable, drawable, shot)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)   
    AsteroidField.containers = (updatable)
    
    dt = 0
    lifes = 3
    score = 0

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        for a in asteroids:
            if player.collision(a):
                if lifes <= 1:
                    print("Game over!!!")
                    print(f"Score: {score}")
                    return
                lifes -= 1
                for a in asteroids:
                    a.kill()
                player.kill()
                player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
                print("lost one life")
                print(f"lifes remaining: {lifes}")
                print("respawning")
        
            for s in shot:
                if s.collision(a):
                    a.split()
                    s.kill()
                    score += 1
                    print("+1 point")

        screen.fill("black")
        for i in drawable:          
            i.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000

        

    
    







































if __name__ == "__main__":
    main()