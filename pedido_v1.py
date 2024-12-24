import streamlit as st

from src.stremlit_components import StreamlitComponents as widgets


# Caminho global para os assets
ASSETS_PATH = "./assets/"

print(widgets)


class PedidoNamoro:
    def __init__(self):
        self.dialog_message = None  # Mensagem do diálogo


    def card_image(self,path_img, text,img_rotate= True):
        widgets.exibir_imagem(
            ASSETS_PATH + path_img,
            caption="",
            use_container_width=True,
            rotate = img_rotate,
        )
        widgets.criar_markdown(
            f"<h3 style='text-align: center; color: white;'>{text}</h4>",
            unsafe_allow_html=True,
        )

        st.divider()

    def carrousel_imagens(self):

        st.markdown("# 2018")
        st.divider()

        widgets.exibir_imagem(
                ASSETS_PATH + "fotos/foto_2018_0.jpeg",
                caption="",
                use_container_width=True,
            )
        widgets.criar_markdown(
            "<h3 style='text-align: center; color: white;'>O dia que nos conhecemos.</h4>",
            unsafe_allow_html=True,
        )

        st.divider()

        widgets.exibir_imagem(
            ASSETS_PATH + "fotos/foto_2018_1.jpg",
            caption="",
            use_container_width=True,
            rotate = False,
        )
        widgets.criar_markdown(
            "<h3 style='text-align: center; color: white;'>Nosso primeiro porre.</h4>",
            unsafe_allow_html=True,
        )

        st.divider()

        self.card_image(
            "fotos/foto_2018_2.jpeg",
            "A gata e seu sorriso bonito."
        )

        self.card_image(
            "fotos/foto_2018_3.jpeg",
            "Obrigado por topar meter o louco comigo",
            img_rotate= False
        )

        self.card_image(
            "fotos/foto_2018_4.jpeg",
            "Sempre fomos muito lindos juntos. Eu lembro do beijo na bochecha desse dia ate hoje",
            img_rotate= False

        )

        self.card_image(

            "fotos/foto_2018_5.jpeg",
            "Essa foto tem historia...",
            img_rotate= False
        )


        self.card_image(
            "fotos/foto_2018_6.jpeg",
            "Obrigado por sempre cuidar de mim <3",
            img_rotate= False
        )

        st.markdown("# 2019")

        self.card_image(
            "fotos/foto_2019_0.jpg",
            "Inicio da nossa fase BusinessWoman e Homem de negocios",
            img_rotate= False
        )

        self.card_image(
            "fotos/foto_2019_1.jpg",
            "Sempre foi um sonho ter voce no meu lado",
            img_rotate= False
        )

        self.card_image(
            "fotos/foto_2019_2.JPG",
            "Começo do carnaval indo fantasiados hahaha",
            img_rotate= True
        )

        self.card_image(
            "fotos/foto_2019_4.JPG",
            "Fim do carnaval com voce",
            img_rotate= False
        )

        self.card_image(
            "fotos/foto_2019_6.jpg",
            "Eu realmente acho que nessa foto nosso corpo forma um coração <3",
            img_rotate= False
        )

        st.markdown("# 2020")

        self.card_image(
            "fotos/foto_2020_0.jpeg",
            "Tivemos nossa primeira foto de ano novo juntos",
            img_rotate= False
        )

        self.card_image(
            "fotos/foto_2020_1.jpeg",
            "Voce sempre foi minha sereia e companheira de praia",
            img_rotate= False
        )


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

        st.markdown("# OBS (IMPORTANTE ANTES DE LER):")
        # CSS para destacar o texto em amarelo
        custom_css = """
            <style>
            .highlight {
                padding: 10px;
                border-radius: 5px;
                font-size: 18px;
            }
            </style>
        """
        # Injetando o CSS
        st.markdown(custom_css, unsafe_allow_html=True)

        # Conteúdo formatado
        st.markdown("""
        ## Este não é um pedido de volta ou de reconciliação.
        <div class="highlight">
        Eu te respeito e sempre vou te respeitar.

        Toda essa homenagem e esse carinho vêm da minha profunda gratidão por você neste ano. Você resgatou algo muito especial em mim: o amor. Hoje, sinto esse sentimento vivo dentro do meu coração, e você não faz ideia do quanto isso me faz bem. Você foi, sem dúvida, a melhor coisa que aconteceu comigo este ano.

        De verdade, não esperava sentir algo tão verdadeiro novamente (finalmente, né?). Voltar a ter sentimentos depois de uma fase depressiva que superei foi algo muito importante para mim. Como pisciano, sempre tive dificuldade em demonstrar meus sentimentos, mas com você foi diferente.

        Por isso, agradeço a Deus e a você por resgatar o amor que estava escondido dentro de mim, com medo de aparecer. Sou imensamente grato por tudo, você mora no meu coração, vagalume <3 e isso vai ser para sempre, indepedente de qualquer coisa, sempre estarei te apoiando e tentando te ajudar para voce alcançar seu sucesso! <3
        </div>
        """, unsafe_allow_html=True)


    def menuLateral(self):
        sidebar = widgets.criar_sidebar()
        custom_css = """
        <style>
        [data-testid="stBaseButton-headerNoPadding"] {
            border: 2px solid #FF5733 !important; /* Borda laranja */
            background-color: #FFC300 !important; /* Fundo amarelo */
            color: black !important; /* Cor da seta */
            font-size: 30px !important; /* Tamanho do ícone */
            border-radius: 10px !important; /* Cantos arredondados */
            width: 60px !important; /* Largura do botão */
            height: 60px !important; /* Altura do botão */
            display: flex; /* Garante centralização */
            justify-content: center;
            align-items: center;
            animation: pulse 2s infinite !important; /* Efeito de pulsar */
        }
        [data-testid="stBaseButton-headerNoPadding"] svg {
            transform: scale(1.5); /* Aumenta o tamanho do ícone SVG */
        }
        @keyframes pulse {
            0% {transform: scale(1);}
            50% {transform: scale(1.1);}
            100% {transform: scale(1);}
        }
        </style>
    """
        # Injetando CSS no app
        st.markdown(custom_css, unsafe_allow_html=True)
        with sidebar:

            widgets.criar_markdown("# Nossa evolução ao longo dos anos (2018 - 2024)", unsafe_allow_html=True)


            self.carrousel_imagens()

            

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
