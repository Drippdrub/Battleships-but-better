import pygame
import random
import math
import customwidgets as widgets
from screens.base import Screen

class MenuScreen(Screen):
    def __init__(self, assets, state):
        super().__init__(assets, state)
        
        a = assets
        self.play_btn = widgets.Button(640, 250, a.play_btn,    3, a.play_hover)
        self.options_btn = widgets.Button(640, 375, a.options_btn,  3, a.options_hover)
        self.credits_btn = widgets.Button(640, 500, a.credits_btn, 3, a.credits_hover)
        self.exit_btn = widgets.Button(640, 625, a.exit_btn,    3, a.exit_hover)
        
        self.ticks = 0
        self.rounded_ticks = 0
        self.scroll = 0
        self.startup_played = [0, 0, 0, 0, 0, 0]
        self.font2 = assets.font2
    
    def update(self, dt, events):
        for event in events:
            pass
        
        self.ticks += 60 * dt
        self.rounded_ticks = round(self.ticks)
        self.scroll -= 60 * dt
        if abs(self.scroll) > 1280:
            self.scroll = 0
        t = self.rounded_ticks
        
        # startup sound cues
        if t == 20 and self.startup_played[5] == 0:
            pygame.mixer.Sound.play(self.assets.door_open_sfx)
            self.startup_played[5] = 1

        # title font animation
        delay, duration = 217, 40
        if delay < t < delay + duration:
            self.font2 = pygame.font.Font(
                self._font_path(), 84 + (delay + duration - t) * 6
            )
        else:
            self.font2 = self.assets.font_title

        if t >= delay + duration and self.startup_played[0] == 0:
            pygame.mixer.Sound.play(self.assets.startup_sfx1)
            self.startup_played[0] = 1

    def draw(self, surface):
        t = self.rounded_ticks
        delay, duration = 217, 40

        # scrolling background
        scale = 1
        if t in range(0, 257):
            surface.blit(pygame.transform.scale(
                self.assets.ocean, (1280, 720)), (0, 0))
        else:
            for i in range(math.ceil(1280 / 1280) + 1):
                surface.blit(pygame.transform.scale(
                    self.assets.ocean, (1280, 720)),
                    (i * 1280 + self.scroll, 0))

        # fade in
        if t <= 100:
            alpha = 250 - 2.5 * t
            fade = pygame.Surface((1280, 720))
            fade.set_alpha(alpha)
            fade.fill((0, 0, 0))
            surface.blit(fade, (0, 0))

        # door animation
        self._draw_door(surface, t)

        # title text
        if t > delay:
            title = "Steel and Salvos"
            img = self.font2.render(title, True, (0, 0, 0))
            surface.blit(img, ((1280 - img.get_width()) / 2, 50))

        # buttons (appear one by one)
        pause, interval = 14, 10
        base = delay + pause + duration
        if t >= base + interval * 1:
            self._maybe_play_sfx(1)
            if self.play_btn.draw(surface):
                pygame.mixer.Sound.play(self.assets.blip)
                self.state.screen = "game_options"

        if t >= base + interval * 2:
            self._maybe_play_sfx(2)
            if self.options_btn.draw(surface):
                pygame.mixer.Sound.play(self.assets.blip)
                self.state.screen = "options"

        if t >= base + interval * 3:
            self._maybe_play_sfx(3)
            if self.credits_btn.draw(surface):
                pygame.mixer.Sound.play(self.assets.blip)
                self.state.screen = "credits"

        if t >= base + interval * 4:
            self._maybe_play_sfx(4)
            if self.exit_btn.draw(surface):
                pygame.mixer.Sound.play(self.assets.blip)
                self.state.screen = "exit"

    # ── helpers ──────────────────────────────────────────────────────────

    def _maybe_play_sfx(self, idx):
        if self.startup_played[idx] == 0:
            pygame.mixer.Sound.play(self.assets.startup_sfx2)
            self.startup_played[idx] = 1

    def _draw_door(self, surface, t):
        delay = 130
        frames = self.assets.blast_door_frames
        f = 2
        idx = (t - delay) // f
        if t < delay:
            img = widgets.Image(640, 360, frames[0], 1)
            img.draw(surface)
        elif 0 <= idx < len(frames) and t in range(0, delay + 30):
            img = widgets.Image(640, 360, frames[int(idx)], 1)
            img.draw(surface)

    def _font_path(self):
        from utils import resource_path
        return resource_path("resources/fonts/Crang.ttf")
        