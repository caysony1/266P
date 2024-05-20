import { ACCOUNT_BASE_URL, BASE_REQUEST_HEADERS } from '../constants/api.constants';

export class AuthService {
    // need to see how to do session stuff
    async login (username, password) {
        const requestUrl = `${ACCOUNT_BASE_URL}/login`
        
        await fetch(requestUrl, {
            method: 'POST',
            headers: BASE_REQUEST_HEADERS,
            body: {
                'username': username,
                'password:': password
            }
        })
    }

    async register (username, password, firstName, lastName, balance) {
        const requestUrl = `${ACCOUNT_BASE_URL}/register`
        
        await fetch(requestUrl, {
            method: 'POST',
            headers: BASE_REQUEST_HEADERS,
            body: {
                'username': username,
                'password:': password,
                'firstname:': firstName,
                'lastname:': lastName,
                'balance': balance
            }
        })
    }
}