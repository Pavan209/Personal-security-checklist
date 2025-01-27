from flask import Flask, render_template, request

app = Flask(__name__)

# Security recommendations based on answers
RECOMMENDATIONS = {
    "password_manager": "Use a password manager to generate and store strong, unique passwords.",
    "2fa": "Enable Two-Factor Authentication (2FA) on all your accounts for added security.",
    "software_updates": "Keep your software and devices updated to patch vulnerabilities.",
    "public_wifi": "Avoid using public Wi-Fi without a VPN to protect your data.",
    "phishing": "Be cautious of phishing attempts. Verify links and email senders before clicking.",
    "device_lock": "Use strong passcodes or biometrics to lock your devices.",
    "backup": "Regularly back up your important data to a secure location.",
}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/results', methods=["POST"])
def results():
    # Collect user answers from the form
    responses = {
        "password_manager": request.form.get("password_manager"),
        "2fa": request.form.get("2fa"),
        "software_updates": request.form.get("software_updates"),
        "public_wifi": request.form.get("public_wifi"),
        "phishing": request.form.get("phishing"),
        "device_lock": request.form.get("device_lock"),
        "backup": request.form.get("backup"),
    }

    # Generate recommendations for "No" answers
    recommendations = [
        RECOMMENDATIONS[key] for key, value in responses.items() if value == "no"
    ]

    return render_template("results.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)