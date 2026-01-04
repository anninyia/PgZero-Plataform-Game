# Author: Anna Victória
# Project: PgZero Platform Test Game
# Dear developer, feel free to modify and expand this code as needed! Also, I didn't finished it, but I added some comments to help u to understand the code better :), enjoy!
# Music and jump sound by Toby Fox for Deltarune

WIDTH = 800
HEIGHT = 450
TITLE = "PgZero Platform Game Test"

import random
from pygame import Rect

# ======================
# * GAME STATES
# ======================
STATE_MENU = "menu"
STATE_PLAY = "play"

game_state = STATE_MENU
sound_enabled = True


# ======================
# * UI BUTTONS
# ======================
start_button = Rect(300, 150, 200, 50)
sound_button = Rect(300, 220, 200, 50)
exit_button = Rect(300, 290, 200, 50)


# ======================
# * ANIMATION CLASS
# ======================
class Animation:
    def __init__(self, frames, speed):
        self.frames = frames
        self.speed = speed
        self.index = 0.0

    def update(self):
        self.index += self.speed
        if self.index >= len(self.frames):
            self.index = 0.0

    def image(self):
        return self.frames[int(self.index)]


# ======================
# * HERO CLASS
# ======================
class Hero:
    def __init__(self):
        self.actor = Actor("hero_idle_0", (100, 350))
        self.vx = 0
        self.vy = 0
        self.on_ground = False

        self.idle_anim = Animation(
            ["hero_idle_0", "hero_idle_1"], 0.08
        )
        self.walk_anim = Animation(
            ["hero_walk_0", "hero_walk_1"], 0.15
        )

    def update(self):
        # gravity
        self.vy += 0.5
        self.actor.y += self.vy
        self.actor.x += self.vx

        # ground collision
        if self.actor.y >= 350:
            self.actor.y = 350
            self.vy = 0
            self.on_ground = True
        else:
            self.on_ground = False

        # animation
        if self.vx == 0:
            self.idle_anim.update()
            self.actor.image = self.idle_anim.image()
        else:
            self.walk_anim.update()
            self.actor.image = self.walk_anim.image()


# ======================
# * ENEMY CLASS
# ======================
class Enemy:
    def __init__(self, x, left, right):
        self.actor = Actor("enemy_idle_0", (x, 350))
        self.left = left
        self.right = right
        self.speed = random.choice([-1, 1])

        self.walk_anim = Animation(
            ["enemy_walk_0", "enemy_walk_1"], 0.1
        )

    def update(self):
        self.actor.x += self.speed

        if self.actor.x <= self.left or self.actor.x >= self.right:
            self.speed *= -1

        self.walk_anim.update()
        self.actor.image = self.walk_anim.image()


# ======================
# * GAME OBJECTS
# ======================
hero = Hero()

enemies = [
    Enemy(400, 350, 550),
    Enemy(650, 600, 750),
]


# ======================
# * SOUND & MUSIC
# ======================
def play_sound(name):
    if sound_enabled:
        try:
            getattr(sounds, name).play()
        except AttributeError:
            print(f"Sound '{name}' not found")


def play_music():
    if sound_enabled and not music.is_playing("music"):
        music.play("music")


# ======================
# * INPUT
# ======================
def on_key_down(key):
    if game_state != STATE_PLAY:
        return

    if key == keys.SPACE and hero.on_ground:
        hero.vy = -10
        play_sound("jump")


def on_key_up(key):
    if key in (keys.A, keys.D):
        hero.vx = 0


def on_mouse_down(pos):
    global game_state, sound_enabled

    if game_state == STATE_MENU:
        if start_button.collidepoint(pos):
            game_state = STATE_PLAY
            play_music()

        elif sound_button.collidepoint(pos):
            sound_enabled = not sound_enabled
            if not sound_enabled:
                music.stop()
            else:
                play_music()

        elif exit_button.collidepoint(pos):
            quit()


# ======================
# * UPDATE LOOP
# ======================
def update():
    if game_state == STATE_PLAY:
        hero.vx = 0
        if keyboard.a:
            hero.vx = -3
        elif keyboard.d:
            hero.vx = 3

        hero.update()

        for enemy in enemies:
            enemy.update()
            if hero.actor.colliderect(enemy.actor):
                reset_game()


# ======================
# * DRAW
# ======================
def draw():
    screen.clear()

    if game_state == STATE_MENU:
        draw_menu()
    else:
        screen.blit("background", (0, 0))
        hero.actor.draw()
        for enemy in enemies:
            enemy.actor.draw()


def draw_menu():
    screen.fill((30, 30, 40))
    screen.draw.text("PLATFORMER TEST", center=(400, 80), fontsize=48)

    screen.draw.filled_rect(start_button, (70, 130, 180))
    screen.draw.filled_rect(sound_button, (70, 130, 180))
    screen.draw.filled_rect(exit_button, (180, 70, 70))

    screen.draw.text("Start Game", center=start_button.center, fontsize=30)
    sound_text = "Sound: ON" if sound_enabled else "Sound: OFF"
    screen.draw.text(sound_text, center=sound_button.center, fontsize=30)
    screen.draw.text("Exit", center=exit_button.center, fontsize=30)


# ======================
# *RESET
# ======================
def reset_game():
    global hero
    hero = Hero()
