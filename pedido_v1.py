import streamlit as st

from src.stremlit_components import StreamlitComponents as widgets

import random


# Caminho global para os assets
ASSETS_PATH = "./assets/"

#print(widgets)


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

    def video_youtube(self):
        from streamlit_player import st_player

        # Embed a youtube video
        st_player("https://www.youtube.com/watch?v=Il-R_o_rldA")
        # O link do YouTube deve estar dentro do src="link_do_video"
        #html_code = """<iframe width="560" height="315" src="https://www.youtube.com/embed/7xbPK_y1Dv8?si=bDUpO0iiwIhaK0L2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>        """

        #st.html(html_code)

    def text_h3(self,text):
        return  f"<h3 style='text-align: center; color: #5613a9; font: bold;'>{text}</h4>"


    def carrousel_imagens(self):

        st.markdown("# 2018")
        st.divider()

        widgets.exibir_imagem(
                ASSETS_PATH + "fotos/foto_2018_0.jpeg",
                caption="",
                use_container_width=True,
            )
        widgets.criar_markdown(
            "<h3 style='text-align: center; color: #5613a9;'>O dia que nos conhecemos.</h4>",
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
            "<h3 style='text-align: center; color: #5613a9;'>Nosso primeiro porre.</h4>",
            unsafe_allow_html=True,
        )

        st.divider()

        self.card_image(
            "fotos/foto_2018_2.jpeg",
            self.text_h3(
            "A gata e seu sorriso bonito <3 "
            ),
        )

        self.card_image(
            "fotos/foto_2018_3.jpeg",
            self.text_h3("Obrigado por topar meter o louco comigo"),
            img_rotate= False
        )

        self.card_image(
            "fotos/foto_2018_4.jpeg",
            self.text_h3("Sempre fomos muito lindos juntos. Eu lembro do beijo na bochecha desse dia ate hoje"),

            img_rotate= False

        )

        self.card_image(

            "fotos/foto_2018_5.jpeg",
            self.text_h3("Essa foto tem historia..."),
            img_rotate= False
        )


        self.card_image(
            "fotos/foto_2018_6.jpeg",
            self.text_h3("Obrigado por sempre cuidar de mim <3"),
            img_rotate= False
        )

        st.markdown("# 2019")

        self.card_image(
            "fotos/foto_2019_0.jpg",
            self.text_h3("Inicio da nossa fase BusinessWoman e Homem de negocios"),
            img_rotate= False
        )

        self.card_image(
            "fotos/foto_2019_1.jpg",
            self.text_h3("Sempre foi um privilégio ter voce no meu lado"),
            img_rotate= False
        )

        self.card_image(
            "fotos/foto_2019_2.JPG",
            self.text_h3("Começo de carnaval indo fantasiados hahaha"),
            img_rotate= True
        )

        self.card_image(
            "fotos/foto_2019_4.JPG",
            self.text_h3("Fim do carnaval com voce"),
            img_rotate= True
        )

        self.card_image(
            "fotos/foto_2019_6.jpg",
            self.text_h3("Eu amo essa foto porque ela forma um coração <3"),
            img_rotate= False
        )

        st.markdown("# 2020")

        self.card_image(
            "fotos/foto_2020_0.jpeg",
            self.text_h3("Tivemos nossa primeira foto de ano novo juntos"),
            img_rotate= False
        )

        self.card_image(
            "fotos/foto_2020_1.jpeg",
            self.text_h3("Eu e minha Sereia na praia..."),
            img_rotate= False
        )

        self.card_image(
            "fotos/foto_2020_2.jpeg",
            self.text_h3("O mar é nosso ponto de equilibrio"),
            img_rotate= False
        )

        self.card_image(
            "fotos/foto_2020_3.jpg",
            self.text_h3("Sobrevivemos uma pandemia juntos..."),
            img_rotate= False
        )


        st.markdown("# 2021")

        self.card_image(
            "fotos/foto_2021_0.jpg",
            self.text_h3("Tivemos mais uma virada de ano... de muitas emoçoes"),
            img_rotate= False
        )

        self.card_image(
            "fotos/foto_2021_1.JPG",
            self.text_h3("O tempo nos embelezou muito! Fala serio!!!"),
            img_rotate= True
        )

        self.card_image(
            "fotos/foto_2021_3.jpg",
            self.text_h3("Obrigado por sempre cuidar de mim <3 mesmo nas minhas dificuldades"),
            img_rotate= False
        )

        st.markdown("# 2024")

        self.card_image(
            "fotos/foto_2024_2.jpg",
            self.text_h3("Ate hoje sou encantado com seu sorriso ilumindo o ambiente"),
            img_rotate= False
        )

        self.card_image(
            "fotos/colagem.jpg",
            self.text_h3("Obrigado por tudo nesse ano de 2024!"),
                        img_rotate= False

        )

        self.card_image(
            "fotos/foto_2024.jpg",
            self.text_h3("Ainda quero arrancar muito sorriso seu <3 "),
            img_rotate= False
        )

    def carrossel_videos(self):
        videos = {
            "O que eu sinto": "https://www.youtube.com/watch?v=Il-R_o_rldA",
            "O que eu penso": "https://www.youtube.com/watch?v=7xbPK_y1Dv8",

            "O que eu faço": "https://youtu.be/1RcP7Dsterg?si=-sg39LacnxvZjX6f",
        }

        escolha = st.radio("Escolha um vídeo 🎬", list(videos.keys()))
        from streamlit_player import st_player
        st_player(videos[escolha])


 

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



    def tocar_musica_random(self):
            # 🎶 Várias músicas por categoria
            musicas = {
                "Natalina": [
                    ASSETS_PATH + "music/Justin Bieber - Mistletoe (Official Music Video).mp3",
                    ASSETS_PATH + "music/Justin Bieber - Anyone (Official Live Performance).mp3",
                ],
                "Romântica": [
                    ASSETS_PATH + "music/two_is_better.mp3",
                    ASSETS_PATH + "music/Enrique-Iglesias-feat-Miranda-Lambert-Space-In-My-Heart-(CeeNaija.com).mp3",
                    ASSETS_PATH + "music/Glee_Cast_-_Without_You.mp3",
                    ASSETS_PATH + "music/HighSchoolMusical3CanIHaveThisDanceHd.mp3",
                    ASSETS_PATH + "music/Ed_Sheeran_-_-_Thinking_Out_Loud.mp3"
                ],
                "Sofrência": [
                    ASSETS_PATH + "music/Sorriso Bonito.mp3",
                    ASSETS_PATH + "music/01 - Salva Meu Coração.mp3",
                    ASSETS_PATH + "music/01TheClimb.mp3",
                    ASSETS_PATH + "music/Manu_Gavassi_-_Planos_Impossiveis_(mp3.pm).mp3"

                ]
            }

            # Selecionar categoria
            categoria = st.selectbox("Escolha o estilo 🎶", list(musicas.keys()))

            # 🎲 Sorteia música apenas dentro da categoria (mas não mostra o nome)
            if st.button(f"Tocar {categoria} aleatória"):
                musica_escolhida = random.choice(musicas[categoria])
                st.audio(musica_escolhida, format="audio/mpeg")

            # 🎲 Aleatório global (não mostra nome)
            if st.button("Tocar música totalmente aleatória 🎲"):
                todas = sum(musicas.values(), [])  # junta todas as listas
                musica_escolhida = random.choice(todas)
                st.audio(musica_escolhida, format="audio/mpeg")

    def listar_opcoes_Musicas(self):
        # Listar opções
        widgets.criar_subheader("1) Opção Natalina :) ")
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



    def page(self):

        #playlsit songs
        songs_romanticas = [ ]


        with widgets.criar_container():

            # Carrousel de videos
            st.image(ASSETS_PATH + "fotos/coracao_dani.jpg")
            st.image(ASSETS_PATH + "fotos/gif_animado.gif")
            st.divider()



            # header
            widgets.criar_header(
                "Para a minha feiticeira e minha Sereia, que tem um sorriso lindo que ilumina meu coração"
            )
            widgets.criar_header("Feliz Natal e um otimo ano de 2025, Danielle Serrano! <3", )
            st.divider()
            
            # videos HSM
            video_url_hf = "https://huggingface.co/spaces/pedrov12/dashboard_moderno/resolve/main/true_lover.mp4"
            st.video(video_url_hf)
            
            st.video(

                data = "https://drive.google.com/file/d/1rOrIGCOxH8OaGH0x_I3b6QCzp774Zbwo/view?usp=sharing",
                #data= ASSETS_PATH + "true_lover.mp4",
                format="video/mp4"
            )

            # Escolhad de musicas
            widgets.criar_subheader("🎶 Play na nossa musiquinha? Escolha entre as opções 🎶")
            self.tocar_musica_random()


            ## Carrousel 
            self.carrossel_videos()

            st.divider()



            widgets.criar_header("Encontre a sua surpresa de natal: rsrs ")

            col1, col2, col3, col4, = widgets.criar_colunas(4)

            if col1.button("❤️", use_container_width=True, key=1):
                self.dialog_message = "Ser profundamente amado por alguém nos dá força; amar alguém profundamente nos dá coragem.  – Lao Tzu"
            if col2.button("❤️", use_container_width=True, key=2):
                self.dialog_message = '"Nossas almas se encontraram muito antes de nossos olhos se cruzarem..."'
            
            if col3.button("❤️", use_container_width=True, key=3):
                self.exibir_pedido()

            if col4.button("❤️", use_container_width=True, key=4):
                self.dialog_message = '"Amar você, minha Sereia, é como mergulhar em um oceano de emoções onde a profundidade nunca termina..."'


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
            for i in range(25):  # Número de flocos de neve
                animation_symbol = "❄️"
                st.markdown(
                    f"""
                    <div class="snowflake" style="left: {i * 10}%; -webkit-animation-delay: {i * 0.5}s; animation-delay: {i * 0.5}s;">{animation_symbol}</div>
                    """,
                    unsafe_allow_html=True
                )

            # footer
            widgets.criar_header("Agradecimentos, Feliz Natal! e um prospero ano de 2025")
            widgets.criar_header("Pedro Victor")


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

            


if __name__ == "__main__":
    pedido = PedidoNamoro()
    pedido.menuLateral()
    pedido.page()
