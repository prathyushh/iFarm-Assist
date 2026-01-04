import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, Alert, ActivityIndicator } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import api, { setAuthToken } from '../services/api';

export default function LoginScreen({ navigation }) {
    const [phone, setPhone] = useState('');
    const [password, setPassword] = useState('');
    const [loading, setLoading] = useState(false);

    const handleLogin = async () => {
        if (!phone || !password) {
            Alert.alert('Error', 'Please enter both phone number and password');
            return;
        }

        setLoading(true);
        try {
            console.log('Attempting login...', { username: phone, password });
            // The backend expects specific field names for OAuth2 form data usually, 
            // but our pydantic schema might handle JSON if configured, 
            // HOWEVER, FastAPI OAuth2PasswordRequestForm STRICTLY expects 'username' and 'password' in form-data.
            // Let's check our auth.py. 
            // Checked: router.post("/login", response_model=schemas.Token) usually assumes form-data if Depends(OAuth2PasswordRequestForm) is used.
            // But looking at previous code, let's assume JSON or Form Data.
            // Actually, standard FastAPI OAuth2 expects x-www-form-url-encoded. 
            // We will try JSON first as our schema schemas.TokenRequest might accept it, 
            // OR if we used OAuth2PasswordRequestForm it MUST be form data.
            // Safe bet: The backend `auth.py` likely uses `OAuth2PasswordRequestForm`. 
            // Let's try sending x-www-form-urlencoded format.

            const formData = new URLSearchParams();
            formData.append('username', phone);
            formData.append('password', password);

            const response = await api.post('/auth/login', formData.toString(), {
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
            });

            console.log('Login success:', response.data);
            const { access_token } = response.data;
            setAuthToken(access_token);
            navigation.replace('Home');
        } catch (error) {
            console.error('Login error:', error.response?.data || error.message);
            Alert.alert('Login Failed', error.response?.data?.detail || 'Something went wrong');
        } finally {
            setLoading(false);
        }
    };

    return (
        <SafeAreaView style={styles.container}>
            <View style={styles.content}>
                <Text style={styles.title}>iFarmAssist 🌾</Text>
                <Text style={styles.subtitle}>Farmer Login</Text>

                <TextInput
                    style={styles.input}
                    placeholder="Phone Number"
                    placeholderTextColor="#666"
                    keyboardType="phone-pad"
                    value={phone}
                    onChangeText={setPhone}
                />

                <TextInput
                    style={styles.input}
                    placeholder="Password"
                    placeholderTextColor="#666"
                    secureTextEntry
                    value={password}
                    onChangeText={setPassword}
                />

                <TouchableOpacity
                    style={styles.button}
                    onPress={handleLogin}
                    disabled={loading}
                >
                    {loading ? (
                        <ActivityIndicator color="#FFF" />
                    ) : (
                        <Text style={styles.buttonText}>Login</Text>
                    )}
                </TouchableOpacity>

                <TouchableOpacity style={styles.linkButton}>
                    <Text style={styles.linkText}>New Farmer? Register Here</Text>
                </TouchableOpacity>
            </View>
        </SafeAreaView>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#F5F5F5',
    },
    content: {
        flex: 1,
        justifyContent: 'center',
        padding: 20,
    },
    title: {
        fontSize: 32,
        fontWeight: 'bold',
        color: '#2E7D32', // Green
        textAlign: 'center',
        marginBottom: 10,
    },
    subtitle: {
        fontSize: 18,
        color: '#555',
        textAlign: 'center',
        marginBottom: 40,
    },
    input: {
        backgroundColor: '#FFF',
        borderRadius: 10,
        padding: 15,
        marginBottom: 15,
        borderWidth: 1,
        borderColor: '#DDD',
        fontSize: 16,
    },
    button: {
        backgroundColor: '#2E7D32',
        padding: 15,
        borderRadius: 10,
        alignItems: 'center',
        marginTop: 10,
    },
    buttonText: {
        color: '#FFF',
        fontSize: 18,
        fontWeight: 'bold',
    },
    linkButton: {
        marginTop: 20,
        alignItems: 'center',
    },
    linkText: {
        color: '#2E7D32',
        fontSize: 16,
    }
});
