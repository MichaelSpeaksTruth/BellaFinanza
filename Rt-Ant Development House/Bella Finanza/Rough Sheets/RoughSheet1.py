import tkinter as tk
from tkinter import messagebox

print("")
print("")
# Predefined list of valid menu values
valid_values = ["1", "2", "3", "4", "5"]  # Example list, replace with your actual values

# Create the main window
root = tk.Tk()
root.title("Menu Input Example")

# Define the function to handle button click
def on_submit():
    init_input = entry.get()
    if init_input not in valid_values:
        messagebox.showerror("Error", "!! Error !!")
    else:
        messagebox.showinfo("Success", "Valid input!")
        # You can convert the input to an integer and do other processing here
        init_input = int(init_input)
        print(f"Valid input: {init_input}")

# Create a label and entry field
label = tk.Label(root, text="Enter Menu Value:")
label.pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=10)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()
