import tkinter as tk
import time

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Reloj Digital con Cronómetro")
        self.master.geometry("400x300")
        self.master.config(bg="lightblue")

        
        self.time_label = tk.Label(self.master, font=("Helvetica", 30), bg="lightblue")
        self.time_label.pack(fill=tk.X, pady=10)
        
        self.chrono_label = tk.Label(self.master, font=("Helvetica", 30), bg="lightblue")
        self.chrono_label.pack(fill=tk.X, pady=10)
        
        self.start_button = tk.Button(self.master, text="Iniciar Cronómetro", command=self.start_chrono)
        self.start_button.pack(pady=5)
        
        self.stop_button = tk.Button(self.master, text="Detener Cronómetro", command=self.stop_chrono)
        self.stop_button.pack(pady=5)
        
        self.reset_button = tk.Button(self.master, text="Reiniciar Cronómetro", command=self.reset_chrono)
        self.reset_button.pack(pady=5)
        
        self.chrono_running = False
        self.chrono_start = 0
        self.chrono_elapsed = 0
        
        self.update_clock()
        
    def start_chrono(self):
        self.chrono_running = True
        self.chrono_start = time.time()
        
    def stop_chrono(self):
        self.chrono_running = False
        self.chrono_elapsed = time.time() - self.chrono_start
        
    def reset_chrono(self):
        self.chrono_start = 0
        self.chrono_elapsed = 0
        
    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        
        if self.chrono_running:
            self.chrono_elapsed = time.time() - self.chrono_start
            self.chrono_label.config(text="{:.2f}".format(self.chrono_elapsed))
        else:
            self.chrono_label.config(text="{:.2f}".format(self.chrono_elapsed))
        
        self.master.after(100, self.update_clock)
        
root = tk.Tk()
app = App(root)
root.mainloop()
