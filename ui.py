import tkinter as tk
from tkinter import messagebox
import subprocess

class CryptoBotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Crypto Trading Bot")

        self.start_button = tk.Button(root, text="Start Bot", command=self.start_bot)
        self.start_button.pack(pady=20)

    def start_bot(self):
        try:
            subprocess.run(["python", "bot.py"])
            messagebox.showinfo("Success", "Bot started successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start bot: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoBotApp(root)
    root.mainloop()
