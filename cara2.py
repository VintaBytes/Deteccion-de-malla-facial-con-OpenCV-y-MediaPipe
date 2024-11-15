import cv2 
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

index_list = [70, 63, 105, 66, 107, 336, 296, 334, 293, 300,
                122, 196, 3, 51, 281, 248, 419, 351, 37, 0, 267]

# Iniciar la captura de video desde la webcam (0 para la cámara integrada)
cap = cv2.VideoCapture(2)

# Establecer el tamaño de la ventana
cv2.namedWindow('Deteccion de gestos', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Deteccion de gestos', 800, 600)

with mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=3,
    min_detection_confidence=0.5) as face_mesh:

    while cap.isOpened():
        # Capturar frame desde la webcam
        ret, frame = cap.read()
        if not ret:
            # Error al capturar el frame.
            break

        height, width, _ = frame.shape
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Procesar la imagen para detectar rostros
        results = face_mesh.process(frame_rgb)

        # Dibujar landmarks en el rostro y líneas que los conectan si se detecta
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                for index in index_list:
                    x = int(face_landmarks.landmark[index].x * width)
                    y = int(face_landmarks.landmark[index].y * height)
                    cv2.circle(frame, (x, y), 2, (0, 0, 255), 5)

                # Dibujar líneas entre los landmarks
                mp_drawing.draw_landmarks(frame, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION)

        # Mostrar el frame con landmarks y líneas
        cv2.imshow("Deteccion de gestos", frame)

        # Salir con la tecla 'esc'
        if cv2.waitKey(5) & 0xFF == 27:
            break

    # Liberar la captura y cerrar la ventana al finalizar
    cap.release()
    cv2.destroyAllWindows()
