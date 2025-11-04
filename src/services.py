import win32serviceutil
import win32service
import win32event
import servicemanager
import subprocess
import sys
import os

class UepaAuthService(win32serviceutil.ServiceFramework):
    _svc_name_ = "AuthSystemUEPA"               # Nome interno do serviço
    _svc_display_name_ = "Sistema de Login UEPA" # Nome visível no Windows
    _svc_description_ = "Gerencia a execução protegida do sistema de login UEPA."

    def __init__(self, args):
        super().__init__(args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)
        self.proc = None

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        if self.proc:
            self.proc.terminate()
        win32event.SetEvent(self.stop_event)

    def SvcDoRun(self):
        servicemanager.LogInfoMsg("✅ Iniciando o serviço AuthSystemUEPA...")

        # Caminho para o seu script principal (ajuste conforme sua estrutura)
        script_path = os.path.join(os.path.dirname(__file__), "main.py")

        # Inicia seu sistema (em modo protegido)
        self.proc = subprocess.Popen([sys.executable, script_path])

        # Espera até que o serviço seja interrompido
        win32event.WaitForSingleObject(self.stop_event, win32event.INFINITE)

        servicemanager.LogInfoMsg("🛑 Serviço AuthSystemUEPA encerrado.")


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(UepaAuthService)
