import pygame
from screens.base import Screen

class PSWScreen(Screen):
    def __init__(self, assets, state):
        super().__init__(assets, state)
        self.ticks = 0

    def update(self, dt, events):
        # skip on any key press
        keys = pygame.key.get_pressed()
        if True in keys:
            self.state.switch("main")

        self.ticks += 60 * dt

        # auto switch after delay
        if self.ticks >= 400:
            self.state.switch("main")

    def draw(self, surface):
        surface.blit(
            pygame.transform.scale(self.assets.psw, (1280, 720)),
            (0, 0)
        )

        # fade to black between ticks 200-400
        if 200 <= self.ticks <= 400:
            alpha = int(1.25 * (self.ticks - 200))  # 0 → 255 over 200 ticks
            fade = pygame.Surface((1280, 720))
            fade.set_alpha(alpha)
            fade.fill((0, 0, 0))
            surface.blit(fade, (0, 0))