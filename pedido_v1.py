import streamlit as st

# Caminho global para os assets
ASSETS_PATH = "/home/pedrov12/Documentos/GitHub/True-Lover/assets"


class StreamlitComponents:
    @staticmethod
    def exibir_imagem(caminho: str, **kwargs):
        """Exibe uma imagem."""
        st.image(caminho, **kwargs)

    @staticmethod
    def botao_download(label: str, caminho: str, nome_arquivo: str):
        """Cria um botão para download de arquivos."""
        with open(caminho, "rb") as file:
            st.download_button(
                label=label, data=file, file_name=nome_arquivo, mime="application/pdf"
            )

    @staticmethod
    def exibir_modal(texto: str):
        """Exibe uma mensagem em um modal."""
        st.write(texto)

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
        st.audio(caminho, autoplay=True, **kwargs)

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


class PedidoNamoro:
    def __init__(self):
        self.dialog_message = None  # Mensagem do diálogo

    def exibir_pedido(self):
        StreamlitComponents.criar_markdown(
            "<h3 style='text-align: center; color: red;'>Tem coragem de ver as novas cartas e poesias?</h3>",
            unsafe_allow_html=True,
        )

        # Botão para exibir uma imagem
        StreamlitComponents.criar_botao(
            "Exibir Imagem",
            on_click=lambda: StreamlitComponents.exibir_imagem(
                ASSETS_PATH + "fotos/foto1.jpg", use_container_width=True
            ),
        )

    def exibir_imagens(self):
        sidebar = StreamlitComponents.criar_sidebar()
        with sidebar:
            StreamlitComponents.exibir_imagem(
                ASSETS_PATH + "fotos/foto1.jpg", caption="", use_container_width=True
            )
            StreamlitComponents.criar_markdown(
                "<h4 style='text-align: center; color: white;'>O dia que nos conhecemos.</h4>",
                unsafe_allow_html=True,
            )

            StreamlitComponents.exibir_imagem(
                ASSETS_PATH + "fotos/foto2.jpg", caption="", use_container_width=True
            )
            StreamlitComponents.criar_markdown(
                "<h4 style='text-align: center; color: white;'>Nosso primeiro porre.</h4>",
                unsafe_allow_html=True,
            )

    def exibir_container(self):
        with StreamlitComponents.criar_container():
            StreamlitComponents.criar_header("Para o(a) mais especial.")
            StreamlitComponents.criar_subheader("🎶 Play na nossa musiquinha? 🎶")
            StreamlitComponents.criar_audio(
                ASSETS_PATH
                + "music/Justin Bieber - Anyone (Official Live Performance).mp3",
                format="audio/mpeg",
                loop=True,
            )
            StreamlitComponents.criar_header("Encontre a surpresa:")

            col1, col2, col3, col4, col5 = StreamlitComponents.criar_colunas(5)
            if col1.button("❤️", use_container_width=True, key=1):
                self.dialog_message = (
                    "Você é uma branch do github? Porque quero dar um merge com você."
                )
            if col2.button("❤️", use_container_width=True, key=2):
                self.dialog_message = "Você deve ser uma função, porque toda vez que eu te chamo, retorno para você."
            if col3.button("❤️", use_container_width=True, key=3):
                self.dialog_message = (
                    "Você pode ser meu compilador(a)? Porque eu não rodo sem você."
                )
            if col4.button("❤️", use_container_width=True, key=4):
                self.exibir_pedido()
            if col5.button("❤️", use_container_width=True, key=5):
                self.dialog_message = (
                    "Você é um debugger? Porque você pode me ajudar com meus erros."
                )

            # Exibir o diálogo se houver uma mensagem
            if self.dialog_message:
                StreamlitComponents.exibir_modal(self.dialog_message)
                self.dialog_message = None  # Limpar a mensagem após exibir


if __name__ == "__main__":
    pedido = PedidoNamoro()
    pedido.exibir_imagens()
    pedido.exibir_container()
