import tkinter as tk
from tkinter import messagebox

def hex_with_opacity(hex_color: str, opacity: float) -> str:
    hex_color = hex_color.lstrip("#")
    if len(hex_color) == 3:
        hex_color = ''.join([c * 2 for c in hex_color])
    if len(hex_color) != 6:
        return "Invalid hex color"
    if not (0 <= opacity <= 1):
        return "Opacity must be between 0 and 1"
    alpha = round(opacity * 255)
    alpha_hex = format(alpha, '02x')
    return f"#{hex_color}{alpha_hex}"

def convert():
    hex_color = entry_color.get()
    try:
        opacity = float(entry_opacity.get())
        result = hex_with_opacity(hex_color, opacity)
        global current_result
        current_result = result
        label_result.config(text=f"Result: {result}")
        try:
            if result.startswith("#") and len(result) >= 7:
                preview_frame.config(bg=result[:7])
                copy_button.config(state="normal")
            else:
                copy_button.config(state="disabled")
        except:
            copy_button.config(state="disabled")
    except ValueError:
        messagebox.showerror("Error", "Opacity must be a number between 0 and 1.")
        copy_button.config(state="disabled")

def copy_to_clipboard():
    if hasattr(root, 'clipboard_clear') and current_result.startswith('#') and len(current_result) >= 7:
        root.clipboard_clear()
        root.clipboard_append(current_result)
        copy_button.config(text="Copied!", bg="#8aff8a")
        root.after(1000, lambda: copy_button.config(text="Copy", bg="SystemButtonFace"))

current_result = "#000000FF"

root = tk.Tk()
root.title("HEX Color Converter")
root.geometry("350x230")
root.resizable(False, False)
root.config(padx=20, pady=15)

root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (350 // 2)
y = (screen_height // 2) - (220 // 2)
root.geometry(f"350x230+{x}+{y}")

input_frame = tk.Frame(root)
input_frame.pack(fill="x", pady=(0, 10))

color_frame = tk.Frame(input_frame)
color_frame.pack(fill="x", pady=5)
tk.Label(color_frame, text="HEX Color:", width=10, anchor="w").pack(side="left")
entry_color = tk.Entry(color_frame)
entry_color.pack(side="left", padx=5, fill="x", expand=True)

opacity_frame = tk.Frame(input_frame)
opacity_frame.pack(fill="x", pady=5)
tk.Label(opacity_frame, text="Opacity:", width=10, anchor="w").pack(side="left")
entry_opacity = tk.Entry(opacity_frame)
entry_opacity.pack(side="left", padx=5, fill="x", expand=True)
entry_opacity.insert(0, "1.0")

tk.Button(root, text="Convert", command=convert, width=10).pack(pady=5)

result_frame = tk.Frame(root)
result_frame.pack(fill="x", pady=5)

label_result = tk.Label(result_frame, text="Result: #000000FF", font=("Courier", 11))
label_result.pack(side="left")

preview_frame = tk.Frame(result_frame, width=30, height=25, bg="#000000", relief="solid", bd=1)
preview_frame.pack(side="right", padx=(10, 0))
preview_frame.pack_propagate(False)

copy_button = tk.Button(root, text="Copy", command=copy_to_clipboard, width=10, state="disabled")
copy_button.pack(pady=5)

tk.Label(root, text="Format: #RRGGBBAA where AA is opacity", font=("Arial", 8), fg="gray").pack(pady=(5, 0))

root.mainloop()