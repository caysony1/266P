import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { AuthService } from '../services/auth-service';

function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [invalidCred, setInvalidCred] = useState(false);

    const routeNavigate = useNavigate();

    const handleSubmit = (e) => {
        e.preventDefault();

        const authService = new AuthService();
        
        authService.login(username, password)
            .then(() => { 
                routeNavigate('/home');
            })
            .catch((e) => {
                console.error('There was a problem with the login operation:', e);
                setInvalidCred(true);
            });
    };

    return (
        <div className="container" style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
            <h1>SWE 266P - Bank App</h1>
            <h2 style={{ marginBottom: "5px" }}>Login</h2>
            <p style={{ color: "red", marginLeft: "5px", marginBottom: "5px", fontSize: "10px" }}>{invalidCred ? "Invalid Login Credentials" : ""}</p>
            <form onSubmit={handleSubmit}>
                <div className="form-group" style={{ display: "flex", alignItems: "center", marginBottom: "10px" }}>
                    <label style={{ marginRight: "10px", width: "80px" }}>Username: </label>
                    <input 
                        type="text" 
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        style={{ width: "200px" }}
                    />
                </div>
                <div className="form-group" style={{ display: "flex", alignItems: "center", marginBottom: "10px" }}>
                    <label style={{ marginRight: "10px", width: "80px" }}>Password: </label>
                    <input 
                        type="password" 
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        style={{ width: "200px" }}
                    />
                </div>
                <button type="submit">Login</button>
            </form>
            <Link to="/register"><button>Don't Have An Account</button></Link>
        </div>
    );
}

export default Login;
