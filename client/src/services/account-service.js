import { ACCOUNT_API_BASE_URL, BASE_REQUEST_HEADERS } from '../constants/api.constants';

export class AccountService {
    async viewBalance () {
        const requestUrl = `${ACCOUNT_API_BASE_URL}/view_balance`
        
        await fetch(requestUrl, {
            method: 'GET',
            headers: BASE_REQUEST_HEADERS
        })
    }

    async deposit (amount) {
        const requestUrl = `${ACCOUNT_API_BASE_URL}/deposit`
        
        await fetch(requestUrl, {
            method: 'POST',
            headers: BASE_REQUEST_HEADERS,
            body: {
                'amount': amount
            }
        })
    }

    async withdraw (amount) {
        const requestUrl = `${ACCOUNT_API_BASE_URL}/withdraw`
        
        await fetch(requestUrl, {
            method: 'POST',
            headers: BASE_REQUEST_HEADERS,
            body: {
                'amount': amount
            }
        })
    }
}