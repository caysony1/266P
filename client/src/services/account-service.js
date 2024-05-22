import { ACCOUNT_API_BASE_URL, BASE_REQUEST_HEADERS } from '../constants/api.constants';

export class AccountService {
    async viewEmail () {
        const requestUrl = `${ACCOUNT_API_BASE_URL}/view_email`
        
        const response = await fetch(requestUrl, {
            method: 'GET',
            headers: BASE_REQUEST_HEADERS,
            credentials: 'include'
        })

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status} - Unable to get email`);
        }

        return await response.json();
    }

    async viewBalance () {
        const requestUrl = `${ACCOUNT_API_BASE_URL}/view_balance`
        
        const response = await fetch(requestUrl, {
            method: 'GET',
            headers: BASE_REQUEST_HEADERS,
            credentials: 'include'
        })

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status} - Unable to get balance`);
        }

        return await response.json();
    }

    async deposit (amount) {
        const requestUrl = `${ACCOUNT_API_BASE_URL}/deposit`
        
        const response = await fetch(requestUrl, {
            method: 'POST',
            headers: BASE_REQUEST_HEADERS,
            credentials: 'include',
            body: JSON.stringify({
                amount: amount
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status} - Unable to deposit`);
        }

        return await response.json();
    }

    async withdraw (amount) {
        const requestUrl = `${ACCOUNT_API_BASE_URL}/withdraw`
        
        const response = await fetch(requestUrl, {
            method: 'POST',
            headers: BASE_REQUEST_HEADERS,
            credentials: 'include',
            body: JSON.stringify({
                amount: amount
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status} - Unable to withdraw`);
        }

        return await response.json();
    }
}