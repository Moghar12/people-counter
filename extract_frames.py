import cv2
import os

# Créer le dossier pour les images extraites
output_dir = 'frames'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Charger la vidéo
video_path = 'video.mp4'
cap = cv2.VideoCapture(video_path)

frame_rate = 1  # Extraire une image par seconde
frame_id = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Sauvegarder l'image toutes les 'frame_rate' secondes
    if frame_id % frame_rate == 0:
        filename = os.path.join(output_dir, f'output_{frame_id:04d}.png')
        cv2.imwrite(filename, frame)
    
    frame_id += 1

cap.release()
cv2.destroyAllWindows()
