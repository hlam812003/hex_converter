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
        label_result.config(text=f"Result: {result}")
        # Update color preview if possible
        try:
            if result.startswith("#") and len(result) >= 7:
                preview_frame.config(bg=result[:7])
        except:
            pass
    except ValueError:
        messagebox.showerror("Error", "Opacity must be a number between 0 and 1.")

root = tk.Tk()
root.title("HEX Color Converter")
root.geometry("350x200")
root.resizable(False, False)
root.config(padx=20, pady=15)

# Center window on screen
root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (350 // 2)
y = (screen_height // 2) - (200 // 2)
root.geometry(f"350x200+{x}+{y}")

# Create frames for better organization
input_frame = tk.Frame(root)
input_frame.pack(fill="x", pady=(0, 10))

# HEX Color input
color_frame = tk.Frame(input_frame)
color_frame.pack(fill="x", pady=5)
tk.Label(color_frame, text="HEX Color:", width=10, anchor="w").pack(side="left")
entry_color = tk.Entry(color_frame)
entry_color.pack(side="left", padx=5, fill="x", expand=True)

# Opacity input
opacity_frame = tk.Frame(input_frame)
opacity_frame.pack(fill="x", pady=5)
tk.Label(opacity_frame, text="Opacity:", width=10, anchor="w").pack(side="left")
entry_opacity = tk.Entry(opacity_frame)
entry_opacity.pack(side="left", padx=5, fill="x", expand=True)
entry_opacity.insert(0, "1.0")

# Convert button
tk.Button(root, text="Convert", command=convert, width=10).pack(pady=5)

# Result frame
result_frame = tk.Frame(root)
result_frame.pack(fill="x", pady=5)

# Result label
label_result = tk.Label(result_frame, text="Result: #000000FF", font=("Courier", 11))
label_result.pack(side="left")

# Color preview 
preview_frame = tk.Frame(result_frame, width=30, height=25, bg="#000000", relief="solid", bd=1)
preview_frame.pack(side="right", padx=(10, 0))
# Ensure frame doesn't resize
preview_frame.pack_propagate(False)

# Help note
tk.Label(root, text="Format: #RRGGBBAA where AA is opacity", font=("Arial", 8), fg="gray").pack(pady=(10, 0))

root.mainloop()