import { AUTH_API_BASE_URL, BASE_REQUEST_HEADERS } from '../constants/api.constants';

export class AuthService {
    // need to see how to do session stuff
    async login (username, password) {
        const requestUrl = `${AUTH_API_BASE_URL}/login`
        
        const response = await fetch(requestUrl, {
            method: 'POST',
            headers: BASE_REQUEST_HEADERS,
            body: JSON.stringify({
                username: username,
                password: password
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
    }

    async register (username, password, firstName, lastName, email, balance) {
        const requestUrl = `${AUTH_API_BASE_URL}/register`;
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
                email: email,
                balance: Number(balance)
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        return data;
    }
}