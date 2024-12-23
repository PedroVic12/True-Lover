from tkinter import Canvas, Tk, Frame, Label, Button, messagebox
from math import sin, cos
from random import randint, choice


class Heart(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.canvas = Canvas(master, bg="black")
        self.canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.objects = []
        self.num = 0
        self.chars = ["➤", "♥", "☆", "◉", "➹", "☼", "❋", "☺", "♪"]
        self.char = "☆"

        self.create_obj()
        self.update()

        self.message = Label(
            self.canvas,
            text="Que a força sempre esteja com você <3, TE AMO! Minha princesa <3",
            fg="white",
            bg="black",
            font=("Arial", 20, "bold"),
        )
        self.message.place(relx=0.5, rely=0.9, anchor="center")

    def create_obj(self):
        for i in range(200):
            obj = self.canvas.create_text(0, 0, font=("Arial", 24))
            self.canvas.coords(obj, 500, 250)
            self.objects.append(obj)

    def draw(self, obj, x, y, color, char):
        self.canvas.itemconfig(obj, fill=color, text=char)
        self.canvas.move(obj, x, y)

    def update(self):
        for t in range(0, 200, 1):
            xp = -1 * int(16 * pow(sin(t), 3))
            yp = -1 * int(13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t))
            color = "#{:02x}{:02x}{:02x}".format(
                randint(100, 255), 0, randint(100, 255)
            )

            self.draw(self.objects[self.num], xp, yp, color, self.char)

            xy = self.canvas.coords(self.objects[self.num])

            self.num += 1
            if self.num >= 200:
                self.num = 0
            if xy[0] >= 800:
                self.char = choice(self.chars)
                for s in range(200):
                    self.canvas.moveto(self.objects[s], 520, 270)

        self.master.after(100, self.update)


class ProposalApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Aceitas?")
        self.root.geometry("600x600")
        self.root.configure(background="#ffc8dd")

        self.setup_ui()

    def setup_ui(self):
        margin = Canvas(
            self.root,
            width=600,
            bg="#ffc8dd",
            height=100,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        margin.pack()

        text_id = Label(
            self.root,
            bg="#ffc8dd",
            text="Quer voltar a ficar comigo? 🥺",
            fg="#590d22",
            font=("Montserrat", 24, "bold"),
        )
        text_id.pack()

        self.button_no = Button(
            self.root,
            text="Não",
            bg="#ffb3c1",
            command=self.denied,
            relief="ridge",
            bd=3,
            font=("Montserrat", 8, "bold"),
        )
        self.button_no.pack()

        self.button_yes = Button(
            self.root,
            text="Sim",
            bg="#ffb3c1",
            relief="ridge",
            bd=3,
            command=self.accepted,
            font=("Montserrat", 14, "bold"),
        )
        self.button_yes.pack()

    def accepted(self):
        self.root.destroy()
        heart_window = Tk()
        heart_window.title("Heart Animation")
        heart_window.geometry("1200x700")
        Heart(heart_window)
        heart_window.mainloop()

    def denied(self):
        denied_window = Tk()
        denied_window.title("Ops!")
        denied_window.geometry("500x300")
        denied_window.configure(background="#ffc8dd")

        Label(
            denied_window,
            text="A por favor... vai... pensa com carinho....",
            fg="#590d22",
            bg="#ffc8dd",
            font=("Montserrat", 16, "bold"),
        ).pack(pady=20)

        Button(
            denied_window,
            text="Fechar",
            bg="#ffb3c1",
            command=denied_window.destroy,
            relief="ridge",
            bd=3,
            font=("Montserrat", 10, "bold"),
        ).pack()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = ProposalApp()
    app.run()
