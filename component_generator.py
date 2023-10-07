import tkinter as tk
from tkinter import messagebox
import os
component_name=""
component_content=""
def generate_component():
    global component_name
    global component_content
    component_name = component_name_entry.get()
    component_content = component_content_text.get("1.0", "end-1c")  # Get content from the Text widget

    # Create the React component directory
    component_directory = os.path.join("src", "components", component_name)
    os.makedirs(component_directory)

    # Create the React component JavaScript file
    with open(os.path.join(component_directory, f"{component_name}.js"), "w") as file:
        file.write(f"import React from 'react';\n\nfunction {component_name}() {{\n  return (\n    <div>\n      {component_content}\n    </div>\n  );\n}}\n\nexport default {component_name};\n")

    messagebox.showinfo("Component Created", f"React component '{component_name}' has been created!")
    root.destroy()
    
# Create the main window
root = tk.Tk()
root.title("React Component Generator")

# Component Name Label and Entry
component_name_label = tk.Label(root, text="Component Name:")
component_name_label.pack()
component_name_entry = tk.Entry(root)
component_name_entry.pack()

# Component Content Label and Textbox
component_content_label = tk.Label(root, text="Component Content:")
component_content_label.pack()
component_content_text = tk.Text(root, height=5, width=40)
component_content_text.pack()

# Generate Button
generate_button = tk.Button(root, text="Generate Component", command=generate_component)
generate_button.pack()

root.mainloop()

# Python script to insert a React component into app.js



# Read the app.js file
with open("src/app.js", "r") as file:
    lines = file.readlines()

# Find the line where you want to insert the component
insert_index = None
for i, line in enumerate(lines):
    if "</>" in line:
        insert_index = i
        break

if insert_index is not None:
    # Insert the new component content
    lines.insert(insert_index, f"      <{component_name.title()} />\n")

    # Write the modified content back to app.js
    with open("src/app.js", "w") as file:
        file.writelines(lines)
    print(f"Inserted {component_name} into app.js.")
else:
    print("Error: Could not find the insertion point in app.js.")


with open("src/app.js", 'r') as file:
    old_content = file.read()


with open("src/app.js", 'w') as file:
    new_data = f"import {component_name.title()} from './components/{component_name}/{component_name}' \n"
    file.write(new_data)
    file.write(old_content)