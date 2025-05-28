## Global Solution Physical Computing

# Detector de Claridade 🚀

![Arduino](https://img.shields.io/badge/Platform-Arduino-blue?style=flat&logo=arduino)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

---

<h1 align="center">💡 Detector de Claridade com Python + OpenCV</h1>

<p align="center">
  🔦 Uma solução simples, eficiente e sem sensores físicos para detectar se o ambiente está <strong>claro</strong> ou <strong>escuro</strong>. Ideal para situações de emergência, automação e monitoramento.
</p>

---

<p align="center">
  Desenvolvido por <strong> Victoria Franceschini Pizza e Eric de Carvalho Rodrigues </strong> 
</p>

<p align="center">
  <strong> RM 550609 | RM 550249 </strong> 
</p>

<p align="center">
  <img src="https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/-OpenCV-5C3EE8?logo=opencv&logoColor=white" />
  <img src="https://img.shields.io/badge/-MediaPipe-FF6F00?logo=google&logoColor=white" />
  <img src="https://img.shields.io/badge/-Feito%20com%20cafe-6f4e37?logo=buymeacoffee&logoColor=white" />
</p>


---

## 🧠 Sobre o Projeto

Este projeto foi desenvolvido como uma proposta de solução para cenários onde a detecção da luminosidade ambiental é crucial, como durante quedas de energia, automações domésticas ou suporte a pessoas com deficiência visual.

Através da captura de vídeo pela webcam e análise da média de luminosidade dos frames, o sistema determina em tempo real se o ambiente está **claro** ou **escuro**.

---

## 🚀 Tecnologias Utilizadas

- 🐍 **Python 3.10+**
- 🎥 **OpenCV**

---

## 🔍 Descrição do Problema

Em situações de queda de energia (apagões), é comum não saber imediatamente se o ambiente está escuro por um problema externo (falta de luz) ou interno (lâmpadas desligadas, sensores fora do ar, etc.). Isso pode ser crítico em ambientes que dependem de iluminação constante, como laboratórios, residências inteligentes ou espaços de trabalho.

Além disso, é importante oferecer uma resposta visual clara que informe rapidamente o estado atual do ambiente — se está iluminado normalmente ou se está em condição de escuridão potencialmente causada por um apagão.

---

## Visão Geral da Solução

Este projeto implementa um sistema simples e eficaz para **detecção em tempo real da claridade do ambiente**, utilizando:

- 📷 **OpenCV** para captura da imagem via webcam
- 🧠 **MediaPipe** (em versões futuras) para fusão com sensores ou interfaces visuais
- 📊 **Análise de brilho médio** para classificação binária: `Claro` ou `Escuro`

### ✅ Comportamento:

- Em tempo real, o sistema avalia o **nível de luz** capturado pela webcam.
- Exibe na tela a mensagem:
  - 🟢 “Ambiente: Claro” quando a luz está adequada.
  - 🔴 “Ambiente: Escuro” quando o local está muito escuro (potencialmente um apagão).
- Permite sair pressionando a tecla `q`.

## 🎯 Funcionalidades

- ✅ Detecção de luminosidade do ambiente em tempo real
- ✅ Interface simples com exibição do status: **"Claro"** ou **"Escuro"**
- ✅ Não necessita de sensores externos — usa apenas a câmera
- ✅ Código leve e fácil de executar

---

[![Vídeo de Demonstração](https://img.shields.io/badge/🔗-Assista%20ao%20Vídeo-blue?style=for-the-badge)](LINK_DO_VIDEO_AQUI)

---
## Como Rodar o Projeto

### 1️⃣ Clone este repositório

git clone https://github.com/victoriafpizza/GSPhysicalComputing.git
cd GSPhysicalComputing

---

### 2️⃣ Instale as dependencias
pip install opencv-python

---

### 3️⃣ Execute o programa
python detectar_claridade.py

---