import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, ScrollView, Alert, ActivityIndicator, KeyboardAvoidingView, Platform } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Mic, Camera, Send } from 'lucide-react-native';
import Markdown from 'react-native-markdown-display'; // Import Markdown
import api from '../services/api';

export default function HomeScreen() {
    const [query, setQuery] = useState('');
    const [response, setResponse] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleSubmit = async () => {
        if (!query.trim()) return;

        setLoading(true);
        setResponse(null); // Clear previous response

        try {
            // Backend expects Multipart/Form-Data
            const formData = new FormData();
            formData.append('input_type', 'TEXT');
            formData.append('original_input', query);

            console.log('Sending Query:', query);

            const res = await api.post('/query/submit', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });

            console.log('Query Response:', res.data);
            setResponse(res.data.ai_response_text);
            setQuery(''); // Clear the input box
        } catch (error) {
            console.error('Query Error:', error);
            Alert.alert('Error', 'Failed to get advice. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <KeyboardAvoidingView
            style={{ flex: 1 }}
            behavior={Platform.OS === "ios" ? "padding" : "height"}
        >
            <SafeAreaView style={styles.container}>
                <View style={styles.header}>
                    <Text style={styles.headerTitle}>iFarmAssist 🌿</Text>
                </View>

                <ScrollView contentContainerStyle={styles.content} keyboardShouldPersistTaps="handled">
                    {/* Welcome Message */}
                    {!response && !loading && (
                        <View style={styles.welcomeCard}>
                            <Text style={styles.welcomeText}>
                                Namaskaram! 🙏{'\n'}
                                Ask anything about farming in Kerala.
                            </Text>
                        </View>
                    )}

                    {/* Response Area */}
                    {loading && (
                        <View style={styles.loadingContainer}>
                            <ActivityIndicator size="large" color="#2E7D32" />
                            <Text style={styles.loadingText}>Thinking... 🚜</Text>
                        </View>
                    )}

                    {response && (
                        <View style={styles.responseCard}>
                            <Text style={styles.responseTitle}>Expert Advice:</Text>
                            {/* Render using Markdown Component */}
                            <Markdown style={markdownStyles}>
                                {response}
                            </Markdown>
                        </View>
                    )}
                </ScrollView>

                {/* Input Area */}
                <View style={styles.inputContainer}>
                    <View style={styles.actionButtons}>
                        <TouchableOpacity style={styles.iconButton} onPress={() => Alert.alert('Voice', 'Coming in Phase 5!')}>
                            <Mic color="#FFF" size={24} />
                        </TouchableOpacity>
                        <TouchableOpacity style={styles.iconButton} onPress={() => Alert.alert('Camera', 'Coming in Phase 5!')}>
                            <Camera color="#FFF" size={24} />
                        </TouchableOpacity>
                    </View>

                    <View style={styles.textInputWrapper}>
                        <TextInput
                            style={styles.textInput}
                            placeholder="Ask a question..."
                            value={query}
                            onChangeText={setQuery}
                            multiline
                        />
                        <TouchableOpacity style={styles.sendButton} onPress={handleSubmit} disabled={loading}>
                            <Send color="#2E7D32" size={24} />
                        </TouchableOpacity>
                    </View>
                </View>
            </SafeAreaView>
        </KeyboardAvoidingView>
    );
}

const markdownStyles = {
    body: {
        fontSize: 16,
        color: '#444',
        lineHeight: 24,
    },
    heading1: {
        fontSize: 20,
        fontWeight: 'bold',
        color: '#2E7D32',
        marginBottom: 10,
    },
    strong: {
        fontWeight: 'bold',
        color: '#333',
    },
    table: {
        borderWidth: 1,
        borderColor: '#ddd',
        borderRadius: 5,
        marginTop: 10,
        marginBottom: 10,
    },
    tr: {
        borderBottomWidth: 1,
        borderColor: '#ddd',
        flexDirection: 'row',
    },
    th: {
        flex: 1,
        padding: 5,
        fontWeight: 'bold',
        backgroundColor: '#f0f0f0',
    },
    td: {
        flex: 1,
        padding: 5,
    },
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#F5F5F5',
    },
    header: {
        padding: 20,
        backgroundColor: '#2E7D32',
        alignItems: 'center',
    },
    headerTitle: {
        fontSize: 24,
        fontWeight: 'bold',
        color: '#FFF',
    },
    content: {
        padding: 20,
        paddingBottom: 100, // Space for bottom input
    },
    welcomeCard: {
        backgroundColor: '#E8F5E9',
        padding: 20,
        borderRadius: 15,
        marginTop: 50,
        alignItems: 'center',
    },
    welcomeText: {
        fontSize: 18,
        color: '#2E7D32',
        textAlign: 'center',
        lineHeight: 28,
    },
    loadingContainer: {
        marginTop: 50,
        alignItems: 'center',
    },
    loadingText: {
        marginTop: 10,
        color: '#666',
        fontSize: 16,
    },
    responseCard: {
        backgroundColor: '#FFF',
        padding: 20,
        borderRadius: 15,
        elevation: 2,
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.1,
        shadowRadius: 4,
    },
    responseTitle: {
        fontSize: 18,
        fontWeight: 'bold',
        color: '#333',
        marginBottom: 10,
    },
    inputContainer: {
        position: 'absolute',
        bottom: 0,
        left: 0,
        right: 0,
        backgroundColor: '#FFF',
        padding: 15,
        borderTopWidth: 1,
        borderTopColor: '#DDD',
        flexDirection: 'row',
        alignItems: 'center',
    },
    actionButtons: {
        flexDirection: 'row',
        marginRight: 10,
    },
    iconButton: {
        backgroundColor: '#2E7D32',
        padding: 10,
        borderRadius: 25,
        marginRight: 10,
    },
    textInputWrapper: {
        flex: 1,
        flexDirection: 'row',
        alignItems: 'center',
        backgroundColor: '#F0F0F0',
        borderRadius: 25,
        paddingHorizontal: 15,
    },
    textInput: {
        flex: 1,
        height: 50,
        fontSize: 16,
        color: '#333',
    },
    sendButton: {
        padding: 5,
    }
});
