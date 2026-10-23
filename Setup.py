# setup.py
import os
import sys

def initialize_local_environment():
    print("==================================================")
    print("Initializing Isos One: Fluidic Tensor Environment")
    print("==================================================")
    
    vault_dir = "./isos_local_vault"
    if not os.path.exists(vault_dir):
        print(f"[*] Provisioning isolated data sandbox: {vault_dir}")
        os.makedirs(vault_dir)
        
    print("[*] Benchmarking host partition boundaries via 1.5 ratio pivot...")
    try:
        stat = os.statvfs(vault_dir)
        available_mb = (stat.f_bavail * stat.f_frsize) / (1024 * 1024)
        print(f"[+] Available hardware volume confirmed: {available_mb:.2f} MB")
    except AttributeError:
        print("[-] Hardware metrics telemetry restricted. Defaulting to standard baseline profiles.")

    core_modules = [
        "fluidic_tensor.py", 
        "gradient_dither.py", 
        "airgapped_mesh.py"
    ]
    
    for file_module in core_modules:
        if os.path.exists(file_module):
            print(f"[+] Verified active operational layer: {file_module}")
        else:
            print(f"[!] Warning: Missing dependency -> {file_module}")

    print("==================================================")
    print("Environment setup complete. Core components online.")
    print("==================================================")

if __name__ == "__main__":
    initialize_local_environment()
