import os
import tkinter as tk
import shutil

component_name=""
def delete_component():
    global component_name
    component_name = component_name_entry.get()

    component_folder = f'src/components/{component_name}'
    if not os.path.exists(component_folder):
        print(f"Component '{component_name}' does not exist.")
        return

    # Remove the component folder
    shutil.rmtree(component_folder)

    # Update app.js to remove the component import and usage
    app_js_path = 'src/app.js'
    with open(app_js_path, 'r') as app_file:
        app_js = app_file.read()

    # Remove the import statement for the deleted component
    import_statement = f"import {component_name.title()} from './components/{component_name}/{component_name}'; \n"
    app_js = app_js.replace(import_statement, '')

    # Remove the component usage from the render method
    app_js = app_js.replace(f'<{component_name.title()} />', '')

    with open(app_js_path, 'w') as app_file:
        app_file.write(app_js)

    print(f"Component '{component_name}' deleted and app.js updated successfully.")
    root.destroy()

root = tk.Tk()
root.title("Delete Component")

# Component Name Label and Entry
component_name_label = tk.Label(root, text="Component Name:")
component_name_label.pack()
component_name_entry = tk.Entry(root)
component_name_entry.pack()

# Generate Button
generate_button = tk.Button(root, text="Delete Component", command=delete_component)
generate_button.pack()

root.mainloop()
