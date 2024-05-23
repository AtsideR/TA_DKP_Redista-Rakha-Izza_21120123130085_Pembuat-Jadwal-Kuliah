import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter.ttk import Combobox
import pandas as pd

class jadwalkuliah:
    #
    def __init__(self, master):
        self.master = master
        self.master.title("Pembuat Jadwal Kuliah")
        self.mode_gelap = False  # default mode terang
        self.jadwal = {hari: [] for hari in ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]}
        self.hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
        self.jam = [str(jam).zfill(2) for jam in range(24)]
        self.menit = [str(menit).zfill(2) for menit in range(0, 60, 5)]

        self.set_theme()
        self.buat_widgets()

    # function untuk mengatur tema
    def set_theme(self):
        if self.mode_gelap:
            self.bg_color = "#2c3e50"
            self.fg_color = "#ecf0f1"
            self.btn_color = "#34495e"
            self.text_area_color = "#7f8c8d"
        else:
            self.bg_color = "#ecf0f1"
            self.fg_color = "#2c3e50"
            self.btn_color = "#bdc3c7"
            self.text_area_color = "#ffffff"

        self.master.configure(bg=self.bg_color)

    # untuk membuat widget2/tool2 pada program
    def buat_widgets(self):
        self.text_area_hari = {}
        self.selected_day = tk.StringVar()
        
        # grid = untuk mengatur lokasi tool pada program
        # label = untuk menuliskan kata yang akan muncul di program
        # combobox = untuk membuat tombol list pada program
        # button = untuk membuat tombol di program
        for i, hari in enumerate(self.hari):
            label1 = tk.Label(self.master, text=f"Jadwal {hari}", bg=self.bg_color, fg=self.fg_color, font=("Arial", 12, "bold"))
            label1.grid(row=1, column=i, padx=5, pady=5, sticky="nsew")
            text_area = tk.Text(self.master, height=25, width=20, state="disabled", bg=self.text_area_color, fg=self.fg_color, font=("Arial", 10))
            text_area.grid(row=2, column=i, padx=5, pady=5, sticky="nsew")
            self.text_area_hari[hari] = text_area
            
        label2 = tk.Label(self.master, text="PEMBUAT JADWAL", bg=self.bg_color, fg=self.fg_color, font=("Arial", 12, "bold"))
        label2.grid(row=0, column=len(self.hari)//2, padx=5, pady=5, sticky="nsew")
        
        tk.Label(self.master, text="Pilih Hari:", bg=self.bg_color, fg=self.fg_color, font=("Arial", 10)).grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.menu_hari = Combobox(self.master, height= 5, width= 8, textvariable=self.selected_day, values=self.hari, font=("Arial", 10), state= "readonly")
        self.menu_hari.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        tk.Label(self.master, text="Masukkan jadwal:", bg=self.bg_color, fg=self.fg_color, font=("Arial", 10)).grid(row=6, column=0, padx=5, pady=5, sticky="e")
        self.acara_entry = tk.Entry(self.master, font=("Arial", 10))
        self.acara_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")

        tk.Label(self.master, text="Jam Mulai:", bg=self.bg_color, fg=self.fg_color, font=("Arial", 10)).grid(row=7, column=0, padx=5, pady=5, sticky="e")
        self.jam_mulai_var = tk.StringVar()
        self.menit_mulai_var = tk.StringVar()
        self.menu_jam_mulai = Combobox(self.master, height= 5, width= 3, textvariable=self.jam_mulai_var, values=self.jam, font=("Arial", 10), state= "readonly")
        self.menu_jam_mulai.grid(row=7, column=1, padx=5, pady=5, sticky="w")
        self.menu_menit_mulai = Combobox(self.master, height= 5, width= 3, textvariable=self.menit_mulai_var, values=self.menit, font=("Arial", 10), state= "readonly")
        self.menu_menit_mulai.grid(row=7, column=2, padx=5, pady=5, sticky="w")

        tk.Label(self.master, text="Jam Selesai:", bg=self.bg_color, fg=self.fg_color, font=("Arial", 10)).grid(row=8, column=0, padx=5, pady=5, sticky="e")
        self.jam_selesai_var = tk.StringVar()
        self.menit_selesai_var = tk.StringVar()
        self.menu_jam_selesai = Combobox(self.master, height= 5, width= 3, textvariable=self.jam_selesai_var, values=self.jam, font=("Arial", 10), state= "readonly")
        self.menu_jam_selesai.grid(row=8, column=1, padx=5, pady=5, sticky="w")
        self.menu_menit_selesai = Combobox(self.master, height= 5, width= 3, textvariable=self.menit_selesai_var, values=self.menit, font=("Arial", 10), state= "readonly")
        self.menu_menit_selesai.grid(row=8, column=2, padx=5, pady=5, sticky="w")
        

        self.tambah_button = tk.Button(self.master, text="Tambah Acara", command=self.tambah_acara, bg=self.btn_color, fg=self.fg_color, font=("Arial", 10))
        self.tambah_button.grid(row=9, column=len(self.hari)//2, padx=5, pady=5, sticky="nsew")
        
        self.hapus_button = tk.Button(self.master, text="Hapus Jadwal", command=self.pilih_hari_hapus, bg=self.btn_color, fg=self.fg_color, font=("Arial", 10))
        self.hapus_button.grid(row=10, column=len(self.hari)//2, padx=5, pady=5, sticky="nsew")

        self.mode_button = tk.Button(self.master, text="Mode Gelap", command=self.toggle_mode, bg=self.btn_color, fg=self.fg_color, font=("Arial", 10))
        self.mode_button.grid(row=11, column=6, padx=5, pady=5, sticky="nsew")
        # Perbarui teks tombol mode
        self.mode_button.config(text="Mode Terang" if self.mode_gelap else "Mode Gelap")
        
        self.simpan_button = tk.Button(self.master, text="Simpan Jadwal", command=self.simpan_jadwal, bg=self.btn_color, fg=self.fg_color, font=("Arial", 10))
        self.simpan_button.grid(row=11, column=len(self.hari)//2, padx=5, pady=5, sticky="nsew")

        # untuk menkonfigurasi ukuran grid kolom
        for i in range(len(self.hari)):
            self.master.columnconfigure(i, weight=1)
        self.master.rowconfigure((0, 1), weight=1)

    # function buat nambahin acara di textarea
    def tambah_acara(self):
        hari = self.selected_day.get()
        acara = self.acara_entry.get()
        waktu_mulai = f"{self.jam_mulai_var.get()}:{self.menit_mulai_var.get()}"
        waktu_selesai = f"{self.jam_selesai_var.get()}:{self.menit_selesai_var.get()}"

        if hari and acara and waktu_mulai and waktu_selesai:
            waktu_mulai_menit = int(self.jam_mulai_var.get()) * 60 + int(self.menit_mulai_var.get())
            waktu_selesai_menit = int(self.jam_selesai_var.get()) * 60 + int(self.menit_selesai_var.get())

            # Memeriksa apakah waktu mulai lebih awal dari waktu selesai
            if waktu_mulai_menit >= waktu_selesai_menit:
                messagebox.showerror("Error", "Waktu mulai harus lebih awal dari waktu selesai.")
                return

            # Memeriksa apakah ada tabrakan jadwal
            for existing_mulai, existing_selesai, _ in self.jadwal[hari]:
                existing_mulai_menit = int(existing_mulai.split(':')[0]) * 60 + int(existing_mulai.split(':')[1])
                existing_selesai_menit = int(existing_selesai.split(':')[0]) * 60 + int(existing_selesai.split(':')[1])

                if not (waktu_selesai_menit <= existing_mulai_menit or waktu_mulai_menit >= existing_selesai_menit):
                    messagebox.showerror("Error", "Jadwal yang ditambahkan bertabrakan dengan jadwal lain.")
                    return

            self.jadwal[hari].append((waktu_mulai, waktu_selesai, acara))
            self.jadwal[hari].sort(key=lambda x: x[0])  # Urutkan acara berdasarkan waktu mulai
            self.perbarui_jadwal()
            self.acara_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Silakan isi semua kolom.")

    # function untuk memasukan jadwal di textarea
    def perbarui_jadwal(self):
        for hari, text_area in self.text_area_hari.items():
            text_area.config(state="normal")
            text_area.delete("1.0", tk.END)
            for waktu_mulai, waktu_selesai, acara in self.jadwal[hari]:
                text_area.insert(tk.END, f"{waktu_mulai} - {waktu_selesai}: {acara}\n")
            text_area.config(state="disabled")

    # metode untuk mengubah mode gelap dan terang
    def toggle_mode(self):
        self.mode_gelap = not self.mode_gelap
        self.set_theme()
        self.buat_widgets()

    # method untuk membuat penghapus jadwal  
    def pilih_hari_hapus(self):
        self.hapus_window = tk.Toplevel(self.master)
        self.hapus_window.title("Pilih Hari")
        self.hapus_window.configure(bg=self.bg_color)

        tk.Label(self.hapus_window, text="Pilih Hari:", bg=self.bg_color, fg=self.fg_color, font=("Arial", 10)).pack(padx=5, pady=5)
        self.hari_listbox = tk.Listbox(self.hapus_window, selectmode=tk.SINGLE, bg=self.text_area_color, fg=self.fg_color, font=("Arial", 10))
        for hari in self.hari:
            self.hari_listbox.insert(tk.END, hari)
        self.hari_listbox.pack(padx=5, pady=5)

        self.pilih_button = tk.Button(self.hapus_window, text="Pilih", command=self.hapus_jadwal, bg=self.btn_color, fg=self.fg_color, font=("Arial", 10))
        self.pilih_button.pack(padx=5, pady=5)

    def hapus_jadwal(self):
        selected_hari_index = self.hari_listbox.curselection()
        if selected_hari_index:
            hari = self.hari_listbox.get(selected_hari_index[0])
            acara_list = [f"{waktu_mulai} - {waktu_selesai}: {acara}" for waktu_mulai, waktu_selesai, acara in self.jadwal[hari]]
            if not acara_list:
                messagebox.showinfo("Info", f"Tidak ada jadwal untuk {hari}.")
                self.hapus_window.destroy()
                return

            self.acara_hapus_window = tk.Toplevel(self.master)
            self.acara_hapus_window.title(f"Hapus Jadwal {hari}")
            self.acara_hapus_window.configure(bg=self.bg_color)

            tk.Label(self.acara_hapus_window, text=f"Pilih Jadwal di {hari}:", bg=self.bg_color, fg=self.fg_color, font=("Arial", 10)).pack(padx=5, pady=5)
            self.acara_listbox = tk.Listbox(self.acara_hapus_window, selectmode=tk.SINGLE, bg=self.text_area_color, fg=self.fg_color, font=("Arial", 10))
            for acara in acara_list:
                self.acara_listbox.insert(tk.END, acara)
            self.acara_listbox.pack(padx=5, pady=5)

            self.konfirmasi_hapus_button = tk.Button(self.acara_hapus_window, text="Hapus", command=lambda: self.konfirmasi_hapus_jadwal(hari), bg=self.btn_color, fg=self.fg_color, font=("Arial", 10))
            self.konfirmasi_hapus_button.pack(padx=5, pady=5)

            self.hapus_window.destroy()
        else:
            messagebox.showerror("Error", "Pilih hari yang ingin dihapus.")

    def konfirmasi_hapus_jadwal(self, hari):
        selected = self.acara_listbox.curselection()
        if selected:
            acara_hapus = self.acara_listbox.get(selected[0])
            for jadwal in self.jadwal[hari]:
                waktu_mulai, waktu_selesai, acara = jadwal
                if f"{waktu_mulai} - {waktu_selesai}: {acara}" == acara_hapus:
                    self.jadwal[hari].remove(jadwal)
                    self.perbarui_jadwal()
                    self.acara_hapus_window.destroy()
                    messagebox.showinfo("Info", "Jadwal berhasil dihapus.")
                    return
            messagebox.showerror("Error", "Jadwal tidak ditemukan.")
        else:
            messagebox.showerror("Error", "Pilih jadwal yang ingin dihapus.")
            
    def simpan_jadwal(self):
        df = []
        for hari, acara_list in self.jadwal.items():
            for waktu_mulai, waktu_selesai, acara in acara_list:
                df.append({"Hari": hari, "Waktu Mulai": waktu_mulai, "Waktu Selesai": waktu_selesai, "Acara": acara})

        df = pd.DataFrame(df)
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
        if file_path:
            df.to_excel(file_path, index=False)
            messagebox.showinfo("Info", f"Jadwal telah disimpan dalam file Excel di {file_path}.")
            
def main():
    root = tk.Tk()
    app = jadwalkuliah(root)
    root.mainloop()

if __name__ == "__main__":
    main()
