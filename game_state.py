from dataclasses import dataclass, field
import copy

BLANK_GRID = [
    [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 99, 99, 99, 99],
    [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 99, 99, 99, 99],
    [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 99, 99, 99, 99],
    [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 99, 99, 99, 99],
    [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 99, 99, 99, 99],
    [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 99, 99, 99, 99],
    [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 99, 99, 99, 99],
    [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 99, 99, 99, 99],
    [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 99, 99, 99, 99],
    [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99],
]

@dataclass
class GameState:
    # ── screen routing ────────────────────────────────────────────────
    screen: str = "PSW"         # current active screen
    return_screen: str = ""     # screen to return to after pause menu

    # ── game setup options ────────────────────────────────────────────
    two_player: bool = False    # False = 1 player, True = 2 player
    difficulty: str = "Easy"   # "Easy" or "Hard"
    time_enabled: bool = False
    time_set: float = 0         # seconds per player

    # ── game progress ─────────────────────────────────────────────────
    in_game: bool = False
    turn: int = 0
    players_ready: int = 0      # how many players have placed boats
    winner: str = "undecided"
    loser: str = ""
    quote: str = ""

    # ── boat grids ────────────────────────────────────────────────────
    placing_grid: list = field(default_factory=lambda: copy.deepcopy(BLANK_GRID))
    p1_boats: list     = field(default_factory=list)
    p2_boats: list     = field(default_factory=list)
    p1_rot: list       = field(default_factory=list)
    p2_rot: list       = field(default_factory=list)

    # ── sunk tracking ─────────────────────────────────────────────────
    p1_boats_sunk: list         = field(default_factory=lambda: [0, 0, 0, 0, 0])
    p2_boats_sunk: list         = field(default_factory=lambda: [0, 0, 0, 0, 0])
    p1_boats_sunk_visible: list = field(default_factory=lambda: [0, 0, 0, 0, 0])
    p2_boats_sunk_visible: list = field(default_factory=lambda: [0, 0, 0, 0, 0])

    # ── timers ────────────────────────────────────────────────────────
    p1_time: float = 0
    p2_time: float = 0

    # ── win screen stats ──────────────────────────────────────────────
    shot_count: int = 0
    accuracy: int = 0
    turn_count: int = 0
    spt: float = 0.0            # shots per turn

    # ── settings ──────────────────────────────────────────────────────
    fps: int = 30
    master_vol: float = 1.0
    music_vol: float = 0.75
    sfx_vol: float = 0.75

    # ── methods ───────────────────────────────────────────────────────
    def reset_for_new_game(self):
        """Call this when starting a fresh game."""
        self.turn = 0
        self.players_ready = 0
        self.winner = "undecided"
        self.loser = ""
        self.quote = ""
        self.p1_boats = []
        self.p2_boats = []
        self.p1_rot = []
        self.p2_rot = []
        self.p1_boats_sunk = [0, 0, 0, 0, 0]
        self.p2_boats_sunk = [0, 0, 0, 0, 0]
        self.p1_boats_sunk_visible = [0, 0, 0, 0, 0]
        self.p2_boats_sunk_visible = [0, 0, 0, 0, 0]
        self.placing_grid = copy.deepcopy(BLANK_GRID)
        if self.time_enabled:
            self.p1_time = self.time_set
            self.p2_time = self.time_set

    def switch(self, screen: str):
        """Change the active screen."""
        self.screen = screen
        print(screen)