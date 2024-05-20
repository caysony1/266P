# 266P Bank Application (Spring 2024)

This is an intentionally vulnerable bank application for educational purposes only. 

Please do not use this in a real-life environment!

Instructions to run project. Order matters!

### Run the Server Side Project

1. Please download python3 if it is not on your machine yet. Go to (pick the right OS!):

    https://www.python.org/downloads/

2. Go to the root directory of the project (266P)

3. Run the following commands:

    `cd server`\
    `python3 -m venv .venv`

4. Activate python's virtual environment (command is based on OS used!):

    Windows: `.venv\Scripts\activate`\
    macOS/Linux: `source .venv/bin/activate`

5. In the virtual environment, utilize the package manager to install the 
dependencies for this project:

    `pip install -r dependencies.txt`

6. Run the following to activate the server-side application:

    `python3 main.py`

### Run the Client Side Project

1. In a separate Terminal window (this is important!), go back to the root directory of this project (266P)

2. Run the following commands:

    `cd client`\
    `npm install`

3. Run the client side application

    `npm run build`\
    `npm run start`

3. The browser should open with the client side project. If it does not automatically open, go to http://localhost:3000.

4. Happy vulnerability hunting!

### How to Terminate application

#### For Server Side Application

1. Go to the terminal window where the application is running
2. Press `Ctrl+C` on the keyboard
3. Type in `deactivate`
4. Successfully terminated server side application

#### For Client Side Application

1. Go to the terminal window where the application is running
2. Press `Ctrl+C` on the keyboard
3. Successfully terminated client side application