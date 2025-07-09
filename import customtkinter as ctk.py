import customtkinter as ctk

# Setup appearance
ctk.set_appearance_mode("System")  # Light / Dark / System
ctk.set_default_color_theme("blue")

# App window
app = ctk.CTk()
app.title("🌡️ Temperature Converter")
app.geometry("400x450")
app.resizable(False, False)

# Dropdown values
units = ["Celsius", "Fahrenheit", "Kelvin"]

# --- Conversion Logic ---
def convert_temp():
    try:
        temp = float(entry_temp.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()
        result = 0

        if from_unit == to_unit:
            result = temp

        elif from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                result = (temp * 9/5) + 32
            elif to_unit == "Kelvin":
                result = temp + 273.15

        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                result = (temp - 32) * 5/9
            elif to_unit == "Kelvin":
                result = (temp - 32) * 5/9 + 273.15

        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                result = temp - 273.15
            elif to_unit == "Fahrenheit":
                result = (temp - 273.15) * 9/5 + 32

        label_result.configure(text=f"Result: {result:.2f} {to_unit}")
    
    except ValueError:
        label_result.configure(text="❌ Please enter a valid number!")

# --- UI Layout ---
label_title = ctk.CTkLabel(app, text="🌡️ Temperature Converter", font=("Arial", 20, "bold"))
label_title.pack(pady=20)

entry_temp = ctk.CTkEntry(app, placeholder_text="Enter temperature")
entry_temp.pack(pady=10)

# --- From Unit ---
label_from = ctk.CTkLabel(app, text="From", font=("Arial", 14))
label_from.pack()
combo_from = ctk.CTkOptionMenu(app, values=units)
combo_from.set("Celsius")
combo_from.pack(pady=5)

# --- To Unit ---
label_to = ctk.CTkLabel(app, text="To", font=("Arial", 14))
label_to.pack()
combo_to = ctk.CTkOptionMenu(app, values=units)
combo_to.set("Fahrenheit")
combo_to.pack(pady=5)

# --- Convert Button ---
btn_convert = ctk.CTkButton(app, text="Convert", command=convert_temp)
btn_convert.pack(pady=20)

# --- Result Display ---
label_result = ctk.CTkLabel(app, text="", font=("Arial", 16))
label_result.pack(pady=10)

# Start the GUI
app.mainloop()