import pygame


class Button:
    """A class to build buttons for the game."""

    def __init__(self, ai_game):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Load the play button image and set it's rect attribute..
        self.image = pygame.image.load('images/PlayButton.bmp')
        self.rect = self.image.get_rect()

        # Build the button's rect object and center it.
        self.rect.center = self.screen_rect.center

    def draw_button(self):
        """Draw button"""
        self.screen.blit(self.image, self.rect)
