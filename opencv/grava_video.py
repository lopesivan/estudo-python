import cv2
import time

# Configurações do vídeo
VIDEO_DEVICE_INDEX = 0  # Índice do dispositivo de vídeo (pode precisar ser ajustado)
VIDEO_WIDTH = 640
VIDEO_HEIGHT = 480
VIDEO_FPS = 30

# Inicializa a captura de vídeo
cap = cv2.VideoCapture(VIDEO_DEVICE_INDEX)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, VIDEO_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, VIDEO_HEIGHT)
cap.set(cv2.CAP_PROP_FPS, VIDEO_FPS)

# Inicia a gravação do vídeo
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Define o codec de vídeo
filename = f'video_{time.time()}.avi'  # Define o nome do arquivo de vídeo
out = cv2.VideoWriter(filename, fourcc, VIDEO_FPS, (VIDEO_WIDTH, VIDEO_HEIGHT))

# Grava o vídeo por 10 segundos
start_time = time.time()
while (time.time() - start_time) < 10.0:
    ret, frame = cap.read()
    if ret:
        out.write(frame)

# Encerra a captura e a gravação
cap.release()
out.release()

