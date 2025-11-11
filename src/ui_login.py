import tkinter as tk
from tkinter import messagebox
from src.hardware import bloquear_teclas
from src.network import login  # comunicação com o servidor

BASE = "http://localhost:5000"  # Endereço do seu servidor Flask


def iniciar_tela_login():
    janela = tk.Tk()
    janela.title("Sistema de Login - UEPA")

    # ---------- TELA CHEIA ----------
    largura = janela.winfo_screenwidth()
    altura = janela.winfo_screenheight()
    janela.geometry(f"{largura}x{altura}+0+0")
    #janela.overrideredirect(True)
    #janela.attributes("-topmost", True)
    janela.config(bg="#f5f6fa")

    # ---------- BLOQUEIOS ----------
    #bloquear_teclas()
    #janela.protocol("WM_DELETE_WINDOW", lambda: None)

    # ---------- INTERFACE ----------
    titulo = tk.Label(
        janela,
        text="🔐 Login - UEPA",
        font=("Segoe UI", 24, "bold"),
        bg="#f5f6fa",
        fg="#2f3640"
    )
    titulo.pack(pady=(100, 40))

    frame = tk.Frame(janela, bg="#f5f6fa")
    frame.pack(pady=20)

    lbl_login = tk.Label(frame, text="Usuário:", font=("Segoe UI", 14), bg="#f5f6fa")
    lbl_login.grid(row=0, column=0, sticky="e", padx=5, pady=5)
    entrada_login = tk.Entry(frame, width=30, font=("Segoe UI", 14))
    entrada_login.grid(row=0, column=1, padx=5, pady=5)

    lbl_senha = tk.Label(frame, text="Senha:", font=("Segoe UI", 14), bg="#f5f6fa")
    lbl_senha.grid(row=1, column=0, sticky="e", padx=5, pady=5)
    entrada_senha = tk.Entry(frame, width=30, font=("Segoe UI", 14), show="*")
    entrada_senha.grid(row=1, column=1, padx=5, pady=5)

    # ---------- FUNÇÃO DE LOGIN ----------
    def tentar_login():
        usuario = entrada_login.get().strip()
        senha = entrada_senha.get().strip()

        if not usuario or not senha:
            messagebox.showwarning("Campos vazios", "Por favor, preencha todos os campos.")
            return

        token = login(BASE, usuario, senha)

        if token:
            messagebox.showinfo("Sucesso", "✅ Acesso permitido!")
            janela.destroy()
            from src.ui_sair import iniciar_tela_sair
            iniciar_tela_sair(usuario)
        else:
            messagebox.showerror("Erro", "❌ Usuário ou senha incorretos.")

    # ---------- BOTÃO DE LOGIN ----------
    botao_login = tk.Button(
        janela,
        text="Entrar",
        command=tentar_login,
        font=("Segoe UI", 14, "bold"),
        bg="#273c75",
        fg="white",
        activebackground="#40739e",
        activeforeground="white",
        relief="flat",
        width=20,
        cursor="hand2"
    )
    botao_login.pack(pady=40)

    rodape = tk.Label(
        janela,
        text="© 2025 UEPA - Sistema de Login",
        font=("Segoe UI", 10),
        bg="#f5f6fa",
        fg="#718093"
    )
    rodape.pack(side="bottom", pady=10)

    janela.mainloop()
