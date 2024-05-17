import React, { useState } from 'react';
import { Link } from 'react-router-dom';

function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = () => {
        // Authenticate User and Go to Home page
    };

    return (
        <div className="container" style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
            <h1>SWE 266P - Bank App</h1>
            <h2>Login</h2>
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