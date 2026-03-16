import tkinter as tk
from tkinter import messagebox
import os
import sys

# --- FUNÇÃO PARA CAMINHOS (IMPORTANTE PARA O EXE) ---
def recurso_path(relative_path):
    """ 
    Obtém o caminho absoluto para o recurso. 
    Necessário para que o PyInstaller encontre as imagens na pasta temporária.
    """
    try:
        # Quando o PyInstaller roda o .exe, ele cria a variável sys._MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # Se estiver rodando como script .py normal, usa a pasta atual
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class JogoCartas:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Flip Card")
        self.root.geometry("400x500")

        # Configurar caminhos das imagens usando a função recurso_path
        # Certifique-se de que a pasta 'imagens' existe no seu projeto!
        try:
            caminho_verso = recurso_path(os.path.join("imagens", "verso.png"))
            # Se você tiver outras imagens, siga o mesmo padrão:
            # caminho_carta1 = recurso_path(os.path.join("imagens", "carta1.png"))
            
            self.img_verso = tk.PhotoImage(file=caminho_verso)
            print(f"Sucesso: Imagem carregada em {caminho_verso}")
        except Exception as e:
            messagebox.showerror("Erro Crítico", f"Não foi possível carregar as imagens:\n{e}")
            self.root.destroy()
            return

        # Interface simples de exemplo
        self.label_instrucao = tk.Label(root, text="Clique na carta para virar", font=("Arial", 12))
        self.label_instrucao.pack(pady=20)

        self.btn_carta = tk.Button(root, image=self.img_verso, command=self.virar_carta)
        self.btn_carta.pack(pady=10)

    def virar_carta(self):
        # Aqui entraria a lógica de mostrar a face da carta
        messagebox.showinfo("Jogo", "Você virou a carta!")

# --- INICIALIZAÇÃO ---
if __name__ == "__main__":
    root = tk.Tk()
    app = JogoCartas(root)
    root.mainloop()