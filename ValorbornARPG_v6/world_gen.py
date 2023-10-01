import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from interpolation import lerp
from player import Player

class World:
    def __init__(self):
        self.bg_color = (0, 0, 0)  # Black background
        self.grid_color = (255, 255, 255)  # White grid lines
        self.grid_size = 50  # Size of each grid cell
        self.prev_player_x = 0
        self.prev_player_y = 0

    def draw_background(self, window):
        window.fill(self.bg_color)

    def draw_origin(self, window):
        origin_x = SCREEN_WIDTH // 2
        origin_y = SCREEN_HEIGHT // 2
        pygame.draw.circle(window, self.grid_color, (origin_x, origin_y), 10)
        font = pygame.font.SysFont(None, 12)
        label = font.render("0,0", True, self.grid_color)
        window.blit(label, (origin_x + 15, origin_y - 5))

    def draw_grid(self, window, player_x, player_y, alpha):
        # Calculate the top-left corner of the screen in world coordinates
        top_left_x = player_x - SCREEN_WIDTH // 2
        top_left_y = player_y - SCREEN_HEIGHT // 2
        self.prev_player_x = player_x
        self.prev_player_y = player_y

        # interpolate
        interpolated_x = lerp(self.prev_player_x, player_x, alpha)
        interpolated_y = lerp(self.prev_player_y, player_y, alpha)
        offset_x = SCREEN_WIDTH // 2 - interpolated_x
        offset_y = SCREEN_HEIGHT // 2 - interpolated_y

        # Draw vertical grid lines
        x = top_left_x - (top_left_x % self.grid_size)
        while x < top_left_x + SCREEN_WIDTH:
            pygame.draw.line(window, self.grid_color, (x - top_left_x, 0), (x - top_left_x, SCREEN_HEIGHT))
            x += self.grid_size

        # Draw horizontal grid lines
        y = top_left_y - (top_left_y % self.grid_size)
        while y < top_left_y + SCREEN_HEIGHT:
            pygame.draw.line(window, self.grid_color, (0, y - top_left_y), (SCREEN_WIDTH, y - top_left_y))
            y += self.grid_size

        # Draw labels at every 5th grid intersection
        x = top_left_x - (top_left_x % (self.grid_size * 5))
        while x < top_left_x + SCREEN_WIDTH:
            y = top_left_y - (top_left_y % (self.grid_size * 5))
            while y < top_left_y + SCREEN_HEIGHT:
                font = pygame.font.SysFont(None, 12)
                label = font.render(f"{x//self.grid_size},{y//self.grid_size}", True, self.grid_color)
                window.blit(label, (x - top_left_x + 5, y - top_left_y))
                y += self.grid_size * 5
            x += self.grid_size * 5

