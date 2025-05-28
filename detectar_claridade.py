import cv2
import numpy as np

def detectar_claridade():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # cv2.CAP_DSHOW resolve bugs no Windows

    if not cap.isOpened():
        print("❌ Erro: Webcam não encontrada.")
        return

    print("🟢 Pressione 'q' para sair.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Falha ao capturar imagem.")
            break

        frame = cv2.resize(frame, (640, 480))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        brilho_medio = np.mean(gray)

        LIMIAR_ESCURO = 60
        estado = "Claro" if brilho_medio > LIMIAR_ESCURO else "Escuro"

        cor = (0, 255, 0) if estado == "Claro" else (0, 0, 255)
        cv2.putText(frame, f"Ambiente: {estado}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, cor, 2)

        cv2.imshow("💡 Detecção de Claridade", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("🛑 Encerrando...")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detectar_claridade()
