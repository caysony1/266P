# 266P Bank Application (Spring 2024)

This is an intentionally vulnerable bank application for educational purposes only. 

Please do not use this in a real-life environment!

Instructions to run project. Order matters!

1. Run the server side project using the command at the root directory:

    Windows: `python3 server\main.py`\
    MacOS/Linux: `python3 server/main.py`

2. If for the first time - set up the client side project. From the root directory, run the following in order:

    `cd server`
    `npm install` 

3. Run the client side application

    `npm run build`
    `npm run start`

3. The browser should open with the client side project. If it does not automatically open, go to http://localhost:3000.

4. Hacking vulnerability hunting!

To terminate either server or client side projects --> just do Control + C within the respective folder (/client and /server folders) 