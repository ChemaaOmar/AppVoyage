let csrfToken = null;

async function getCSRFToken() {
    if (!csrfToken) {
        const response = await fetch('http://localhost:5000/security/get-csrf-token', {
            credentials: 'include'  // Inclure les cookies dans la requête
        });
        if (!response.ok) {
            console.error('Failed to fetch CSRF token:', response);
            throw new Error('Failed to fetch CSRF token');
        }
        const data = await response.json();
        csrfToken = data.csrf_token;
    }
    return csrfToken;
}

export async function secureFetch(url, options = {}) {
    try {
        const modeResponse = await fetch('http://localhost:5000/security/get-security-mode', {
            credentials: 'include'  // Inclure les cookies dans la requête
        });
        if (!modeResponse.ok) {
            console.error('Failed to fetch security mode:', modeResponse);
            throw new Error(`Failed to fetch security mode: ${modeResponse.statusText}`);
        }
        const modeData = await modeResponse.json();
        console.log('Security mode:', modeData);
        const mode = modeData.mode;

        if (mode === 'secure') {
            const token = await getCSRFToken();
            options.headers = {
                ...options.headers,
                'X-CSRFToken': token,
                'Content-Type': 'application/json'
            };
        } else {
            options.headers = {
                ...options.headers,
                'Content-Type': 'application/json'
            };
        }

        const fetchResponse = await fetch(url, {
            ...options,
            credentials: 'include'  // Inclure les cookies dans la requête
        });

        if (!fetchResponse.ok) {
            console.error('Failed to fetch:', fetchResponse);
            throw new Error(`Failed to fetch: ${fetchResponse.statusText}`);
        }
        return fetchResponse;
    } catch (error) {
        console.error('Error in secureFetch:', error);
        throw error;
    }
}
