import tkinter as tk

windows = tk.Tk()

windows.title("Activation Window")

windows.geometry("400x500")
windows.resizable(False, False)
windows.configure(bg='white')


frame_header_box = tk.Frame(windows, width=400, height=20, bg='#F0F0F0')
frame_main_first = tk.Frame(windows, width=200, height=70, bg='white', 
                       highlightbackground="#BFBFBF", highlightthickness=1)
frame_main_second = tk.Frame(windows, width=200, height=150, bg='white', 
                       highlightbackground="#BFBFBF", highlightthickness=1)


frame_header_box.grid(row=0, column=0, columnspan=2)
frame_main_first.grid(row=1, column=0, columnspan=2, pady=30)
frame_main_second.grid(row=2, column=0, columnspan=2, pady=10)
windows.mainloop()

