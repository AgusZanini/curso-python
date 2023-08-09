import cv2
import face_recognition as fr

# cargar imagenes
foto_control = fr.load_image_file("fotoA.jpg")
foto_prueba = fr.load_image_file("fotoD.jpg")

# pasar imagenes a rgb
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# localizar caara control
lugar_cara_A = fr.face_locations(foto_control)[0]
cara_codificada_A = fr.face_encodings(foto_control)[0]

# localizar cara prueba
lugar_cara_b = fr.face_locations(foto_prueba)[0]
cara_codificada_B = fr.face_encodings(foto_prueba)[0]

# mostar rectangulo A
cv2.rectangle(foto_control,
              (lugar_cara_A[3], lugar_cara_A[0]),
              (lugar_cara_A[1], lugar_cara_A[2]),
              (0, 255, 0),
              2)

# mostrar rectangulo B
cv2.rectangle(foto_prueba,
              (lugar_cara_b[3], lugar_cara_b[0]),
              (lugar_cara_b[1], lugar_cara_b[2]),
              (0, 255, 0),
              2)

# medida de la distancia
distancia = fr.face_distance([cara_codificada_A], cara_codificada_B)

# realizar comparacion
resultado = fr.compare_faces([cara_codificada_A], cara_codificada_B)  # pasamos una lista de imagenes,
# en nuestro caso tenemos solo una imagen

# mostrar resultados
cv2.putText(foto_prueba,
            f"{resultado} {distancia.round(2)}",  # que voy a mostrar
            (25, 25),  # ubicacion
            cv2.FONT_HERSHEY_COMPLEX,  # fuente de texto
            0.5,  # escala
            (0, 255, 0),  # color
            2)  # grosor

# mostrar imagenes
cv2.imshow("Foto Control", foto_control)
cv2.imshow("Foto Prueba", foto_prueba)

cv2.waitKey(0)
