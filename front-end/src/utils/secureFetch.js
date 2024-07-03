// secureFetch.js

async function getCSRFToken() {
    const response = await fetch('http://localhost:5000/security/get-csrf-token');
    const data = await response.json();
    return data.csrf_token;
}

export async function secureFetch(url, options = {}) {
    const modeResponse = await fetch('http://localhost:5000/security/get-security-mode');
    const modeData = await modeResponse.json();
    const mode = modeData.mode;

    if (mode === 'secure') {
        const csrftoken = await getCSRFToken();
        options.headers = {
            ...options.headers,
            'X-CSRFToken': csrftoken
        };
    }

    return fetch(url, options);
}
