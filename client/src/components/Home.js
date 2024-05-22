import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { AccountService } from '../services/account-service';
import { AuthService } from '../services/auth-service';

function Home() {
    // put reactive material here yada yada yada
    const [balance, setBalance] = useState(0);
    const [deposit, setDeposit] = useState(0);
    const [withdraw, setWithdraw] = useState(0);
    const [email, setEmail] = useState('');

    const routeNavigate = useNavigate();

    useEffect(() => {
        retrieveEmail();
        retrieveBalance();
    }, []);

    const retrieveEmail = async () => {
        // setEmail("testing@123.com");
        // Get user's email
    }

    const retrieveBalance = async () => {
        try {
            const accountService = new AccountService();
            const result = await accountService.viewBalance();
            setBalance(result.balance);
        } catch (e) {
            console.log("Error retrieving", e);
        }
    };

    const handleDeposit = async (e) => {
        try {
            e.preventDefault();

            const accountService = new AccountService();
            await accountService.deposit(deposit);
            retrieveBalance();
        }
        catch (e) {
            console.error(`error withdrawing: ${e}`);
        }
    };

    const handleWithdraw = async (e) => {
        try {
            e.preventDefault();

            const accountService = new AccountService();
            await accountService.withdraw(withdraw);
            retrieveBalance();
        }
        catch (e) {
            console.error(`error withdrawing: ${e}`);
        }
    };

    const handleLogout = async (e) => {
        try {
            e.preventDefault();
            const authService = new AuthService();
            await authService.logout();
            routeNavigate('/login');
        }
        catch (e) {
            console.error(`error logging out: ${e}`);
        }
    }
    
    return (
        <>
        <div>
            <p style={{  display: "inline", fontSize: "13px" }}><b>Account Email: </b></p>
            <div style={{ display: "inline", fontSize: "13px" }} dangerouslySetInnerHTML={{  __html: email }}></div>
        </div>
        <div style={{ display: "flex", justifyContent: "flex-end", marginTop: "20px", marginRight: "20px" }}>
            <button onClick={handleLogout}>Log Out</button>
        </div>
        <div className="container" style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
            <h1>Your Wallet</h1>
            <div style={{ marginBottom: "20px" }}><b>Account Balance: ${balance}</b></div>
            <form onSubmit={handleDeposit} style={{ marginBottom: "40px" }}>
                <div style={{ display: "flex", alignItems: "center" }}>
                    <label style={{ marginRight: "10px", width: "80px" }}>Deposit (USD): </label>
                    <input 
                        type="number" 
                        value={deposit}
                        onChange={(e) => setDeposit(e.target.value)}
                        min="0"
                    />
                </div>
                <button type="submit">Deposit</button>
            </form>

            <form onSubmit={handleWithdraw} style= {{ marginBottom: "20px" }}>
                <div style={{ display: "flex", alignItems: "center" }}>
                    <label style={{ marginRight: "10px", width: "80px" }}>Withdraw (USD): </label>
                    <input 
                        type="number" 
                        value={withdraw}
                        onChange={(e) => setWithdraw(e.target.value)}
                        min="0"
                    />
                </div>
                <button type="submit">Withdraw</button>
            </form>
        </div>
        </>
    );
}

export default Home;
