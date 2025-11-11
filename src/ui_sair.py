from src.hardware import desbloquear_teclas
from src.ui_login import iniciar_tela_login
import tkinter as tk
from tkinter import messagebox




def iniciar_tela_sair(usuario):
    #  Janela principal
    janela = tk.Tk()
    janela.title("Sessão Ativa - UEPA")
    janela.geometry("300x180")
    janela.config(bg="#f5f6fa")
    janela.resizable(False, False)
    #janela.protocol("WM_DELETE_WINDOW", lambda: None)

    # 🔓 Libera teclas bloqueadas
    desbloquear_teclas()

    lbl_usuario = tk.Label(
        janela,
        text=f"👤 Usuário: {usuario}",
        font=("Segoe UI", 11, "bold"),
        bg="#f5f6fa",
        fg="#2f3640"
    )
    lbl_usuario.pack(pady=(30, 20))

    def encerrar_sessao():
        confirmar = messagebox.askyesno("Encerrar sessão", "Deseja realmente sair?")
        if confirmar:
            janela.destroy()
            iniciar_tela_login()  # Volta para a tela de login

    botao_sair = tk.Button(
        janela,
        text="Sair",
        command=encerrar_sessao,
        font=("Segoe UI", 10, "bold"),
        bg="#c23616",
        fg="white",
        relief="flat",
        width=12,
        cursor="hand2"
    )
    botao_sair.pack(pady=10)

    janela.mainloop()
