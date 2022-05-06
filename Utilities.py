import subprocess
import platform

def ClearTerminal():
    subprocess.Popen( "cls" if platform.system() == "Windows" else "clear", shell=True)
