import pygame
from utils import resource_path
from importer import *

class Assets:
    def __init__(self):
        self._load_fonts()
        self._load_images()
        self._load_sounds()
    
    def _load_fonts(self):
        self.font1 = pygame.font.Font(resource_path("resources/fonts/CompassPro.ttf"), 72)
        self.font2 = pygame.font.Font(resource_path("resources/fonts/Crang.ttf"), 84)
        self.font3 = pygame.font.Font(resource_path("resources/fonts/CompassPro.ttf"), 36)
        self.font4 = pygame.font.Font(resource_path("resources/fonts/CompassPro.ttf"), 28)
        self.font5 = pygame.font.Font(resource_path("resources/fonts/CompassPro.ttf"), 18)

        self.font_large = pygame.font.Font(resource_path("resources/fonts/CompassPro.ttf"), 72)
        self.font_title = pygame.font.Font(resource_path("resources/fonts/Crang.ttf"), 84)
        self.font_medium = pygame.font.Font(resource_path("resources/fonts/CompassPro.ttf"), 36)
        self.font_small = pygame.font.Font(resource_path("resources/fonts/CompassPro.ttf"), 28)
        self.font_tiny = pygame.font.Font(resource_path("resources/fonts/CompassPro.ttf"), 18)
        
    def _load_images(self):
        # ── single images ─────────────────────────────────────────────────
        self.ocean        = import_image("resources", "images", "Ocean")
        self.metal_bg     = import_image("resources", "images", "metal bg")
        self.black_screen = import_image("resources", "images", "black_screen")
        self.nuke         = import_image("resources", "images", "nuke")
        self.psw          = import_image("resources", "images", "PSW")
        self.credits      = import_image("resources", "images", "Credits", alpha=False)
        self.pause_icon   = import_image("resources", "images", "Pause")
        self.help_icon    = import_image("resources", "images", "help")
        self.mute         = import_image("resources", "images", "mute")
        self.unmute       = import_image("resources", "images", "unmute")

        # ── buttons ───────────────────────────────────────────────────────
        self.play_btn              = import_image("resources", "images", "buttons", "button_play")
        self.play_hover            = import_image("resources", "images", "buttons", "button_play_hover")
        self.options_btn           = import_image("resources", "images", "buttons", "button_options")
        self.options_hover         = import_image("resources", "images", "buttons", "button_options_hover")
        self.credits_btn           = import_image("resources", "images", "buttons", "button_credits")
        self.credits_hover         = import_image("resources", "images", "buttons", "button_credits_hover")
        self.exit_btn              = import_image("resources", "images", "buttons", "button_exit")
        self.exit_hover            = import_image("resources", "images", "buttons", "button_exit_hover")
        self.back_btn              = import_image("resources", "images", "buttons", "button_back")
        self.back_hover            = import_image("resources", "images", "buttons", "button_back_hover")
        self.okay_btn              = import_image("resources", "images", "buttons", "button_okay")
        self.okay_hover            = import_image("resources", "images", "buttons", "button_okay_hover")
        self.okay_disabled         = import_image("resources", "images", "buttons", "button_okay_disabled")
        self.confirm_fleet_btn     = import_image("resources", "images", "buttons", "button_confirmfleet")
        self.confirm_fleet_hover   = import_image("resources", "images", "buttons", "button_confirmfleet_hover")
        self.randomise_fleet_btn   = import_image("resources", "images", "buttons", "button_randomisefleet")
        self.randomise_fleet_hover = import_image("resources", "images", "buttons", "button_randomisefleet_hover")
        self.resume_btn            = import_image("resources", "images", "buttons", "button_resume")
        self.resume_hover          = import_image("resources", "images", "buttons", "button_resume_hover")
        self.option2_btn           = import_image("resources", "images", "buttons", "button_options2")
        self.option2_hover         = import_image("resources", "images", "buttons", "button_options_hover2")
        self.leave_btn             = import_image("resources", "images", "buttons", "button_leave")
        self.leave_hover           = import_image("resources", "images", "buttons", "button_leave_hover")

        # ── toggles ───────────────────────────────────────────────────────
        self.select_1p      = import_image("resources", "images", "buttons", "toggle_select1P")
        self.select_2p      = import_image("resources", "images", "buttons", "toggle_select2P")
        self.diff_easy      = import_image("resources", "images", "buttons", "toggle_diffEasy")
        self.diff_hard      = import_image("resources", "images", "buttons", "toggle_diffHard")

        # ── time buttons ──────────────────────────────────────────────────
        self.time_off = import_image("resources", "images", "buttons", "time_off")
        self.time_60s = import_image("resources", "images", "buttons", "time_60")
        self.time_90s = import_image("resources", "images", "buttons", "time_90")
        self.time_3m  = import_image("resources", "images", "buttons", "time_3m")
        self.time_5m  = import_image("resources", "images", "buttons", "time_5m")
        self.time_10m = import_image("resources", "images", "buttons", "time_10m")

        # ── fps buttons ───────────────────────────────────────────────────
        self.fps_30  = import_image("resources", "images", "buttons", "fps30")
        self.fps_60  = import_image("resources", "images", "buttons", "fps60")
        self.fps_120 = import_image("resources", "images", "buttons", "fps120")

        # ── player/ai boards ──────────────────────────────────────────────
        self.player1_board  = import_image("resources", "images", "Player1 Board")
        self.player2_board  = import_image("resources", "images", "Player2 Board")
        self.ai_easy_board  = import_image("resources", "images", "AI Easy Board")
        self.ai_hard_board  = import_image("resources", "images", "AI Hard Board")
        self.middle_board   = import_image("resources", "images", "Middle Board")
        self.big_board      = import_image("resources", "images", "Big Board")
        self.left_board     = import_image("resources", "images", "Left Board")
        self.split_board    = import_image("resources", "images", "Split Board")

        # ── player icons ──────────────────────────────────────────────────
        # import_image_folder_dict gives {"Player1": surf, "Player2": surf, ...}
        self.player_icons = import_image_folder_dict("resources", "images", "Icons")
        # access as: self.player_icons["Player1"] etc

        # ── hud images ────────────────────────────────────────────────────
        self.hud_p1p2  = import_image("resources", "images", "Huds", "Hud1")
        self.hud_p2p1  = import_image("resources", "images", "Huds", "Hud4")
        self.hud_p1a1  = import_image("resources", "images", "Huds", "Hud2")
        self.hud_p1a2  = import_image("resources", "images", "Huds", "Hud3")
        self.hud_time  = import_image("resources", "images", "Huds", "HudTime")

        # ── turn banners ──────────────────────────────────────────────────
        self.turn_banner_you = import_image("resources", "images", "turn banner1")
        self.turn_banner_opp = import_image("resources", "images", "turn banner2")

        # ── control key icons ─────────────────────────────────────────────
        self.key_wasd  = import_image("resources", "images", "Instructions", "WASD")
        self.key_nums  = import_image("resources", "images", "Instructions", "Numbers")
        self.key_shift = import_image("resources", "images", "Instructions", "Shift")
        self.key_r     = import_image("resources", "images", "Instructions", "R")
        self.key_e     = import_image("resources", "images", "Instructions", "E")
        self.key_f     = import_image("resources", "images", "Instructions", "F")
        self.key_space = import_image("resources", "images", "Instructions", "Space")

        # ── placement labels ──────────────────────────────────────────────
        # each returns {"DestroyerStored": surf, "DestroyerPlaced": surf, ...}
        self.placement_labels = import_image_folder_dict("resources", "images", "Placement Labels")
        # access as: self.placement_labels["DestroyerStored"] etc

        # ── grid cell labels ──────────────────────────────────────────────
        self.grid_labels = import_image_folder_dict("resources", "images", "isometric tiles", "Grid Labels")
        # access as: self.grid_labels["Acell"], self.grid_labels["1cell"] etc

        # ── cursors ───────────────────────────────────────────────────────
        self.cursor_c = import_image("resources", "images", "isometric tiles", "cursorC")
        self.cursor_x = import_image("resources", "images", "isometric tiles", "cursorX")

        # ── sea tiles (animated, 3 frames each) ───────────────────────────
        # expects files named: sea unit.png, sea unit2.png, sea unit3.png etc
        # since they aren't numbered 1/2/3.png we load individually
        self.sea_tiles = [
            import_image("resources", "images", "isometric tiles", "sea unit"),
            import_image("resources", "images", "isometric tiles", "sea unit2"),
            import_image("resources", "images", "isometric tiles", "sea unit3"),
        ]
        self.sea_nohit_tiles = [
            import_image("resources", "images", "isometric tiles", "sea no_hit1"),
            import_image("resources", "images", "isometric tiles", "sea no_hit2"),
            import_image("resources", "images", "isometric tiles", "sea no_hit3"),
        ]
        self.sea_hit_tiles = [
            import_image("resources", "images", "isometric tiles", "sea hit1"),
            import_image("resources", "images", "isometric tiles", "sea hit2"),
            import_image("resources", "images", "isometric tiles", "sea hit3"),
        ]

        # ── boat tiles ────────────────────────────────────────────────────
        # individual loads since filenames aren't consistently numbered
        self.boat_tiles = {
            "destroyer": {
                "normal": [
                    import_image("resources", "images", "isometric tiles", "destroyer2"),
                    import_image("resources", "images", "isometric tiles", "destroyer1"),
                ],
                "hit":    import_image("resources", "images", "isometric tiles", "destroyerX"),
                "cursor": import_image("resources", "images", "isometric tiles", "destroyerC"),
            },
            "submarine": {
                "normal": [
                    import_image("resources", "images", "isometric tiles", "sub3"),
                    import_image("resources", "images", "isometric tiles", "sub2"),
                    import_image("resources", "images", "isometric tiles", "sub1"),
                ],
                "hit":    import_image("resources", "images", "isometric tiles", "subX"),
                "cursor": import_image("resources", "images", "isometric tiles", "subC"),
            },
            "cruiser": {
                "normal": [
                    import_image("resources", "images", "isometric tiles", "cruiser3"),
                    import_image("resources", "images", "isometric tiles", "cruiser2"),
                    import_image("resources", "images", "isometric tiles", "cruiser1"),
                ],
                "hit":    import_image("resources", "images", "isometric tiles", "cruiserX"),
                "cursor": import_image("resources", "images", "isometric tiles", "cruiserC"),
            },
            "battleship": {
                "normal": [
                    import_image("resources", "images", "isometric tiles", "bttlship4"),
                    import_image("resources", "images", "isometric tiles", "bttlship3"),
                    import_image("resources", "images", "isometric tiles", "bttlship2"),
                    import_image("resources", "images", "isometric tiles", "bttlship1"),
                ],
                "hit":    import_image("resources", "images", "isometric tiles", "bttlshipX"),
                "cursor": import_image("resources", "images", "isometric tiles", "bttlshipC"),
            },
            "carrier": {
                "normal": [
                    import_image("resources", "images", "isometric tiles", "carrier4"),
                    import_image("resources", "images", "isometric tiles", "carrier2"),
                    import_image("resources", "images", "isometric tiles", "carrier3"),
                    import_image("resources", "images", "isometric tiles", "carrier2"),  # note: original reused carrier2 for slot 4
                    import_image("resources", "images", "isometric tiles", "carrier1"),
                ],
                "hit":    import_image("resources", "images", "isometric tiles", "carrierX"),
                "cursor": import_image("resources", "images", "isometric tiles", "carrierC"),
            },
        }

        # ── sink animations ───────────────────────────────────────────────
        # import_image_sub_folders returns {"Destroyer1": [f1,f2,f3,f4,f5], "Destroyer2": [...], ...}
        self.sink_frames = {
            "destroyer":  import_image_sub_folders("resources", "images", "isometric tiles", "Sink Anims", "Destroyer"),
            "submarine":  import_image_sub_folders("resources", "images", "isometric tiles", "Sink Anims", "Submarine"),
            "cruiser":    import_image_sub_folders("resources", "images", "isometric tiles", "Sink Anims", "Cruiser"),
            "battleship": import_image_sub_folders("resources", "images", "isometric tiles", "Sink Anims", "battleship"),
            "carrier":    import_image_sub_folders("resources", "images", "isometric tiles", "Sink Anims", "carrier"),
        }
        # access as: self.sink_frames["destroyer"]["Destroyer1"][frame_idx]

        # ── blast door animation ───────────────────────────────────────────
        # expects files named 1.png through 8.png inside the folder... 
        # but your files are named blast_door1.png etc, so load individually
        self.blast_door_frames = import_image_folder("resources", "images", "Anims", "Blast Door")

        # ── explosion animation ───────────────────────────────────────────
        # files are named 1.png through 12.png so import_image_folder works
        self.explosion_frames = import_image_folder("resources", "images", "Anims", "Explosion")

        # ── splash animation ──────────────────────────────────────────────
        self.splash_frames = import_image_folder("resources", "images", "Anims", "Splash")
    
    def _load_sounds(self):
        # sfx imports
        # metal door sounds
        self.door_open_sfx = pygame.mixer.Sound(resource_path("resources/sounds/SFX/door open.mp3"))
        self.door_open_sfx.set_volume(0.75)
        self.door_close_sfx = pygame.mixer.Sound(resource_path("resources/sounds/SFX/door close.mp3"))
        self.door_close_sfx.set_volume(0.75)

        # startup sounds
        self.startup_sfx1 = pygame.mixer.Sound(resource_path("resources/sounds/SFX/Explosion1.wav"))
        self.startup_sfx1.set_volume(0.75)
        self.startup_sfx2 = pygame.mixer.Sound(resource_path("resources/sounds/SFX/Blip1.wav"))
        self.startup_sfx2.set_volume(0.75)
        self.music_unending = pygame.mixer.music.load(resource_path("resources/sounds/Music/unending.wav"))

        # button press sound 
        self.blip = pygame.mixer.Sound(resource_path(r"resources/sounds/SFX/Blip2.wav"))
        self.blip.set_volume(0.75)

        # boat placement sounds
        self.place_sfx1 = pygame.mixer.Sound(resource_path("resources/sounds/SFX/place.wav"))
        self.place_sfx1.set_volume(0.75)
        self.denyClick_sfx1 = pygame.mixer.Sound(resource_path("resources/sounds/SFX/DenyClick.wav"))
        self.denyClick_sfx1.set_volume(0.75)

        # boat sinking sound
        self.sink_sfx1 = pygame.mixer.Sound(resource_path("resources/sounds/SFX/Sink.wav"))
        self.sink_sfx1.set_volume(0.75)

        # boat hit (explosion) sounds
        self.explosion_sfx1 = pygame.mixer.Sound(resource_path("resources/sounds/SFX/Explosion1.wav"))
        self.explosion_sfx1.set_volume(0.75)
        self.explosion_sfx2 = pygame.mixer.Sound(resource_path("resources/sounds/SFX/Explosion2.wav"))
        self.explosion_sfx2.set_volume(0.75)
        self.explosion_sfx3 = pygame.mixer.Sound(resource_path("resources/sounds/SFX/Explosion3.wav"))
        self.explosion_sfx3.set_volume(0.75)
        self.explosion_sfx4 = pygame.mixer.Sound(resource_path("resources/sounds/SFX/Explosion4.wav"))
        self.explosion_sfx4.set_volume(0.75)

        # boat miss (splash) sounds
        self.splash_sfx1 = pygame.mixer.Sound(resource_path("resources/sounds/SFX/Splash.wav"))
        self.splash_sfx1.set_volume(0.75)
        self.splash_sfx2 = pygame.mixer.Sound(resource_path("resources/sounds/SFX/Splash2.wav"))
        self.splash_sfx2.set_volume(0.75)
        self.splash_sfx3 = pygame.mixer.Sound(resource_path("resources/sounds/SFX/Splash3.wav"))
        self.splash_sfx3.set_volume(0.75)
        self.splash_sfx4 = pygame.mixer.Sound(resource_path("resources/sounds/SFX/Splash4.wav"))
        self.splash_sfx4.set_volume(0.75)
        self.splash_sfx5 = pygame.mixer.Sound(resource_path("resources/sounds/SFX/Splash5.wav"))
        self.splash_sfx5.set_volume(0.75)