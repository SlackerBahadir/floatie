import PIL
from PIL import Image
import os
import sys

from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QSize, Qt

ACTIVE_CHARACTER = "cat"

def get_biggest_resulotion_state_image():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    character_states_dir = os.path.join(BASE_DIR, "..", "assets", "characters", ACTIVE_CHARACTER)
    character_states_dir_list = os.listdir(character_states_dir)
    
    resulotions = list()

    for state_dir in character_states_dir_list:
        state_images_dir = os.path.join(character_states_dir, state_dir)
        state_images_files = os.listdir(state_images_dir)
        for state_images in state_images_files:
            wid, hgt = Image.open(os.path.join(state_images_dir, state_images)).size
            
            resulotions.append((wid, hgt))
            
    return max(resulotions)
    
    
class Pet(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        screen = app.primaryScreen()
        screen_res = screen.size()
        
        image_wid, image_hgt = get_biggest_resulotion_state_image()
        
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.Tool)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        
        self.setFixedSize(image_wid, image_hgt)
        
app = QApplication(sys.argv)
window =  Pet()
