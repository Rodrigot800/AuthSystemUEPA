import keyboard
import threading

# Teclas únicas
TECLAS_BLOQUEADAS = ["win", "esc", "alt", "tab", "ctrl", "shift"]

# Combinações específicas
ATALHOS_BLOQUEADOS = [
    "alt+tab",
    "alt+f4",
    "ctrl+esc",
    "alt+esc",
    "ctrl+shift+esc",
    "win+d",
    "win+l",
    "win+e",
    "win+r"
]

ganchos = []
bloqueio_ativo = False

def bloquear_teclas():
    """Bloqueia teclas e atalhos comuns de navegação."""
    global bloqueio_ativo
    if bloqueio_ativo:
        return
    bloqueio_ativo = True

    # Bloquear teclas únicas
    for tecla in TECLAS_BLOQUEADAS:
        try:
            keyboard.block_key(tecla)
        except Exception as e:
            print(f"Erro ao bloquear {tecla}: {e}")

    # Bloquear atalhos compostos
    for atalho in ATALHOS_BLOQUEADOS:
        try:
            hook = keyboard.add_hotkey(atalho, lambda: None, suppress=True)
            ganchos.append(hook)
        except Exception as e:
            print(f"Erro ao bloquear {atalho}: {e}")

    print("✅ Bloqueio de teclas ativado.")

def desbloquear_teclas():
    """Remove bloqueios de teclas."""
    global bloqueio_ativo
    if not bloqueio_ativo:
        return

    try:
        for tecla in TECLAS_BLOQUEADAS:
            keyboard.unblock_key(tecla)
        for hook in ganchos:
            keyboard.remove_hotkey(hook)
        keyboard.unhook_all()
        ganchos.clear()
    except Exception as e:
        print(f"Erro ao desbloquear teclas: {e}")

    bloqueio_ativo = False
    print("🔓 Bloqueio de teclas desativado.")
