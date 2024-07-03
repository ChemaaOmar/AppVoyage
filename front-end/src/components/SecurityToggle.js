// import React, { useState, useEffect } from 'react';

// function SecurityToggle() {
//     const [mode, setMode] = useState('secure');

//     useEffect(() => {
//         const fetchSecurityMode = async () => {
//             const response = await fetch('http://localhost:5000/security/get-security-mode');
//             const data = await response.json();
//             setMode(data.mode);
//         };
//         fetchSecurityMode();
//     }, []);

//     const toggleSecurity = async () => {
//         const response = await fetch('http://localhost:5000/security/toggle-security', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json'
//             }
//         });
//         const data = await response.json();
//         setMode(data.mode);
//     };

//     return (
//         <div>
//             <button onClick={toggleSecurity}>
//                 Switch to {mode === 'secure' ? 'Insecure' : 'Secure'} Mode
//             </button>
//             <p>Current mode: {mode === 'secure' ? 'Secure' : 'Insecure'}</p>
//         </div>
//     );
// }

// export default SecurityToggle;
