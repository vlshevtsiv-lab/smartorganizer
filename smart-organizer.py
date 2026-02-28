import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

EXTENTIONS = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
}

class SimpleOrganizer:
    def __init__(self, window):
        self.window = window
        self.window.title("Simple File Organizer")
        self.window.geometry("500x400")
        self.window.config(bg="#f0f0f0")

        self.selected_path = ""

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="File Organizer", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=20)
                    
        self.btn_select = tk.Button(self.window, text="Select Folder", command=self.select_folder,
                                    bg="#007bff", font=("Arial", 12))
        self.btn_select.pack(pady=10)

        self.label_path = tk.Label(self.window, text="No folder selected", bg="#f0f0f0", fg="gray")
        self.label_path.pack()

        self.log_box = tk.Text(self.window, width=50, height=10, font=("Consolas", 10))
        self.log_box.pack(pady=20, padx=20)

        self.btn_start = tk.Button(self.window, text="Start Organizing", command=self.start_sorting,
                                   state="disabled", bg="#28a745", font=("Arial", 12, "bold"))
        self.btn_start.pack(pady=10)

    def log(self, text):
        self.log_box.insert(tk.END, text + "\n")
        self.log_box.see(tk.END)

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.selected_path = folder
            self.label_path.config(text=f"Selected folder: {folder}", fg="black")
            self.btn_start.config(state="normal")
            self.log(f"Selected folder: {os.path.basename(folder)}")

    def start_sorting(self):
        count = 0
        self.log("Starting organization...")

        try:
            for filename in os.listdir(self.selected_path):
                file_path = os.path.join(self.selected_path, filename)

                if os.path.isdir(file_path):
                    continue

                ext = os.path.splitext(filename)[1].lower()

                moved = False
                for category, extensions in EXTENTIONS.items():
                    if ext in extensions:
                        dest_folder = os.path.join(self.selected_path, category)

                        if not os.path.exists(dest_folder):
                            os.makedirs(dest_folder)

                        shutil.move(file_path, os.path.join(dest_folder, filename))
                        self.log(f" {filename} -> {category}/")
                        count += 1
                        moved = True
                        break

                if not moved and ext != "":
                    other_folder = os.path.join(self.selected_path, "Other")
                    if not os.path.exists(other_folder):
                        os.makedirs(other_folder)
                    shutil.move(file_path, os.path.join(other_folder, filename))
                    self.log(f" {filename} -> Other/")
                    count += 1

            # finished looping through files
            messagebox.showinfo("Success", f"Done! sorted {count} files!")
            self.log(f"Done. Total files sorted: {count}")

        except Exception as e:
            messagebox.showerror("Oops!", f"An error occurred: {e}")
            
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleOrganizer(root)
    root.mainloop()