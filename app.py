
import streamlit as st
from docx import Document
from io import BytesIO

st.set_page_config(page_title="Otimização SEO de Blog", layout="centered")
st.title("🔍 Otimizador de Blog com SEO")

st.markdown("Faça o upload de um arquivo `.docx` com seu post de blog e receba uma análise SEO com sugestões aplicadas.")

uploaded_file = st.file_uploader("📤 Envie seu arquivo DOCX", type=["docx"])

def analisar_seo(texto):
    # Simulação de sugestões (versão básica)
    sugestoes = [
        "✅ Verifique se a palavra-chave aparece no título.",
        "✅ Adicione uma meta description com até 160 caracteres.",
        "✅ Use subtítulos H2 e H3 com palavras-chave.",
        "✅ Prefira parágrafos curtos e frases na voz ativa.",
        "✅ Insira links internos (para seu site) e externos (fontes).",
        "✅ Descreva imagens com 'alt text'.",
        "✅ Certifique-se que o conteúdo seja mobile friendly.",
        "✅ Finalize com um Call to Action (CTA).",
        "✅ Use título único e adicione tags no post."
    ]
    novo_texto = "🔧 Texto otimizado (simulação)\\n\\n" + texto

" + texto
    return "\n".join(sugestoes), novo_texto

if uploaded_file:
    doc = Document(uploaded_file)
    texto = "\n".join([p.text for p in doc.paragraphs if p.text.strip() != ""])
    
    st.subheader("✅ Análise SEO")
    checklist, texto_otimizado = analisar_seo(texto)
    st.text(checklist)

    st.subheader("📝 Texto Otimizado")
    st.text_area("Prévia:", texto_otimizado, height=300)

    # Gerar novo .docx para download
    output_doc = Document()
    output_doc.add_heading("Texto Otimizado para SEO", level=1)
    output_doc.add_paragraph(texto_otimizado)
    buffer = BytesIO()
    output_doc.save(buffer)
    buffer.seek(0)

    st.download_button("📥 Baixar .docx otimizado", buffer, file_name="texto_otimizado.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
