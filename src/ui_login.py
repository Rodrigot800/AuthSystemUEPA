import tkinter as tk
from tkinter import messagebox
from src.auth import autenticar_cliente

from src.hardware import bloquear_teclas



def iniciar_tela_login():
    janela = tk.Tk()
    janela.title("Sistema de Login - UEPA")

    # ---------- TELA CHEIA REAL ----------
    largura = janela.winfo_screenwidth()
    altura = janela.winfo_screenheight()
    janela.geometry(f"{largura}x{altura}+0+0")  # Define o tamanho para a tela inteira
    janela.overrideredirect(True)               # Remove barra de título e bordas
    janela.attributes("-topmost", True)         # Sempre no topo
    janela.config(bg="#f5f6fa")

    bloquear_teclas()

    # # ---------- BLOQUEIOS ----------
    # janela.protocol("WM_DELETE_WINDOW", lambda: None)
    # janela.bind("<Alt-F4>", lambda e: "break")

    # def bloquear_teclas(event):
    #    return "break"

    # teclas_para_bloquear = [
    #     "<Escape>", "<Shift_L>", "<Shift_R>",
    #     "<Control_L>", "<Control_R>", "<Alt_L>", "<Alt_R>",
    #     "<F1>", "<F2>", "<F3>", "<F4>", "<F5>", "<F6>",
    #     "<F7>", "<F8>", "<F9>", "<F10>", "<F11>", "<F12>"
    # ]

    # for tecla in teclas_para_bloquear:
    #     janela.bind_all(tecla, bloquear_teclas)

    # Bloqueia as teclas Windows esquerda e direita
    # keyboard.block_key("windows")
    # keyboard.block_key("left windows")
    # keyboard.block_key("right windows")

    # Bloqueia combinações comuns como Win+R
    # keyboard.add_hotkey('windows+r', lambda: None)
    # keyboard.add_hotkey('windows+e', lambda: None)
    # keyboard.add_hotkey('windows+d', lambda: None)
    # keyboard.add_hotkey('windows+tab', lambda: None)

    # Bloqueia Esc, Shift, Ctrl, F1-F12
    # teclas = [
    #     "esc", "ctrl", "alt",
    #     "f1", "f2", "f3", "f4", "f5", "f6",
    #     "f7", "f8", "f9", "f10", "f11", "f12"
    # ]
    # for tecla in teclas:
    #     keyboard.block_key(tecla)
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

    def tentar_login():
        usuario = entrada_login.get().strip()
        senha = entrada_senha.get().strip()

        if not usuario or not senha:
            messagebox.showwarning("Campos vazios", "Por favor, preencha todos os campos.")
            return

        if autenticar_cliente(usuario, senha):
            janela.destroy()
        else:
            messagebox.showerror("Erro", "❌ Usuário ou senha incorretos.")

        if autenticar_cliente(usuario, senha):
            messagebox.showinfo("Sucesso", "✅ Acesso permitido!")
        
            from src.ui_sair import iniciar_tela_sair
            iniciar_tela_sair(usuario)


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

    rodape = tk.Label(janela, text="© 2025 UEPA - Sistema de Login",
                      font=("Segoe UI", 10), bg="#f5f6fa", fg="#718093")
    rodape.pack(side="bottom", pady=10)

    janela.mainloop()
