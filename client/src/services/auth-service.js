import { AUTH_API_BASE_URL, BASE_REQUEST_HEADERS } from '../constants/api.constants';

export class AuthService {
    // need to see how to do session stuff
    async login (username, password) {
        const requestUrl = `${AUTH_API_BASE_URL}/login`
        
        await fetch(requestUrl, {
            method: 'POST',
            headers: BASE_REQUEST_HEADERS,
            body: JSON.stringify({
                'username': username,
                'password': password
            })
        })
    }

    async register (username, password, firstName, lastName, balance) {
        const requestUrl = `${AUTH_API_BASE_URL}/register`;
    
        try {
            const response = await fetch(requestUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    username: username,
                    password: password,
                    firstname: firstName,
                    lastname: lastName,
                    email: null, // PLACEHOLDER - populate with form field here
                    balance: Number(balance)
                })
            });
    
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
    
            const data = await response.json();
            return data;
        } catch (error) {
            console.error('There was a problem with the fetch operation:', error);
        }
    }
}