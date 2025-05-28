import cv2
import numpy as np

def detectar_claridade():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Erro: Webcam não encontrada.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Redimensiona pra performance
        frame = cv2.resize(frame, (640, 480))

        # Converte pra escala de cinza
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Calcula brilho médio
        brilho_medio = np.mean(gray)

        # Define limiar (ajustável)
        LIMIAR_ESCURO = 60
        estado = "Claro" if brilho_medio > LIMIAR_ESCURO else "Escuro"

        # Mostra o estado na tela
        cv2.putText(frame, f"Ambiente: {estado}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0) if estado == "Claro" else (0,0,255), 2)
        cv2.imshow("Detecção de Claridade", frame)

        # Sai com 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detectar_claridade()
