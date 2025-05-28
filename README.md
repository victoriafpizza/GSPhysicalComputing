# GS Physical Computing

# Detector de Claridade 🚀

![Arduino](https://img.shields.io/badge/Platform-Arduino-blue?style=flat&logo=arduino)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Descrição

Resumo direto do projeto:  
- Criar um sistema que identifica a condição de luminosidade do ambiente capturada pela webcam. Ele pode ser utilizado em soluções de emergência, monitoramento ou segurança durante falhas de energia.
---

## ⚙️ Componentes Utilizados

- Python 3.10+
- OpenCV.

---

## 🔧 Como Usar

1. Clone o repositório:

```bash
git clone https://github.com/seuusuario/nome-do-repo.git
cd nome-do-repo

2. Instale as dependências:

bash
Copiar
Editar
pip install opencv-python

3. Execute o projeto

python detectar_claridade.py

---

## Funcionamento
- A webcam é ativada e a média da luminosidade da imagem é analisada.
- O sistema exibe na tela se o ambiente está "Claro" ou "Escuro", com base em um limiar ajustável.
