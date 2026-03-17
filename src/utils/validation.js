```javascript
export const validateEmail = (email) => {
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailRegex.test(email);
};

export const validateName = (name) => {
    const nameRegex = /^[a-zA-Z ]+$/;
    return nameRegex.test(name);
};

export const validateMessage = (message) => {
    return message.trim() !== '';
};
```

This code provides a basic structure for a fintech startup website with home, about, contact, and not found pages. The contact page includes a form that sends a POST request to the backend API. The API call is handled by the `contactApi` function in the `src/services/api.js` file. The form validation is handled by the `validateEmail`, `validateName`, and `validateMessage` functions in the `src/utils/validation.js` file.

Please note that you need to replace `https://your-backend-api.com/api` with your actual backend API URL.

Also, this code does not include any CSS styling. You can add CSS files to the `src` folder and import them in the corresponding components.

To run the application, navigate to the project directory and run `npm start`. The application will start on `http://localhost:3000`.