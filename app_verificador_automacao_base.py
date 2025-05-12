import streamlit as st
import pandas as pd

st.set_page_config(page_title="Detector de Anúncios no YouTube", page_icon="🎯")

st.title("🎯 Detector de Anúncios no YouTube")
st.markdown("Este app ajuda você a verificar se vídeos do YouTube exibem anúncios e são segmentáveis no Google Ads.")

tab1, tab2 = st.tabs(["🔗 Verificador individual", "📂 Verificador em lote (CSV)"])

def verificar_video(video_url):
    # ⚠️ Aqui entraria o código Selenium real
    # Placeholder para simular o funcionamento automático
    return "🟢 Provavelmente monetizado (simulação)"

with tab1:
    video_url = st.text_input("Cole o link do vídeo do YouTube:")
    if video_url:
        st.video(video_url)
        if st.button("🔍 Verificar automaticamente"):
            resultado = verificar_video(video_url)
            st.success(f"Resultado: {resultado}")

with tab2:
    uploaded_file = st.file_uploader("Enviar CSV com coluna `video_url`", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        if "video_url" in df.columns:
            st.success("Arquivo carregado. Verifique abaixo:")
            for idx, row in df.iterrows():
                st.markdown(f"### 🎥 Vídeo {idx + 1}")
                st.video(row["video_url"])
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown(f"- [Abrir vídeo diretamente]({row['video_url']})")
                with col2:
                    st.markdown("🟡 Status: Simulação")
                st.markdown("---")
        else:
            st.error("O CSV precisa conter uma coluna chamada exatamente `video_url`.")

st.markdown("---")
st.markdown("🔧 Em breve: verificação automática real com robô de navegação e leitura de anúncios.")
