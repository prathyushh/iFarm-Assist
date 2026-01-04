import axios from 'axios';
import { Platform } from 'react-native';

// Automatically detected IP: Local Network
const DEV_URL = process.env.EXPO_PUBLIC_API_URL;

if (!DEV_URL) {
    console.warn("⚠️ API URL is missing! Check mobile/.env");
}

const api = axios.create({
    baseURL: DEV_URL + '/api/v1',
    timeout: 120000,
    headers: {
        'Content-Type': 'application/json',
    },
});

export const setAuthToken = (token) => {
    if (token) {
        api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
    } else {
        delete api.defaults.headers.common['Authorization'];
    }
};

export default api;
