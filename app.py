import streamlit as st
import numpy as np
import cv2
from PIL import Image
import plotly.graph_objects as go

# -----------------------------
# MÓDULOS VISÃO
# -----------------------------
from vision.pupil_distance import monocular_pd
from vision.pupil_detection import detect_pupil
from vision.face_mesh import detect_face

# -----------------------------
# EXAMES
# -----------------------------
from exams.vision_test import vision_test
from exams.cornea_map import generate_cornea_map

# -----------------------------
# MODELOS DE IA (placeholders)
# -----------------------------
from ai_models.myopia_model import predict_myopia
from ai_models.dry_eye_classifier import classify_dry_eye
from ai_models.keratoconus_detector import detect_keratoconus

# -----------------------------
# CLÍNICA / RELATÓRIO
# -----------------------------
# from clinic.database import save_patient
from reports.pdf_report import generate_report  # precisa do reportlab

# -----------------------------
# UTILITÁRIOS
# -----------------------------
calculate_pd = monocular_pd

# Funções placeholders
def estimate_refraction(frame):
    return {"sphere": -1.25, "cylinder": -0.50, "axis": 90}

def detect_strabismus(left_pupil, right_pupil):
    return False

def generate_cornea_surface():
    X, Y = np.meshgrid(np.linspace(-1,1,50), np.linspace(-1,1,50))
    Z = np.sin(X**2 + Y**2)
    return X, Y, Z

def load_image(foto):
    img = Image.open(foto)
    frame = np.array(img)
    return cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

# -----------------------------
# CONFIG STREAMLIT
# -----------------------------
st.set_page_config(page_title="Optometry AI Lab", layout="centered")
st.title("👁️ Optometry AI Lab")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Captura",
        "Distância Pupilar",
        "Teste de Visão",
        "Topografia Corneana",
        "Autorrefrator",
        "Exame Ocular IA",
        "Topografia 3D",
        "IA Ocular",
        "Paciente / Laudo"
    ]
)

# -----------------------------
# FUNÇÕES DE CADA MENU
# -----------------------------
def captura_menu():
    foto = st.camera_input("Capture o rosto")
    if foto:
        image = Image.open(foto)
        st.image(image)
        st.success("Imagem capturada")

def distancia_pupilar_menu():
    foto = st.camera_input("Capture o rosto")
    if foto:
        frame = load_image(foto)
        h, w, _ = frame.shape
        results = detect_face(frame)
        if results.multi_face_landmarks:
            landmarks = results.multi_face_landmarks[0].landmark
            # ⚡ Corrigido: usar .x e .y
            pd = calculate_pd(
                (landmarks[0].x * w, landmarks[0].y * h),
                (landmarks[1].x * w, landmarks[1].y * h)
            )
            st.success(f"DP estimada: {pd:.2f} mm")
        st.image(foto)

def teste_visao_menu():
    st.header("Teste de Visão")
    result = vision_test()
    if result:
        st.write("Resultado:", result)

def topografia_corneana_menu():
    if st.button("Gerar mapa corneano"):
        curvature, map_data = generate_cornea_map()
        st.write("Curvatura média:", round(curvature,2))
        st.dataframe(map_data)

def autorrefrator_menu():
    st.header("Autorrefrator")
    
    # Placeholders
    foto_placeholder = st.empty()        # Para o input da câmera
    resultado_placeholder = st.empty()   # Para mostrar resultados

    # Captura da foto
    foto = foto_placeholder.camera_input("Capture os olhos")
    if foto:
        # Carrega e converte a imagem
        frame = load_image(foto)

        # Estima refração (função fictícia)
        result = estimate_refraction(frame)

        # Mostra resultados no placeholder
        resultado_placeholder.write(f"Esférico: {result['sphere']}")
        resultado_placeholder.write(f"Cilíndrico: {result['cylinder']}")
        resultado_placeholder.write(f"Eixo: {result['axis']}")

def exame_ocular_ia_menu():
    st.header("Exame Ocular IA")

    # Placeholders
    foto_placeholder = st.empty()
    resultado_placeholder = st.empty()

    foto = foto_placeholder.camera_input("Capture os olhos")
    if foto:
        frame = load_image(foto)
        pupils = detect_pupil(frame)

        if len(pupils) >= 2:
            st.warning("Não foi possível detectar duas pupilas. Tente novamente com luz melhor ou mais próxima da câmera.")
            pd = monocular_pd(pupils[0], pupils[1])
            resultado_placeholder.write(f"DP: {round(pd, 2)} mm")

            if detect_strabismus(pupils[0], pupils[1]):
                resultado_placeholder.warning("Possível estrabismo")
        else:
            resultado_placeholder.warning("Não foram detectadas duas pupilas")

def topografia_3d_menu():
    X, Y, Z = generate_cornea_surface()
    fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])
    st.plotly_chart(fig)

def ia_ocular_menu():
    st.subheader("Placeholders de IA ocular")
    blink_rate = st.slider("Taxa de piscar", 0, 30, 10)
    st.write("Classificação olho seco (simulada)")
    
    curvature = st.slider("Curvatura corneana", 40.0, 50.0, 44.0)
    st.write("Detecção ceratocone (simulada)")

def paciente_laudo_menu():
    name = st.text_input("Nome do paciente")
    if st.button("Gerar laudo"):
        file = generate_report(name, 63, "-1.25")
        st.success("Laudo gerado")
        with open(file, "rb") as f:
            st.download_button("Baixar PDF", f, file_name=file)

# -----------------------------
# MENU PRINCIPAL
# -----------------------------
menu_functions = {
    "Captura": captura_menu,
    "Distância Pupilar": distancia_pupilar_menu,
    "Teste de Visão": teste_visao_menu,
    "Topografia Corneana": topografia_corneana_menu,
    "Autorrefrator": autorrefrator_menu,
    "Exame Ocular IA": exame_ocular_ia_menu,
    "Topografia 3D": topografia_3d_menu,
    "IA Ocular": ia_ocular_menu,
    "Paciente / Laudo": paciente_laudo_menu
}

# Executa a função correspondente ao menu
menu_functions[menu]()