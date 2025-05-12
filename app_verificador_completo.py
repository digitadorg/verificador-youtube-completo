import streamlit as st
import pandas as pd

st.set_page_config(page_title="Detector de Anúncios no YouTube", page_icon="🎯")

st.title("🎯 Detector de Anúncios no YouTube")
st.markdown("Este app ajuda você a **verificar se vídeos do YouTube exibem anúncios** e são segmentáveis no Google Ads.")

tab1, tab2 = st.tabs(["🔗 Verificador individual", "📂 Verificador em lote (CSV)"])

with tab1:
    video_url = st.text_input("Cole o link do vídeo do YouTube:")
    if video_url:
        st.video(video_url)
        st.markdown("### 🧪 Teste manual sugerido:")
        st.markdown(f"- 🔗 [Abrir vídeo diretamente]({video_url})")
        st.markdown("- ❌ Desative bloqueadores de anúncios")
        st.markdown("- ✅ Veja se aparece algum dos seguintes:")
        st.markdown("  - Anúncio em vídeo (antes, durante ou depois)")
        st.markdown("  - Banner sobreposto com botão de fechar")
        st.markdown("  - Botão 'Pular anúncio'")
        st.info("Se aparecer algum dos elementos acima, o vídeo está monetizado e aceita anúncios.")

with tab2:
    st.markdown("Faça upload de um arquivo `.csv` com uma coluna chamada `video_url` contendo os links dos vídeos.")
    uploaded_file = st.file_uploader("Enviar CSV", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        if "video_url" in df.columns:
            st.success("Arquivo carregado com sucesso! Veja os vídeos abaixo para verificação manual:")
            for idx, row in df.iterrows():
                st.markdown(f"### 🎥 Vídeo {idx + 1}")
                st.video(row["video_url"])
                st.markdown(f"- [Abrir vídeo diretamente]({row['video_url']})")
                st.markdown("---")
        else:
            st.error("⚠️ O CSV precisa ter uma coluna chamada exatamente `video_url`.")

st.markdown("---")
st.markdown("🛡️ *Este app não coleta dados. É apenas uma ferramenta de apoio para anunciantes da Rede de Display.*")
