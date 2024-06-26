import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { AuthService } from '../services/auth-service';

function Register() {
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [email, setEmail] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [accBalance, setAccBalance] = useState(0);
    const [invalids, setInvalids] = useState(false);
    
    const routeNavigate = useNavigate();

    const isValid = (input) => {
        const regex =  /^[_\-\.0-9a-z]+$/;
        return regex.test(input) && input.length >= 1 && input.length <= 127;
    }

    const isValidNumeric = (input) => {
        const regex = /^(0|[1-9][0-9]*)\.[0-9]{2}$/;
        return regex.test(input) && parseFloat(input) >= 0 && parseFloat(input) <= 4294967295.99;
    }

    const isValidEmail = (input) => {
        const regex = /^[a-zA-Z0-9@.]+$/;
        return regex.test(input);
    }

    const handleSubmit = (e) => {
        e.preventDefault();

        const tempInvalids = {};

        if (!isValidEmail(email)) {
            tempInvalids.email = true;
        }

        if (!isValid(firstName)) {
            tempInvalids.fname = true;
        }

        if (!isValid(lastName)) {
            tempInvalids.lname = true;
        }
        
        if (!isValid(username)) {
            tempInvalids.uname = true;
        }
        
        if (!isValid(password)) {
            tempInvalids.pword = true;
        }

        if (!isValidNumeric(accBalance)) {
            tempInvalids.balance = true;
        }

        if (Object.keys(tempInvalids).length >= 1) {
            setInvalids(tempInvalids);
            return;
        }

        const authService = new AuthService();
        
        authService.register(username, password, firstName, lastName, email, accBalance)
        .then(() => {
            setInvalids(false);
            routeNavigate('/home');
        })
        .catch((e) => {
            console.error('Register issue occurred:', e);
            setInvalids(true);
        });
    }

    return (
        <div className="container" style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
            <h1>Create Account</h1>
            <p style={{ color: "red", marginLeft: "5px", marginBottom: "5px", fontSize: "10px" }}>{invalids ? "Username is already taken" : ""}</p>

            <p style={{ fontSize: "10px" }}><b>**Every field must be specified.**</b></p>
            <ul style={{ fontSize: "10px", textAlign: "left", marginBottom: "20px" }}>
                <li style={{ marginBottom: "5px" }}><b>first name, last name, username, and password must contain only underscores, hyphens, dots, digits, and lowercase alphabetical characters</b></li>
                <li style={{ marginBottom: "5px" }}><b>first name, last name, username, and password must be between 1 and 127 characters long</b></li>
                <li><b>numeric inputs must contain two decimal places</b></li>
            </ul>
            <form onSubmit={handleSubmit}>
                <div style={{ display: "flex", alignItems: "center", marginBottom: "20px"}}>
                    <label style={{ marginRight: "10px", width: "80px" }}>First Name: </label>
                    <input 
                        type="text" 
                        value={firstName}
                        onChange={(e) => setFirstName(e.target.value)}
                    />
                    <p style={{ color: "red", marginLeft: "5px" }}>{invalids.fname ? "Invalid Input" : ""}</p>
                </div>
                <div style={{ display: "flex", alignItems: "center", marginBottom: "20px" }}>
                    <label style={{ marginRight: "10px", width: "80px" }}>Last Name: </label>
                    <input 
                        type="text" 
                        value={lastName}
                        onChange={(e) => setLastName(e.target.value)}
                    />
                    <p style={{ color: "red", marginLeft: "5px" }}>{invalids.lname ? "Invalid Input" : ""}</p>
                </div>
                <div style={{ display: "flex", alignItems: "center", marginBottom: "20px" }}>
                    <label style={{ marginRight: "10px", width: "80px" }}>Email Address: </label>
                    <input 
                        type="text" 
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                    />
                    <p style={{ color: "red", marginLeft: "5px" }}>{invalids.email ? "Invalid Input" : ""}</p>
                </div>
                <div style={{ display: "flex", alignItems: "center", marginBottom: "20px" }}>
                    <label style={{ marginRight: "10px", width: "80px" }}>Username: </label>
                    <input 
                        type="text" 
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                    />
                    <p style={{ color: "red", marginLeft: "5px" }}>{invalids.uname ? "Invalid Input" : ""}</p>
                </div>
                <div style={{ display: "flex", alignItems: "center", marginBottom: "20px" }}>
                    <label style={{ marginRight: "10px", width: "80px" }}>Password: </label>
                    <input 
                        type="password" 
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />
                    <p style={{ color: "red", marginLeft: "5px" }}>{invalids.pword ? "Invalid Input" : ""}</p>
                </div>
                <div style={{ display: "flex", alignItems: "center", marginBottom: "20px" }}>
                    <label style={{ marginRight: "10px", width: "80px" }}>Initial Account Balance (USD): </label>
                    <input 
                        type="text" 
                        value={accBalance}
                        onChange={(e) => setAccBalance(e.target.value)}
                    />
                    <p style={{ color: invalids.balance ? "red" : "black", marginLeft: "5px" }}>{invalids.balance ? "Invalid Input" : "e.g. \"5.00\""}</p>
                </div>
                <button type="submit">Register</button>
            </form>
            <Link to="/"><button>Cancel</button></Link>
        </div>
    );
}

export default Register;
