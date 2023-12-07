from pyzbar import pyzbar
import cv2
import time

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error al abrir la cámara.")

last_barcode = None
last_detection_time = 0
cooldown = 3  # 3 segundos de cooldown

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        barcodes = pyzbar.decode(frame)
        for barcode in barcodes:
            barcodeData = barcode.data.decode("utf-8")

            # Comprueba si el código de barras es el mismo que el último y si está dentro del tiempo de cooldown
            if barcodeData != last_barcode or (time.time() - last_detection_time) > cooldown:
                last_barcode = barcodeData
                last_detection_time = time.time()

                (x, y, w, h) = barcode.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                
                barcodeType = barcode.type
                text = "{} ({})".format(barcodeData, barcodeType)
                cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

                print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))

        cv2.imshow('Frame', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
