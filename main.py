import pytesseract 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
import winsound
import numpy as np 
from PIL import ImageGrab, Image
import cv2
import time

last_time = time.time()

while(True):
    screen = np.array(ImageGrab.grab(bbox=(200, 100, 2150, 440)))

    text = pytesseract.image_to_string(screen)
    
    if ":" or ";" in text:
        print(text.strip())
        
    if "Nefarious" in text:
        winsound.Beep(2500, 1000)


    #cv2.imshow('window', new_image)
    cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    
    print(1/(time.time()-last_time))
    last_time = time.time()

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

