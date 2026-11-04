# lovetool.py - Python 3.11+, Termux
# Simulasi Package Manager "Love" + Chafa + Tema Merah
# pip install colorama
import time
import sys
import os
import subprocess
from colorama import Fore, Style, init

init(autoreset=True)

# GAMBAR PALING BAWAH
BG_IMAGE = "/storage/emulated/0/avg/e4d22d3b02274b84db518254c22c053f.jpg"

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def header():
    clear()
    if os.path.exists(BG_IMAGE):
        try:
            subprocess.run(["chafa", "--size", "50x25", BG_IMAGE], check=True)
        except:
            pass
    print(f"{Fore.RED}    [ Love Package Manager ]\n")

def menu():
    print(f"""{Fore.RED}
    ┌──────────────────────────────────────────────┐
    │  [1] Install Love                            │
    │  [2] Uninstall Love                          │
    │  [3] Search Love                             │
    │  [4] Blocked Love                            │
    │  [0] Exit                                    │
    └──────────────────────────────────────────────┘
        """)

def proses_loading(text, duration=2):
    print(f"{Fore.RED}[*] {text}", end="", flush=True)
    for _ in range(3):
        time.sleep(duration/3)
        print(".", end="", flush=True)
    print()

def main():
    while True:
        header()
        menu()
        
        choice = input(f"{Fore.RED}Love > {Style.RESET_ALL}").strip()
        
        if choice == "1":
            print(f"\n{Fore.RED}=== INSTALL LOVE ===")
            target = input(f"{Fore.RED}Masukkan Nama Target: {Style.RESET_ALL}")
            proses_loading(f"Mengunduh paket cinta untuk {target}")
            time.sleep(1)
            print(f"{Fore.RED}[+] Paket 'love_to_{target}.pkg' berhasil diinstal.")
            print(f"{Fore.RED}[+] Status: Siap dipakai. Jangan lupa kasih bunga. 🌹")
            input(f"\n{Fore.RED}Tekan Enter untuk kembali...")
            
        elif choice == "2":
            print(f"\n{Fore.RED}=== UNINSTALL LOVE ===")
            target = input(f"{Fore.RED}Masukkan Nama Target: {Style.RESET_ALL}")
            print(f"{Fore.RED}[!] Peringatan: Menghapus cinta bisa menyebabkan patah hati.")
            konfirmasi = input(f"{Fore.RED}Yakin ingin uninstall? (y/n): {Style.RESET_ALL}")
            if konfirmasi.lower() == 'y':
                proses_loading(f"Menghapus semua memori tentang {target}")
                time.sleep(1)
                print(f"{Fore.RED}[-] Paket cinta dihapus. Sisa sampah: Kenangan.")
                print(f"{Fore.RED}[-] Status: Move on dalam proses. 💔")
            else:
                print(f"{Fore.RED}[+] Uninstall dibatalkan. Cinta tetap terpasang.")
            input(f"\n{Fore.RED}Tekan Enter untuk kembali...")
            
        elif choice == "3":
            print(f"\n{Fore.RED}=== SEARCH LOVE ===")
            keyword = input(f"{Fore.RED}Masukkan kata kunci (misal: gebetan): {Style.RESET_ALL}")
            proses_loading(f"Mencari '{keyword}' di database semesta")
            time.sleep(1)
            print(f"{Fore.RED}[+] 1 hasil ditemukan: Seseorang yang diam-diam stalking sosmed lu.")
            print(f"{Fore.RED}[+] Peluang: 50% (tergantung keberanian).")
            input(f"\n{Fore.RED}Tekan Enter untuk kembali...")
            
        elif choice == "4":
            print(f"\n{Fore.RED}=== BLOCKED LOVE ===")
            target = input(f"{Fore.RED}Masukkan Nama Target: {Style.RESET_ALL}")
            proses_loading(f"Memblokir akses cinta dari {target}")
            time.sleep(1)
            print(f"{Fore.RED}[!] Paket diblokir oleh firewall hati.")
            print(f"{Fore.RED}[!] Alasan: Terlalu toxic / Ghosting / Friendzone.")
            print(f"{Fore.RED}[+] Status: Akses ditolak permanen.")
            input(f"\n{Fore.RED}Tekan Enter untuk kembali...")
            
        elif choice == "0":
            print(f"{Fore.RED}Keluar dari Love Package Manager. Semoga harimu menyenangkan! 👋")
            break
        else:
            print(f"{Fore.RED}[!] Pilihan tidak valid.")
            time.sleep(1)

if __name__ == "__main__":
    main()
