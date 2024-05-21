import React, { useState, useEffect } from 'react';
import { AccountService } from '../services/account-service';

function Home() {
    // put reactive material here yada yada yada
    const [balance, setBalance] = useState(0);
    const [deposit, setDeposit] = useState(0);
    const [withdraw, setWithdraw] = useState(0);

    useEffect(() => {
        retrieveBalance();
    }, []);

    const retrieveBalance = async () => {
        try {
            const accountService = new AccountService();

            const res = await accountService.viewBalance(); // What is the res?
            setBalance(res);
        } catch (e) {
            console.log("Error retrieving", e);
        }
    };

    const handleDeposit = (e) => {
        e.preventDefault();

        const accountService = new AccountService();

        accountService.deposit(deposit).then(() => {
            retrieveBalance();
        });
    };

    const handleWithdraw = (e) => {
        e.preventDefault();

        const accountService = new AccountService();

        accountService.withdraw(withdraw).then(() => {
            retrieveBalance();
        });
    };
    
    return (
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
    );
}

export default Home;
