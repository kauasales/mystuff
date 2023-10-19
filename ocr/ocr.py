import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def pre_processamento():
    img = cv2.imread("placa12.jpg")

    img_resize = cv2.resize(img, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)

    img_cinza = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)

    # Calcule a média da luminosidade em escala de cinza
    average_luminosity = np.mean(img_cinza)

    # Calcule o valor máximo da luminosidade em escala de cinza
    max_luminosity = np.max(img_cinza)

    print(f'Média da luminosidade: {average_luminosity}')
    print(f'Máxima luminosidade: {max_luminosity}')

    if average_luminosity > 170:
        _, img_binary = cv2.threshold(img_cinza, average_luminosity-20, 255, cv2.THRESH_BINARY)
    
    if average_luminosity < 170:
        _, img_binary = cv2.threshold(img_cinza, average_luminosity-10, 255, cv2.THRESH_BINARY)

    if average_luminosity < 130:
        _, img_binary = cv2.threshold(img_cinza, average_luminosity+32, 255, cv2.THRESH_BINARY)


    '''if 100<average_luminosity<110: 
        _, img_binary = cv2.threshold(img_cinza, 150, 255, cv2.THRESH_BINARY)

    elif 110<=average_luminosity<120:
         _, img_binary = cv2.threshold(img_cinza, 150, 255, cv2.THRESH_BINARY)
 
    elif 120<=average_luminosity<130:
         _, img_binary = cv2.threshold(img_cinza, 150, 255, cv2.THRESH_BINARY)
       
    elif 130<=average_luminosity<140:
         _, img_binary = cv2.threshold(img_cinza, 150, 255, cv2.THRESH_BINARY)
        
    elif 140<=average_luminosity<150:
         _, img_binary = cv2.threshold(img_cinza, 150, 255, cv2.THRESH_BINARY)
               
    elif 150<=average_luminosity<160:
         _, img_binary = cv2.threshold(img_cinza, 150, 255, cv2.THRESH_BINARY)
                      
    elif 160<average_luminosity<170:
         _, img_binary = cv2.threshold(img_cinza, 150, 255, cv2.THRESH_BINARY)
       
    elif 170<=average_luminosity<180:
         _, img_binary = cv2.threshold(img_cinza, 157, 255, cv2.THRESH_BINARY) ##
       
    elif 180<=average_luminosity<190:
         _, img_binary = cv2.threshold(img_cinza, 150, 255, cv2.THRESH_BINARY)
       
    elif 190<=average_luminosity<200:
         _, img_binary = cv2.threshold(img_cinza, 175, 255, cv2.THRESH_BINARY) ##
       
    elif 200<=average_luminosity<210:
         _, img_binary = cv2.threshold(img_cinza, 150, 255, cv2.THRESH_BINARY)
               
    elif 210<=average_luminosity<220:
         _, img_binary = cv2.threshold(img_cinza, 150, 255, cv2.THRESH_BINARY)
               
    elif 220<=average_luminosity<230:
         _, img_binary = cv2.threshold(img_cinza, 150, 255, cv2.THRESH_BINARY)
               
    elif 230<=average_luminosity<240:
         _, img_binary = cv2.threshold(img_cinza, 150, 255, cv2.THRESH_BINARY)

    elif 240<=average_luminosity<250:
         _, img_binary = cv2.threshold(img_cinza, 150, 255, cv2.THRESH_BINARY)
                           
    elif average_luminosity>250:
         _, img_binary = cv2.threshold(img_cinza, 200, 255, cv2.THRESH_BINARY)'''
    
    cv2.imwrite("img_ocr.png", img_binary)


    cv2.imshow("", img_binary)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def ocr():

    img_roi = cv2.imread('img_ocr.png')

    config = r'-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 --psm 6'

    saida = pytesseract.image_to_string(img_roi, config=config)

    print(saida)

pre_processamento()
ocr()