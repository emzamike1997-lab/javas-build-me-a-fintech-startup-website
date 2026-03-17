```javascript
import axios from 'axios';

const api = axios.create({
    baseURL: 'https://your-backend-api.com/api',
});

export const contactApi = async (name, email, message) => {
    try {
        const response = await api.post('/contact', { name, email, message });
        return response.data;
    } catch (error) {
        throw error;
    }
};
```

###