import cv2
import numpy as np

# Haar Cascade Modell laden
face_cascade = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')

# DNN Modell laden
dnn_net = cv2.dnn.readNetFromCaffe(
    'models/deploy.prototxt',
    'models/res10_300x300_ssd_iter_140000.caffemodel'
)

def detect_faces(frame):
    # Haar Cascade Erkennung
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # DNN Erkennung
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0))
    dnn_net.setInput(blob)
    detections = dnn_net.forward()
    
    return faces, detections

def draw_results(frame, faces, detections):
    (h, w) = frame.shape[:2]
    
    # Haar Cascade Ergebnisse zeichnen
    for (x, y, w, h) in faces:
        cv2.circle(frame, (x + w//2, y + h//2), w//2, (0, 255, 0), 2)
        cv2.putText(frame, "Gesicht (Haar)", (x, y-10),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # DNN Ergebnisse zeichnen
    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        
        if confidence > 0.5:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            # Rechteck zeichnen
            cv2.rectangle(frame, (startX, startY), (endX, endY), (255, 0, 0), 2)
            cv2.putText(frame, "Gesicht (DNN)", (startX, startY-10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

def main():
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        faces, detections = detect_faces(frame)
        draw_results(frame, faces, detections)
        
        cv2.imshow('Gesichtserkennung', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
