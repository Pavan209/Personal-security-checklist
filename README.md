# Personal-security-checklist
- Overview
The Personal Security Checklist is a web application designed to help individuals assess their digital security practices. By answering a series of yes/no questions, users can identify vulnerabilities in their habits and receive actionable recommendations to improve their security. The application is built using Python, Flask, and HTML/CSS.



- Features
 SelfAssessment: Users can evaluate their digital security practices by answering 7 key questions.
 Personalized Recommendations: Based on the user's responses, the app provides tailored advice for improving security.
 Simple and Interactive UI: Clean and responsive design for an intuitive user experience.
 Lightweight Application: Powered by Python's Flask framework for quick and efficient performance.



- Technologies Used
 Python: Core backend logic and Flask framework.
 Flask: For handling routes and processing user inputs.
 HTML/CSS: Frontend design for user interaction and recommendations.
 Bootstrap (Optional): For styling and responsiveness (if needed).



- How It Works
1. Checklist Questions:
    The user answers "Yes" or "No" to 7 questions covering areas such as password management, 2FA, software updates, public WiFi, phishing awareness, device security, and data backups.

2. Recommendations:
    For each "No" response, the app generates a corresponding recommendation to improve security practices.

3. Results Page:
    Displays the recommendations or congratulates the user for following all best practices.


- Security Practices Assessed
1. Password Manager: Do you use a password manager to store and generate strong passwords?
2. TwoFactor Authentication (2FA): Have you enabled 2FA for your accounts?
3. Software Updates: Are your software and devices regularly updated?
4. Public WiFi Usage: Do you avoid using public WiFi without a VPN?
5. Phishing Awareness: Are you cautious about phishing attempts and verify links before clicking?
6. Device Security: Do you use strong passcodes or biometrics to secure your devices?
7. Data Backup: Do you regularly back up important data to a secure location?


- Folder Structure
```
personalsecuritychecklist/
├── app.py  Flask application
├── templates/
│ ├── index.html  Home page with the checklist
│ ├── results.html  Results page with recommendations
├── static/
│ └── styles.css  CSS file for styling
```


- Features of Flask Implementation
 Dynamic Routing: Handles user inputs via `/` and `/results` routes.
 Form Data Handling: Collects answers from the user and dynamically generates recommendations.
 CSS Styling: Ensures the app is visually appealing and easy to navigate.


- Applications
 Personal Use: Empower individuals to identify and improve their digital security practices.
 Awareness Campaigns: Use the app in workshops or educational settings to promote cybersecurity awareness.
 Forensic Training: Help individuals understand key principles for safeguarding digital devices and data.


- Limitations
 Focuses only on basic security practices; it doesn't cover advanced or enterpriselevel security measures.
 Recommendations are generalized and may not apply to specific scenarios.
 No persistent data storage (user inputs are processed dynamically and not saved).

