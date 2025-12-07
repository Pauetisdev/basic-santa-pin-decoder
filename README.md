# santa-pin-decoder

This project is a simple Python program to solve a **Christmas coding challenge**. It decodes a ciphered code to find a **4-digit PIN**.

## 🛠️ Requirements

* **Python 3.10 or newer** (Needed for the `match/case` feature).

---

## ⚙️ How It Works (The Rules)

The code is made of blocks like `[nOP...]`.

* **Normal Block:** Starts with one digit (`n`), then has operations (`+` or `-`).
* **Special Block:** `[<]` means "repeat the last number."
* **Math Rule:** All math uses **Modulo 10** (Mod 10). (Example: $9 + 1 = 0$).
* **Final Goal:** The program must give exactly **4 digits**.

---
