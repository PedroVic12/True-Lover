import streamlit as st
from PIL import Image


class StreamlitComponents:

    @staticmethod
    def exibir_imagem(caminho: str, rotate=True, **kwargs):
        """Exibe uma imagem."""
        imagem = Image.open(caminho)
        imagem_rotacionada = imagem.rotate(-90, expand=True)
        st.image(imagem_rotacionada, **kwargs)

    @staticmethod
    def botao_download(label: str, caminho: str, nome_arquivo: str):
        """Cria um botão para download de arquivos."""
        with open(caminho, "rb") as file:
            st.download_button(
                label=label, data=file, file_name=nome_arquivo, mime="application/pdf"
            )

    @staticmethod
    def exibir_modal(texto: str, **kwargs):
        """Exibe uma mensagem em um modal."""
        st.subheader(
            texto,
        )

    @staticmethod
    def criar_botao(label: str, on_click=None, **kwargs):
        """Cria um botão."""
        return st.button(label, on_click=on_click, **kwargs)

    @staticmethod
    def criar_container():
        """Cria um container."""
        return st.container()

    @staticmethod
    def criar_sidebar():
        """Cria a barra lateral."""
        return st.sidebar

    @staticmethod
    def criar_audio(caminho: str, **kwargs):
        """Reproduz um arquivo de áudio."""
        st.audio(caminho, autoplay=False, **kwargs)

    @staticmethod
    def criar_colunas(n):
        """Cria colunas."""
        return st.columns(n)

    @staticmethod
    def criar_markdown(markdown: str, **kwargs):
        """Cria um markdown."""
        st.markdown(markdown, **kwargs)

    @staticmethod
    def criar_header(texto: str, **kwargs):
        """Cria um cabeçalho."""
        st.header(texto, **kwargs)

    @staticmethod
    def criar_subheader(texto: str, **kwargs):
        """Cria um subcabeçalho."""
        st.subheader(texto, **kwargs)
