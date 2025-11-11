# src/main.py         $ python -m src.main
from src.ui_login import iniciar_tela_login
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



def main():
    
    iniciar_tela_login()

if __name__ == "__main__":
    main()
