# Detección de malla facial con OpenCV y MediaPipe

<span><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/></span>

Este script en Python utiliza las bibliotecas **OpenCV** y **MediaPipe** para detectar y visualizar los puntos de referencia (landmarks) faciales en tiempo real a través de la cámara web. Además, resalta puntos específicos de la malla facial.

## Requisitos

- Python 3.x
- OpenCV (`cv2`)
- MediaPipe

## Instalación

Antes de ejecutar el script, asegúrate de instalar las dependencias necesarias:

```bash
pip install opencv-python mediapipe
```

## Código

```python
import cv2 
import mediapipe as mp

# Inicialización de MediaPipe Face Mesh y utilidades de dibujo
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

# Lista de índices de landmarks faciales a resaltar
index_list = [70, 63, 105, 66, 107, 336, 296, 334, 293, 300,
              122, 196, 3, 51, 281, 248, 419, 351, 37, 0, 267]

# Iniciar la captura de video desde la cámara web (cambiar el índice si es necesario)
cap = cv2.VideoCapture(0)

# Configurar la ventana de visualización
cv2.namedWindow('Detección de Gestos', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Detección de Gestos', 800, 600)

# Configuración de MediaPipe Face Mesh
with mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=3,
    min_detection_confidence=0.5) as face_mesh:

    while cap.isOpened():
        # Capturar frame desde la cámara web
        ret, frame = cap.read()
        if not ret:
            break

        # Obtener dimensiones del frame y convertir a RGB
        height, width, _ = frame.shape
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Procesar la imagen para detectar rostros
        results = face_mesh.process(frame_rgb)

        # Si se detectan rostros, dibujar landmarks y conexiones
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # Dibujar puntos específicos
                for index in index_list:
                    x = int(face_landmarks.landmark[index].x * width)
                    y = int(face_landmarks.landmark[index].y * height)
                    cv2.circle(frame, (x, y), 2, (0, 0, 255), 5)

                # Dibujar la malla facial completa
                mp_drawing.draw_landmarks(
                    frame, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION)

        # Mostrar el frame procesado
        cv2.imshow("Detección de Gestos", frame)

        # Salir al presionar 'Esc'
        if cv2.waitKey(5) & 0xFF == 27:
            break

    # Liberar recursos
    cap.release()
    cv2.destroyAllWindows()
```

## Explicación paso a paso

1. **Importación de bibliotecas**: Se importan las bibliotecas necesarias para el procesamiento de imágenes y la detección de rostros.

2. **Inicialización de MediaPipe Face Mesh**: Se configura el modelo de malla facial de MediaPipe y las utilidades de dibujo.

3. **Definición de `index_list`**: Esta lista contiene los índices de los landmarks faciales que se desean resaltar específicamente en la visualización.

4. **Captura de video**: Se inicia la captura de video desde la cámara web. Si tienes múltiples cámaras, puede ser necesario cambiar el índice en `cv2.VideoCapture(0)`.

5. **Configuración de la ventana**: Se establece el nombre y el tamaño de la ventana donde se mostrará el video procesado.

6. **Bucle principal**: Mientras la cámara esté abierta, se capturan frames y se procesan.

   - **Lectura del frame**: Se lee el frame actual de la cámara.

   - **Conversión de color**: Se convierte el frame de BGR a RGB, ya que MediaPipe trabaja con imágenes RGB.

   - **Procesamiento con MediaPipe**: Se procesa el frame para detectar los landmarks faciales.

   - **Dibujo de landmarks**:

     - Se recorren los rostros detectados y se dibujan círculos en los puntos especificados en `index_list`.
     - Se dibuja la malla facial completa utilizando las utilidades de dibujo de MediaPipe.

   - **Visualización**: Se muestra el frame procesado en la ventana.

   - **Salida del bucle**: Si se presiona la tecla 'Esc', el bucle se rompe y se liberan los recursos.

7. **Liberación de recursos**: Al finalizar, se libera la captura de video y se cierran las ventanas abiertas.

## Notas

- **Cámara web**: Si el script no detecta la cámara correctamente, intenta cambiar el índice en `cv2.VideoCapture(0)` a otro número (por ejemplo, `cv2.VideoCapture(1)`).

- **Rendimiento**: La detección en tiempo real puede ser exigente para la CPU. Si experimentas retrasos, considera reducir la resolución del video o limitar el número de rostros detectados.

- **Personalización**: Puedes modificar `index_list` para resaltar diferentes puntos de la malla facial según tus necesidades.

## Ejecución

Para ejecutar el script, utiliza el siguiente comando en tu terminal:

```bash
python nombre_del_script.py
```

## Captura:
<span><img src="https://github.com/VintaBytes/Deteccion-de-malla-facial-con-OpenCV-y-MediaPipe/blob/main/cara1.png"/></span>


## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.
