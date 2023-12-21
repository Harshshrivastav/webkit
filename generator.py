import os
import customtkinter as ctk 
import shutil
project_name = ''
project_description = ''

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("green") 
  
app = ctk.CTk() 
app.geometry("500x400") 
app.title("WEBKIT: Project Generator") 
  

def get_project_info():
    global project_name
    global project_description
    project_name = name_entry.get()
    project_description = description_entry.get() 
    print(f"Project Name: {project_name}")
    print(f"Project description: {project_description}")
    app.destroy() 
 
label = ctk.CTkLabel(app,text="WEB KIT") 
label.pack(pady=20) 
frame = ctk.CTkFrame(master=app) 
frame.pack(pady=20,padx=40,fill='both',expand=True) 
label = ctk.CTkLabel(master=frame,text='Generate React project') 
label.pack(pady=12,padx=10)

name_entry= ctk.CTkEntry(master=frame,placeholder_text="Project Name") 
name_entry.pack(pady=12,padx=10) 
  
description_entry= ctk.CTkEntry(master=frame,placeholder_text="Project Description") 
description_entry.pack(pady=12,padx=10) 

button = ctk.CTkButton(master=frame,text='Generate ',command=get_project_info) 
button.pack(pady=12,padx=10) 
app.mainloop()

print(project_name)

commands = [
    "mkdir public &&  cd public &&  touch index.html",
]
combined_command = " && ".join(commands)
os.system(combined_command)


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
    
commands = [
    "npm init -y",
]
for command in commands:
    os.system(command)

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
    print("writing Package.json...")

with open('public/index.html','w') as file:
    file.write(index_content)
    print("writing index.html...")

    
with open("src/index.js",'w')as file:
    file.write(index_js)
    print("writing index.js....")

with open("src/app.js",'w')as file:
    file.write(app_js)
    print("writing app.js....")


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
    
