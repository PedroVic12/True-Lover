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
            img_rotate= True
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

        self.card_image(
            "fotos/foto_2020_2.jpeg",
            "Sempre sonhei ter uma pessoa que goste de entrar no mar comigo",
            img_rotate= False
        )

        self.card_image(
            "fotos/foto_2020_3.jpg",
            "Sobrevivemos uma pandemia juntos...",
            img_rotate= False
        )


        st.markdown("# 2021")

        self.card_image(
            "fotos/foto_2021_0.jpg",
            "Tivemos mais uma virada de ano... de muitas emoçoes",
            img_rotate= False
        )

        self.card_image(
            "fotos/foto_2021_1.JPG",
            "O tempo nos embelezou muito! Fala serio!!!",
            img_rotate= True
        )

        self.card_image(
            "fotos/foto_2021_3.jpg",
            "Obrigado por sempre cuidar de mim <3 mesmo nas minhas dificuldades",
            img_rotate= False
        )

        st.markdown("# 2024")

        self.card_image(
            "fotos/foto_2024_2.jpg",
            "Ate hoje sou encantado com seu sorriso ilumindo o ambiente",
            img_rotate= False
        )

        self.card_image(
            "fotos/colagem.jpg",
            "Obrigado por tudo nesse ano de 2024!",
                        img_rotate= False

        )

        self.card_image(
            "fotos/foto_2024.jpg",
            "Ainda quero arrancar muito sorriso seu <3 ",
            img_rotate= False
        )



    def exibir_pedido(self):
        widgets.criar_markdown(
            "<h3 style='text-align: center; color: red;'>Tem coragem de ver as novas cartas e poesias que fiz para voce?</h3>",
            unsafe_allow_html=True,
        )

        # Botão para exibir uma imagem
        widgets.criar_botao(
            "Carta 1 (10/11/2024)",
            on_click=lambda: widgets.exibir_imagem(
                ASSETS_PATH + "fotos/carta1.jpg", use_container_width=True
            ),
        )

        widgets.criar_botao(
            "Carta 2 (18/12/2024)",
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
            widgets.criar_header("Feliz Natal, Danielle Serrano! :)", )
            st.divider()
            widgets.criar_subheader("🎶 Play na nossa musiquinha? Escolha entre as opções 🎶")
            widgets.criar_markdown("# Não tem HSM ta muito na cara já xD")
            widgets.criar_subheader("1) Opção Natalina")
            widgets.criar_audio(
                ASSETS_PATH
                + "music/Justin Bieber - Mistletoe (Official Music Video).mp3",
                format="audio/mpeg",
            )
            widgets.criar_subheader("2) Opção Romântica")
            widgets.criar_audio(
                ASSETS_PATH
                + "music/two_is_better.mp3",
                format="audio/mpeg",
            )

            widgets.criar_subheader("3) Opção Sofrencia Brasileira")
            widgets.criar_audio(
                ASSETS_PATH
                + "music/Sorriso Bonito.mp3",
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

            st.divider()
            natal_css = """
            /* customizable snowflake styling */
            .snowflake {
            color: #FFF;
            font-size: 1em;
            font-family: Arial;
            text-shadow: 0 0 1px #000;
            }

            @-webkit-keyframes snowflakes-fall{0%{top:-10%}100%{top:100%}}@-webkit-keyframes snowflakes-shake{0%{-webkit-transform:translateX(0px);transform:translateX(0px)}50%{-webkit-transform:translateX(80px);transform:translateX(80px)}100%{-webkit-transform:translateX(0px);transform:translateX(0px)}}@keyframes snowflakes-fall{0%{top:-10%}100%{top:100%}}@keyframes snowflakes-shake{0%{transform:translateX(0px)}50%{transform:translateX(80px)}100%{transform:translateX(0px)}}.snowflake{position:fixed;top:-10%;z-index:9999;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;cursor:default;-webkit-animation-name:snowflakes-fall,snowflakes-shake;-webkit-animation-duration:10s,3s;-webkit-animation-timing-function:linear,ease-in-out;-webkit-animation-iteration-count:infinite,infinite;-webkit-animation-play-state:running,running;animation-name:snowflakes-fall,snowflakes-shake;animation-duration:10s,3s;animation-timing-function:linear,ease-in-out;animation-iteration-count:infinite,infinite;animation-play-state:running,running}.snowflake:nth-of-type(0){left:1%;-webkit-animation-delay:0s,0s;animation-delay:0s,0s}.snowflake:nth-of-type(1){left:10%;-webkit-animation-delay:1s,1s;animation-delay:1s,1s}.snowflake:nth-of-type(2){left:20%;-webkit-animation-delay:6s,.5s;animation-delay:6s,.5s}.snowflake:nth-of-type(3){left:30%;-webkit-animation-delay:4s,2s;animation-delay:4s,2s}.snowflake:nth-of-type(4){left:40%;-webkit-animation-delay:2s,2s;animation-delay:2s,2s}.snowflake:nth-of-type(5){left:50%;-webkit-animation-delay:8s,3s;animation-delay:8s,3s}.snowflake:nth-of-type(6){left:60%;-webkit-animation-delay:6s,2s;animation-delay:6s,2s}.snowflake:nth-of-type(7){left:70%;-webkit-animation-delay:2.5s,1s;animation-delay:2.5s,1s}.snowflake:nth-of-type(8){left:80%;-webkit-animation-delay:1s,0s;animation-delay:1s,0s}.snowflake:nth-of-type(9){left:90%;-webkit-animation-delay:3s,1.5s;animation-delay:3s,1.5s}

                """

            # Injetando CSS no app
            st.markdown(
                f"<style>{natal_css}</style>", unsafe_allow_html=True
            )

            # Criando flocos de neve
            for i in range(20):  # Número de flocos de neve
                animation_symbol = "❄️"
                st.markdown(
                    f"""
                    <div class="snowflake" style="left: {i * 10}%; -webkit-animation-delay: {i * 0.5}s; animation-delay: {i * 0.5}s;">{animation_symbol}</div>
                    """,
                    unsafe_allow_html=True
                )
            widgets.criar_header("Agradecimentos, Feliz Natal! e um prospero ano de 2025")
            widgets.criar_header("Pedro Victor")


if __name__ == "__main__":
    pedido = PedidoNamoro()
    pedido.menuLateral()
    pedido.page()
