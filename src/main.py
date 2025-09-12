# Erforderliche Bibliotheken importieren
import cv2
import mediapipe as mp

# Initialisieren von MediaPipe Face Detection und Drawing Utilities
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# Zugriff auf die Webcam
# Die '0' steht normalerweise für die eingebaute Webcam.
cap = cv2.VideoCapture(0)

# Face Detection-Modell laden
# min_detection_confidence: Mindest-Konfidenzwert (0.0 bis 1.0)
with mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.5) as face_detection:

    # Endlosschleife, um Bilder von der Webcam kontinuierlich zu lesen
    while cap.isOpened():
        # Lese ein einzelnes Bild (Frame) von der Webcam
        success, image = cap.read()
        if not success:
            print("Bild von der Kamera konnte nicht gelesen werden.")
            break

        # Das Bild horizontal spiegeln, um eine intuitive Selbstansicht zu ermöglichen
        image = cv2.flip(image, 1)

        # Zur Leistungsverbesserung das Bild als nicht mehr beschreibbar markieren
        image.flags.writeable = False
        # Das Bild vom BGR-Format (OpenCV-Standard) in das RGB-Format konvertieren,
        # da MediaPipe RGB-Bilder erwartet.
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Das RGB-Bild mit MediaPipe verarbeiten, um Gesichter zu erkennen
        results = face_detection.process(image_rgb)

        # Das Bild wieder als beschreibbar markieren, damit wir darauf zeichnen können
        image.flags.writeable = True
        
        # Wenn Gesichter erkannt wurden
        if results.detections:
            # Durch alle erkannten Gesichter iterieren
            for detection in results.detections:
                # Zeichne die Erkennungs-Rechtecke auf das Bild
                mp_drawing.draw_detection(image, detection)

        # Zeige das resultierende Bild in einem Fenster an
        cv2.imshow('MediaPipe Gesichtserkennung', image)

        # Warte auf Tastendruck. Wenn 'q' gedrückt wird, beende die Schleife.
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

# Gib die Webcam-Ressource frei
cap.release()
# Schließe alle OpenCV-Fenster
cv2.destroyAllWindows()