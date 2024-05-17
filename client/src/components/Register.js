import React, { useState } from 'react';
import { Link } from 'react-router-dom';

function Register() {
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [accBalance, setAccBalance] = useState(0);

    const handleSubmit = () => {
        // Register User and Go to Home page
    }

    return (
        <div className="container" style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
            <h1>Create Account</h1>
            <form onSubmit={handleSubmit}>
                <div style={{ display: "flex", alignItems: "center", marginBottom: "20px"}}>
                    <label style={{ marginRight: "10px", width: "80px" }}>First Name: </label>
                    <input 
                        type="text" 
                        value={firstName}
                        onChange={(e) => setFirstName(e.target.value)}
                    />
                </div>
                <div style={{ display: "flex", alignItems: "center", marginBottom: "20px" }}>
                    <label style={{ marginRight: "10px", width: "80px" }}>Last Name: </label>
                    <input 
                        type="text" 
                        value={lastName}
                        onChange={(e) => setLastName(e.target.value)}
                    />
                </div>
                <div style={{ display: "flex", alignItems: "center", marginBottom: "20px" }}>
                    <label style={{ marginRight: "10px", width: "80px" }}>Username: </label>
                    <input 
                        type="text" 
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                    />
                </div>
                <div style={{ display: "flex", alignItems: "center", marginBottom: "20px" }}>
                    <label style={{ marginRight: "10px", width: "80px" }}>Password: </label>
                    <input 
                        type="password" 
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />
                </div>
                <div style={{ display: "flex", alignItems: "center", marginBottom: "20px" }}>
                    <label style={{ marginRight: "10px", width: "80px" }}>Initial Account Balance (USD): </label>
                    <input 
                        type="number" 
                        value={accBalance}
                        onChange={(e) => setAccBalance(e.target.value)}
                    />
                </div>
                <button type="submit">Register</button>
            </form>
            <Link to="/"><button>Cancel</button></Link>
        </div>
    );
}

export default Register;