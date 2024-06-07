# importação da opencv-python
import cv2
import os
from functions import getAllContours

# configuração da captura da webcam
webcam = cv2.VideoCapture(0)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

# definição da constante home
HOME = os.getcwd()
print(f'Repositório atual: {HOME}')

# loop de repetição para captura de fotos
while True:
    
    ret, frame = webcam.read()
    
    contours = getAllContours(frame)
    
    biggest_contour = max(contours, key=cv2.contourArea) if contours else None

    # Optional: Draw the biggest contour on the original image
    if biggest_contour is not None:
        # Get bounding rectangle of the contour
        x, y, w, h = cv2.boundingRect(biggest_contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # for contour in contours:
    # cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
    
    cv2.imshow("webcam", frame)
    
    k = cv2.waitKey(1)
    if k%256==ord('q'):
        print("Janela de captura finalizada")
        break

webcam.release()
cv2.destroyAllWindows()