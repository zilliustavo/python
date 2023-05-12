from PIL import ImageGrab # pip install pillow
import pyautogui

def isCollision(data):

    for i in range(760, 835):
        for j in range(290, 330):
            if data[i, j] < 100:
                pyautogui.keyDown("up")
                print("pulando")
                return
    return

if __name__ == "__main__":
    
    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollision(data)
