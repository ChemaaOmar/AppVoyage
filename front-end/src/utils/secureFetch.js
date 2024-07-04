// secureFetch.js

let csrfToken = null;

async function getCSRFToken() {
    if (!csrfToken) {
        const response = await fetch('http://localhost:5000/security/get-csrf-token', {
            credentials: 'include'  // Inclure les cookies dans la requête
        });
        const data = await response.json();
        csrfToken = data.csrf_token;
    }
    return csrfToken;
}

export async function secureFetch(url, options = {}) {
    const modeResponse = await fetch('http://localhost:5000/security/get-security-mode', {
        credentials: 'include'  // Inclure les cookies dans la requête
    });
    const modeData = await modeResponse.json();
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

    return fetch(url, {
        ...options,
        credentials: 'include'  // Inclure les cookies dans la requête
    });
}
