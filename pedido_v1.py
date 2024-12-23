import streamlit as st

from src.stremlit_components import StreamlitComponents as widgets

print(widgets)

# Caminho global para os assets
ASSETS_PATH = "./assets/"


class PedidoNamoro:
    def __init__(self):
        self.dialog_message = None  # Mensagem do diálogo

    def exibir_pedido(self):
        widgets.criar_markdown(
            "<h3 style='text-align: center; color: red;'>Tem coragem de ver as novas cartas e poesias que fiz para voce?</h3>",
            unsafe_allow_html=True,
        )

        # Botão para exibir uma imagem
        widgets.criar_botao(
            "Carta 1",
            on_click=lambda: widgets.exibir_imagem(
                ASSETS_PATH + "fotos/carta1.jpg", use_container_width=True
            ),
        )

        widgets.criar_botao(
            "Carta 2",
            on_click=lambda: widgets.exibir_imagem(
                ASSETS_PATH + "fotos/carta2.jpg", use_container_width=True
            ),
        )
        widgets.criar_botao(
            "Poesia 1",
            on_click=lambda: widgets.exibir_imagem(
                ASSETS_PATH + "fotos/poesia1.jpg", use_container_width=True
            ),
        )

        widgets.criar_botao(
            "Poesia 2",
            on_click=lambda: widgets.exibir_imagem(
                ASSETS_PATH + "fotos/poesia2.jpg", use_container_width=True
            ),
        )

    def menuLateral(self):
        sidebar = widgets.criar_sidebar()
        with sidebar:
            widgets.criar_header("Nossa evolução ao longo dos anos")
            widgets.exibir_imagem(
                ASSETS_PATH + "fotos/foto_2018_0.jpeg",
                caption="",
                use_container_width=True,
            )
            widgets.criar_markdown(
                "<h4 style='text-align: center; color: white;'>O dia que nos conhecemos.</h4>",
                unsafe_allow_html=True,
            )

            widgets.exibir_imagem(
                ASSETS_PATH + "fotos/foto_2018_1.jpg",
                caption="",
                use_container_width=True,
                rotate = False,
            )
            widgets.criar_markdown(
                "<h4 style='text-align: center; color: white;'>Nosso primeiro porre.</h4>",
                unsafe_allow_html=True,
            )

    def page(self):
        with widgets.criar_container():
            st.image(ASSETS_PATH + "fotos/gif_animado.gif")
            st.divider()
            widgets.criar_header(
                "Para a mais especial, minha feiticeira, que tem o sorriso que ilumina meu coração, "
            )
            widgets.criar_header("Danielle Serrano.")
            st.divider()
            widgets.criar_subheader("🎶 Play na nossa musiquinha? 🎶")
            widgets.criar_subheader("1) Opção Natalina")
            widgets.criar_audio(
                ASSETS_PATH
                + "music/Justin Bieber - Mistletoe (Official Music Video).mp3",
                format="audio/mpeg",
            )
            widgets.criar_subheader("2) Opção Romântica")
            widgets.criar_audio(
                ASSETS_PATH
                + "music/Justin Bieber - Anyone (Official Live Performance).mp3",
                format="audio/mpeg",
            )
            widgets.criar_header("Encontre a sua surpresa de natal:")

            col1, col2, col3, col4, col5, col6 = widgets.criar_colunas(6)
            if col1.button("❤️", use_container_width=True, key=1):
                self.dialog_message = '"O amor não consiste em olhar um para o outro, mas em olhar juntos na mesma direção." – Antoine de Saint-Exupéry"'
            if col2.button("❤️", use_container_width=True, key=2):
                self.dialog_message = '"Nossas almas se encontraram muito antes de nossos olhos se cruzarem."'
            if col3.button("❤️", use_container_width=True, key=3):
                self.dialog_message = "Ser profundamente amado por alguém nos dá força; amar alguém profundamente nos dá coragem.  – Lao Tzu"
            if col4.button("❤️", use_container_width=True, key=4):
                self.exibir_pedido()
            if col5.button("❤️", use_container_width=True, key=5):
                self.dialog_message = '"Amar você é mergulhar em um oceano de emoções onde a profundidade nunca termina."'
            if col6.button("❤️", use_container_width=True, key=6):
                self.dialog_message = (
                    '"No abraço do teu amor, encontrei o lar que sempre procurei."'
                )

            # Exibir o diálogo se houver uma mensagem
            if self.dialog_message:
                widgets.exibir_modal(self.dialog_message)
                self.dialog_message = None  # Limpar a mensagem após exibir


if __name__ == "__main__":
    pedido = PedidoNamoro()
    pedido.menuLateral()
    pedido.page()
