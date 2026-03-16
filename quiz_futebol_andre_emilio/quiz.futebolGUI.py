import tkinter as tk
from tkinter import messagebox
import random
import os

# =========================================
# CONFIGURAÇÕES
# =========================================

APP_TITLE = "Arquivo Esportivo 18.4.3"
TIME_PER_QUESTION = 15
RANKING_FILE = "ranking.txt"

THEMES = {
    "Copa do Mundo": "#1E8449",
    "UCL": "#922B21",
    "Eurocopa": "#566573",
    "Brasileirão": "#1F618D",
    "Libertadores": "#B7950B"
}

QUESTIONS = {
    "Copa do Mundo": [
        ("Quem venceu a Copa de 1970?", ["Brasil", "Itália", "Alemanha", "Uruguai"], "Brasil"),
        ("Onde foi a Copa de 2014?", ["Brasil", "Alemanha", "Rússia", "Qatar"], "Brasil"),
        ("Quem venceu a Copa de 2022?", ["Argentina", "França", "Brasil", "Croácia"], "Argentina"),
    ],
    "UCL": [
        ("Qual clube tem mais Champions?", ["Real Madrid", "Milan", "Liverpool", "Barcelona"], "Real Madrid"),
        ("Quem venceu a Champions 2023?", ["Manchester City", "Inter", "Real Madrid", "Bayern"], "Manchester City"),
    ],
    "Eurocopa": [
        ("Quem venceu a Euro 2016?", ["Portugal", "França", "Alemanha", "Espanha"], "Portugal"),
        ("Quem venceu a Euro 2021?", ["Itália", "Inglaterra", "França", "Portugal"], "Itália"),
    ],
    "Brasileirão": [
        ("Quem venceu o Brasileirão de 2019?", ["Flamengo", "Palmeiras", "Santos", "Grêmio"], "Flamengo"),
        ("Quem venceu o Brasileirão de 2023?", ["Palmeiras", "Botafogo", "Flamengo", "Grêmio"], "Palmeiras"),
    ],
    "Libertadores": [
        ("Quem venceu a Libertadores 2019?", ["Flamengo", "River Plate", "Palmeiras", "Grêmio"], "Flamengo"),
        ("Quem venceu a Libertadores 2023?", ["Fluminense", "Boca Juniors", "Palmeiras", "Grêmio"], "Fluminense"),
    ]
}

# =========================================
# QUIZ
# =========================================

class Quiz:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry("800x550")
        self.root.configure(bg="black")

        self.player = ""
        self.score = 0
        self.combo = 0
        self.index = 0
        self.time_left = TIME_PER_QUESTION
        self.paused = False
        self.timer_id = None # Armazena o ID do timer para poder cancelar

        self.start_screen()

    def clear(self):
        """Limpa todos os widgets da tela."""
        if self.timer_id:
            self.root.after_cancel(self.timer_id) # Para o timer ao limpar a tela
            self.timer_id = None
        for widget in self.root.winfo_children():
            widget.destroy()

    def start_screen(self):
        self.clear()
        tk.Label(self.root, text=APP_TITLE, font=("Helvetica", 24, "bold"), bg="black", fg="white").pack(pady=30)

        self.name_entry = tk.Entry(self.root, font=("Helvetica", 14), justify="center")
        self.name_entry.pack(pady=10)
        self.name_entry.insert(0, "Nome do jogador")

        for mode in QUESTIONS.keys():
            tk.Button(
                self.root, text=mode, font=("Helvetica", 13), width=25,
                bg=THEMES[mode], fg="white",
                command=lambda m=mode: self.start_quiz(m)
            ).pack(pady=6)

        tk.Button(self.root, text="TOP 10", font=("Helvetica", 12), command=self.show_ranking).pack(pady=20)

    def start_quiz(self, mode):
        # Captura o nome e prepara as perguntas
        nome = self.name_entry.get().strip()
        self.player = nome if nome and nome != "Nome do jogador" else "Jogador"
        self.mode = mode
        self.questions = QUESTIONS[mode][:] # Copia a lista original
        random.shuffle(self.questions) # Embaralha uma vez no início

        self.score = 0
        self.combo = 0
        self.index = 0
        self.next_question()

    def next_question(self):
        self.clear()
        
        if self.index >= len(self.questions):
            self.finish()
            return

        self.time_left = TIME_PER_QUESTION
        self.paused = False

        question, options, self.correct = self.questions[self.index]
        
        # Embaralha as opções para não ficarem sempre na mesma ordem
        opts_shuffled = options[:]
        random.shuffle(opts_shuffled)

        self.timer_label = tk.Label(self.root, text=f"Tempo: {self.time_left}s", font=("Helvetica", 12), bg="black", fg="white")
        self.timer_label.pack(pady=5)

        tk.Label(self.root, text=f"Questão {self.index + 1} de {len(self.questions)}", font=("Helvetica", 10), bg="black", fg="gray").pack()

        tk.Label(self.root, text=question, font=("Helvetica", 16), wraplength=700, bg="black", fg="white").pack(pady=30)

        for opt in opts_shuffled:
            tk.Button(self.root, text=opt, font=("Helvetica", 12), width=30, command=lambda o=opt: self.answer(o)).pack(pady=4)

        self.btn_pause = tk.Button(self.root, text="⏸ Pausar", command=self.toggle_pause)
        self.btn_pause.pack(pady=10)

        self.countdown()

    def countdown(self):
        if not self.paused and self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Tempo: {self.time_left}s")
            self.timer_id = self.root.after(1000, self.countdown)
        elif self.time_left == 0:
            self.combo = 0
            self.index += 1
            self.next_question()

    def toggle_pause(self):
        self.paused = not self.paused
        if self.paused:
            self.btn_pause.config(text="▶️ Retomar")
        else:
            self.btn_pause.config(text="⏸ Pausar")
            self.countdown()

    def answer(self, selected_option):
        if selected_option == self.correct:
            self.combo += 1
            # Bônus por combo
            pontos = 2 if self.combo >= 2 else 1
            self.score += pontos
        else:
            self.combo = 0

        self.index += 1
        self.next_question()

    def finish(self):
        # Lógica de ranking melhorada
        if self.score <= 2: rank = "INICIANTE"
        elif self.score <= 4: rank = "GERACIONAL"
        elif self.score <= 7: rank = "ICÔNICO"
        else: rank = "LEGENDÁRIO"

        # Salva no arquivo
        with open(RANKING_FILE, "a", encoding="utf-8") as f:
            f.write(f"{self.player} | {self.mode} | {self.score} pts | {rank}\n")

        messagebox.showinfo("Fim de Jogo", f"Jogador: {self.player}\nPontuação: {self.score}\nRanking: {rank}")
        self.start_screen()

    def show_ranking(self):
        if not os.path.exists(RANKING_FILE):
            messagebox.showinfo("TOP 10", "Nenhum ranking salvo ainda!")
            return

        with open(RANKING_FILE, "r", encoding="utf-8") as f:
            linhas = f.readlines()
            # Pega as últimas 10 jogadas
            ultimas = linhas[-10:]
            ranking_texto = "".join(ultimas)

        messagebox.showinfo("Últimos Resultados", ranking_texto)

if __name__ == "__main__":
    root = tk.Tk()
    app = Quiz(root)
    root.mainloop()