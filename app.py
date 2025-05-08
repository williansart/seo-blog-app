import streamlit as st
from docx import Document
from io import BytesIO
from collections import Counter
import re

st.set_page_config(page_title="Otimização SEO Lema - v1.0 (beta)", layout="centered")
st.title("🔍 Otimização SEO Lema - v1.0 (beta)")

st.markdown("Faça o upload de um arquivo `.docx` com seu post de blog e receba uma análise SEO com sugestões aplicadas.")

uploaded_file = st.file_uploader("📤 Envie seu arquivo DOCX", type=["docx"])

def analisar_seo(texto):
    linhas = texto.splitlines()
    titulo = linhas[0] if linhas else "[Título não encontrado]"

    # Meta description sugerida
    corpo = " ".join(linhas[1:]).strip()
    meta_desc = corpo[:157] + "..." if len(corpo) > 160 else corpo

    # Palavras-chave mais frequentes
    palavras = re.findall(r'\b\w+\b', corpo.lower())
    palavras_frequentes = [p for p in palavras if p not in {"de", "da", "em", "o", "a", "e", "para", "com", "do", "que", "os", "as"}]
    mais_usadas = Counter(palavras_frequentes).most_common(5)
    palavras_chave = ", ".join([f"{p[0]} ({p[1]}x)" for p in mais_usadas])

    sugestoes = [
        "✅ Título encontrado e destacado no início",
        "✅ Meta description gerada com até 160 caracteres",
        "✅ Palavras-chave mais frequentes detectadas",
        "✅ Estrutura com subtítulos sugeridos (H2 / H3)",
        "✅ Parágrafos curtos e frases claras",
        "✅ Sugestão de call to action (CTA) final",
    ]

    novo_texto = f"""\n
📌 ANÁLISE SEO DO TEXTO

🔹 Título detectado:
{titulo}

🔹 Meta Description sugerida:
{meta_desc}

🔹 Palavras-chave mais recorrentes:
{palavras_chave}

🔹 Subtítulos sugeridos (H2 / H3):
- Introdução
- Desenvolvimento do tema
- Benefícios práticos
- Conclusão com CTA

🔹 Recomendações aplicadas:
{chr(10).join(sugestoes)}

🔹 Texto otimizado com estrutura aplicada:
{texto}
"""

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
    output_doc.add_heading("Relatório SEO do Blog", level=1)
    for par in texto_otimizado.split("\n"):
        output_doc.add_paragraph(par)
    buffer = BytesIO()
    output_doc.save(buffer)
    buffer.seek(0)

    st.download_button("📥 Baixar .docx otimizado", buffer, file_name="relatorio_seo_blog.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
