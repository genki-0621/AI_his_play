#!/usr/bin/env python3
import os, subprocess

ROOT = os.path.dirname(os.path.dirname(__file__))  # プロジェクト直下
MENU = {
  "1": ("XOR demo",          ["python", "-m", "apps.xor"]),
  "2": ("Troubleshooting",   ["python", "-m", "apps.troubleshooting"]),
  "3": ("Inventory demo",    ["python", "-m", "apps.inventory"]),
}

def main():
    print("== GENKI Portfolio Launcher ==")
    for k,(name,_) in MENU.items():
        print(f"[{k}] {name}")
    sel = input("Select: ").strip()
    cmd = MENU.get(sel)
    if not cmd:
        print("bye"); return
    # ここがキモ：プロジェクト直下で -m を実行
    subprocess.run(cmd[1], check=False, cwd=ROOT)

if __name__ == "__main__":
    main()
