import pygame
import random

# Ekran boyutları
WIDTH = 800
HEIGHT = 600

# Renkler
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Oyun sınıfı
class Game:
    


    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Top Oyunu")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 40)
        self.running = True
        self.score = 0
        self.speed = 5
        self.bar_width = 150
        self.bar_height = 20
        self.bar_x = (WIDTH - self.bar_width) // 2
        self.ball_radius = 10
        self.ball_x = random.randint(self.ball_radius, WIDTH - self.ball_radius)
        self.ball_y = HEIGHT // 2
        self.ball_dx = random.choice([-1, 1]) * self.speed
        self.ball_dy = -self.speed
        self.start_time = pygame.time.get_ticks()

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and not self.running:
                    self.restart_game()



    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.bar_x > 0:
            self.bar_x -= self.speed
        if keys[pygame.K_RIGHT] and self.bar_x < WIDTH - self.bar_width:
            self.bar_x += self.speed

        self.ball_x += self.ball_dx
        self.ball_y += self.ball_dy

        # Topun ekran sınırlarına çarpması durumu
        if self.ball_x <= self.ball_radius or self.ball_x >= WIDTH - self.ball_radius:
            self.ball_dx *= -1
        if self.ball_y <= self.ball_radius:
            self.ball_dy *= -1

        # Topun çubuğa çarpması durumu
        if self.ball_y >= HEIGHT - self.bar_height - self.ball_radius and \
                self.bar_x <= self.ball_x <= self.bar_x + self.bar_width:
            self.ball_dy *= -1
            self.score += 1
            self.speed += 0.2

        # Topun yere çarpması durumu
        if self.ball_y >= HEIGHT - self.ball_radius:
            self.running = False

    def draw(self):
        self.screen.fill(BLACK)
        pygame.draw.rect(self.screen, WHITE, (self.bar_x, HEIGHT - self.bar_height, self.bar_width, self.bar_height))
        pygame.draw.circle(self.screen, RED, (int(self.ball_x), int(self.ball_y)), self.ball_radius)
        score_text = self.font.render("Skor: " + str(self.score), True, WHITE)
        self.screen.blit(score_text, (10, 10))
        pygame.display.flip()
        

    def play(self):
        while self.running:
            self.process_events()
            self.update()
            self.draw()
            self.clock.tick(60)

        # Oyun bittiğinde yeniden oynama seçeneği
        while True:
            self.screen.fill(BLACK)
            game_over_text = self.font.render("Oyun Bitti! Skorunuz: " + str(self.score), True, WHITE)
            self.screen.blit(game_over_text, (WIDTH // 2 - 200, HEIGHT // 2 - 50))
            restart_text = self.font.render("Tekrar Oynamak için R tuşuna basın", True, WHITE)
            self.screen.blit(restart_text, (WIDTH // 2 - 220, HEIGHT // 2 + 50))
            pygame.display.flip()
        def restart_game(self):
            self.score = 0
            self.speed = 5
            self.bar_x = (WIDTH - self.bar_width) // 2
            self.ball_x = random.randint(self.ball_radius, WIDTH - self.ball_radius)
            self.ball_y = HEIGHT // 2
            self.ball_dx = random.choice([-1, 1]) * self.speed
            self.ball_dy = -self.speed
            self.running = True
            self.play()



if __name__ == "__main__":
    game = Game()
    game.play()
