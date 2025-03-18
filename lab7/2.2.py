import pygame
import sys

pygame.init()
H = 800
W = 600

screen = pygame.display.set_mode((H, W))
pygame.display.set_caption("Spotify")

bg_color = (0, 0, 0)
fon = pygame.image.load("lab7/imagess/spotify.jpg")

songs = [
    "lab7/musiks/ARO,S.Ó.Seni.mp3",
    "lab7/musiks/cant hold us.mp3",
    "lab7/musiks/Heat waves .mp3",
    "lab7/musiks/INSTASAMKA,MONEYKEN LOVE.mp3",
    "lab7/musiks/MiyaGi,По Уши в Тебя Влюблен.mp3",
    "lab7/musiks/wake up.mp3"
]

current_track = 0  
paused = False
volume = 0.5  


def play_music():
    pygame.mixer.music.load(songs[current_track])
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()
    print(f" Сейчас играет: {songs[current_track]}")


play_music()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()

    
    if pressed[pygame.K_LEFT]:
        current_track = (current_track - 1) % len(songs)
        play_music()

    
    if pressed[pygame.K_RIGHT]:
        current_track = (current_track + 1) % len(songs)
        play_music()

    
    if pressed[pygame.K_SPACE]:
        if paused:
            pygame.mixer.music.unpause()
            print("▶️ Продолжение")
        else:
            pygame.mixer.music.pause()
            print(" Пауза")
        paused = not paused

    
    if pressed[pygame.K_s]:
        pygame.mixer.music.stop()
        print(" Остановлено")

    
    if pressed[pygame.K_UP]:
        volume = min(1.0, volume + 0.1)
        pygame.mixer.music.set_volume(volume)
        print(f"Громкость: {int(volume * 100)}%")

    
    if pressed[pygame.K_DOWN]:
        volume = max(0.0, volume - 0.1)
        pygame.mixer.music.set_volume(volume)
        print(f" Громкость: {int(volume * 100)}%")

    screen.fill(bg_color)
    screen.blit(fon, (0, 0))
    pygame.display.flip()

pygame.quit()
sys.exit() 