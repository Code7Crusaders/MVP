import sys
import os

# Imposta il percorso per importare i moduli dal backend
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.abspath(os.path.join(current_dir, "..", "src", "app"))
sys.path.insert(0, src_path)
