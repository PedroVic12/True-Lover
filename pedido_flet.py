import flet as ft

def main(page: ft.Page):
    page.title = "Para o(a) mais especial"

    # Dicionário de imagens
    image_dict = {
        "conhecemos": "https://i.pinimg.com/736x/04/32/b0/0432b0e1b6645072a471234b66b12530.jpg",
        "porre": "https://i.pinimg.com/736x/f9/09/f4/f909f41ee03acae0a10c9616976237bb.jpg",
        "gata":"https://i.pinimg.com/736x/2c/e8/ce/2ce8ce80e30b3711b595081ee7b9a7de.jpg",
        "abraco": "https://i.pinimg.com/736x/a5/2a/d4/a52ad46c3bc13c25563c3fc34d533295.jpg",
        
        # ... outras imagens
    }

    # Página principal
    page.add(
        ft.Column([
            ft.Row([
                ft.Image(src=image_dict["conhecemos"], width=200),
                ft.Image(src=image_dict["porre"], width=200),
                # ... outras imagens
            ]),
            ft.Audio(
                src="Justin Bieber - Anyone (Official Live Performance).mp3",
                autoplay=True,
                #loop=True
            ),
            ft.Row([
                ft.ElevatedButton("❤️", on_click=lambda e: show_modal("Você é uma branch do github? Porque quero dar um merge com você.")),
                ft.ElevatedButton("❤️", on_click=lambda e: show_modal("Você deve ser uma função, porque toda vez que eu te chamo, retorno para você.")),
                ft.ElevatedButton("❤️", on_click=lambda e: show_modal("Voce pode ser meu compilador(a)? Porque eu não rodo sem você.")),
                ft.ElevatedButton("❤️", on_click=lambda e: show_modal("Quer namorar comigo?", on_click=lambda e: show_modal("Te amo, vida"))),
                ft.ElevatedButton("❤️", on_click=lambda e: show_modal("Você é um debugger? Porque você pode me ajudar com meus erros."))
            ])
        ])
    )

    # Página modal (inicialmente oculta)
    modal = ft.AlertDialog(
        title="Mensagem",
        content=ft.Text("Conteúdo da modal"),
        actions=[ft.TextButton("OK", on_click=lambda e: page.dialog.close())],
        modal=True,
        on_dismiss=lambda e: page.go("/")
    )
    page.overlay.append(modal)

    def show_modal(message):
        modal.content.value = message
        page.dialog = modal
        page.go("/dialog")

ft.app(target=main)
