import os
import tkinter as tk
import subprocess
import shutil
project_name = ''
project_description = ''

def get_project_info():
    global project_name
    global project_description
    project_name = name_entry.get()
    project_description = description_entry.get() 
    print(f"Project Name: {project_name}")
    print(f"Project description: {project_description}")
    root.destroy()  # Stop the GUI event loop

# Create the main window
root = tk.Tk()
root.title("Project Name Input")

# Create a label
name_label = tk.Label(root, text="Enter Project Name:")
name_label.pack()

# Create an entry widget
name_entry = tk.Entry(root)
name_entry.pack()

# Create a label
description_label = tk.Label(root, text="Enter Project Description:")
description_label.pack()

# Create an entry widget
description_entry = tk.Entry(root)
description_entry.pack()

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=get_project_info)
submit_button.pack()

# Start the GUI event loop
root.mainloop()

print(project_name)

commands = [
    " mkdir public &&  cd public &&  touch index.html",
]
combined_command = " && ".join(commands)
os.system(combined_command)

# Combine the commands into a single command string

commands = [
    " mkdir src && cd src && touch app.js && touch index.js",
]
combined_command = " && ".join(commands)
os.system(combined_command)

commands = [
    "touch project_name.txt && touch project_desc.txt",
]
combined_command = " && ".join(commands)
os.system(combined_command)

source_dir = 'images'
dest_dir = 'src/images'

try:
  # Copy the entire contents of the source directory to the destination directory
  shutil.copytree(source_dir, dest_dir)
  print(f"Images copied from '{source_dir}' to '{dest_dir}' successfully.")
except Exception as e:
  print(f"Error copying images: {e}")

# creating projectname.txt
with open('project_name.txt', 'w') as file:
    file.write(project_name)
with open('project_desc.txt', 'w') as file:
    file.write(project_description)

package_json_content = f'''
{{
    "name": "{project_name}",
    "version": "1.0.0",
    "description": "{project_description}",
    "private": true,
  "dependencies": {{
    "@testing-library/jest-dom": "^5.17.0",
    "@testing-library/react": "^13.4.0",
    "@testing-library/user-event": "^13.5.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1",
    "web-vitals": "^2.1.4"
  }},
  "scripts": {{
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  }},
  "eslintConfig": {{
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  }},
  "browserslist": {{
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }}
}}'''
index_content = f'''

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta
      name="description"
      content={project_description}
    />
    <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
   
    <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
   
    <title>{project_name}</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
   
  </body>
</html>
'''

index_js = f'''

import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './app';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
'''
app_js = f'''
import React from 'react';
import {{ BrowserRouter as Router, Route, Routes }} from 'react-router-dom';

const About = () => <div>About Us Page</div>;
const Contact = () => <div>Contact Us Page</div>;

const App = () => {{
  return (
  <>
    <Router>
      <Routes>
        <Route path="/about" component={{About}} />
        <Route path="/contact" component={{Contact}} />
      </Routes>
    </Router>
  </>
  );
}};

export default App;
'''

# Save the package.json content to a file
with open('package.json', 'w') as file:
    file.write(package_json_content)

with open('public/index.html','w') as file:
    file.write(index_content)
    
with open("src/index.js",'w')as file:
    file.write(index_js)

with open("src/app.js",'w')as file:
    file.write(app_js)


# Commands to run in the background
commands = [
    "npm init -y",
]
for command in commands:
    os.system(command)

# subprocess.run(["python", "component_generator.py"])

commands = [
    "npm i",
    "npm install react-bootstrap bootstrap react-router-dom"
]
for command in commands:
    os.system(command)
commands = [
    "npm start",
]
for command in commands:
    os.system(command)
    
