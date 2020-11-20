from pygame import mixer

mixer.init()

def playMusic():
    mixer.music.load("D:\\baban\\pythonworks\\game_assets\\SnakeGame\\snake_music.mp3")
    mixer.music.set_volume(1.0)
    mixer.music.play(-1)
    print("hjsdfk")

playMusic()