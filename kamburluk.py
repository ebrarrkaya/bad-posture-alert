import cv2
import mediapipe as mp
import numpy as np
from PIL import Image, ImageFont, ImageDraw
from pygame import mixer

cam = cv2.VideoCapture(1)
pose = mp.solutions.pose
vucut = pose.Pose()
font = ImageFont.truetype("opencv/fonts/CALIBRI.TTF", 32)
mixer.init()
mixer.music.load("opencv/kamburlukkontrol/uyari.mp3")
x = True
right = None
left = None

while True:
    ret, goruntu = cam.read()
    if not ret:
        break
    goruntu = cv2.flip(goruntu, 1)
    goruntu = cv2.resize(goruntu, (1000, 800))
    h, w, _ = goruntu.shape
    rgb = cv2.cvtColor(goruntu, cv2.COLOR_BGR2RGB)
    algilama = vucut.process(rgb)
    if algilama.pose_landmarks:
        noktalar = algilama.pose_landmarks.landmark
        lshoulder, lhip = noktalar[11], noktalar[23]
        rshoulder, rhip = noktalar[12], noktalar[24]

        lshoulder_x, lshoulder_y = int(lshoulder.x*w), int(lshoulder.y*h)
        rshoulder_x, rshoulder_y = int(rshoulder.x*w), int(rshoulder.y*h)
        lhip_x, lhip_y = int(lhip.x*w), int(lhip.y*h)
        rhip_x, rhip_y = int(rhip.x*w), int(rhip.y*h)

        rmesafe = rhip_y - rshoulder_y
        lmesafe = lhip_y - lshoulder_y

        pil = Image.fromarray(cv2.cvtColor(goruntu, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(pil)

        if rmesafe > lmesafe:
            right = True
            left = False
        elif rmesafe < lmesafe:
            left = True
            right = False

        if rmesafe <= 255 and right:
            if not mixer.music.get_busy() and x:
                x = False
                mixer.music.play()
            draw.text((30, 40), "Duruş bozukluğu algılandı. Lütfen dik durun!", font=font, fill=(255, 0, 0))
        elif lmesafe <= 255 and left:
            if not mixer.music.get_busy() and x:
                x = False
                mixer.music.play()
            draw.text((30,40), "Duruş bozukluğu algılandı. Lütfen dik durun!", font=font, fill=(255, 0, 0))
        else:
            x = True
            mixer.music.stop()
            if right:
                draw.text((30, 40), f"Sol Profil Mesafe: {rmesafe}px", font=font, fill=(255,0,255))
            elif left:
                draw.text((30, 40), f"Sağ Profil Mesafe: {lmesafe}px", font=font, fill=(0,0,255))

        goruntu = cv2.cvtColor(np.array(pil), cv2.COLOR_RGB2BGR)
        if right:
            cv2.line(goruntu, (rshoulder_x, rshoulder_y), (rhip_x, rhip_y), (255,0,255), 2)
            cv2.circle(goruntu, (rshoulder_x, rshoulder_y), 10, (255,128,255), -1)
            cv2.circle(goruntu, (rhip_x, rhip_y), 10, (255,128,255), -1)
        elif left:
            cv2.line(goruntu, (lshoulder_x, lshoulder_y), (lhip_x, lhip_y), (255,0,0), 2)
            cv2.circle(goruntu, (lshoulder_x, lshoulder_y), 10, (255,128,0), -1)
            cv2.circle(goruntu, (lhip_x, lhip_y), 10, (255,128,0), -1)
    cv2.imshow("Durus Bozuklugu Kontrolu", goruntu)
    if cv2.waitKey(1) == 27:
        break
cam.release()
cv2.destroyAllWindows()
