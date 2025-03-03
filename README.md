# Gesichtserkennung

Ein Python-Programm zur Gesichtserkennung mit OpenCV.

## ✨Funktionen

- Verwendet zwei verschiedene Modelle:
  - Haar Cascade
  - Deep Neural Network (DNN)
- Zeichnet Kreise um erkannte Gesichter
- Beschriftet Gesichter auf Deutsch
- Beenden mit der Taste 'q'

## 📁Voraussetzungen

- Python 3.13.2
- OpenCV
- NumPy

## 🛠️Installation

1. Repository klonen:

   ```bash
   git clone https://github.com/Changlai-Bao/Gesichtserkennung
   ```

2. Abhängigkeiten installieren:

   ```bash
   python -m venv .venv
   pip install -r requirements.txt
   ```

3. Modelle herunterladen:
   - [haarcascade_frontalface_default.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)
   - [deploy.prototxt](https://github.com/opencv/opencv/blob/master/samples/dnn/face_detector/deploy.prototxt)
   - [res10_300x300_ssd_iter_140000.caffemodel](https://github.com/opencv/opencv_3rdparty/raw/dnn_samples_face_detector_20170830/res10_300x300_ssd_iter_140000.caffemodel)

4. Modelle in den `src/models`-Ordner kopieren

## 🚀Verwendung

```bash
python src/main.py
```

## 📜Lizenz

Dieses Projekt steht unter [MIT License](LICENSE)

## 📫Kontakt

- 📧 Email: [changlai.bao@outlook.com](mailto:changlai.bao@outlook.com)
- 🐙 GitHub: [Changlai-Bao](https://github.com/Changlai-Bao)
- 🌐 Webseit: [https://Changlai-Bao.github.io](https://Changlai-Bao.github.io)
