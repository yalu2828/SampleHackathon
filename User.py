from fastapi import FastAPI

app = FastAPI()

# -------------------------------
# DEMO USER DATABASE (FAKE DATA)
# Intentionally insecure for CredSense AI demo
# -------------------------------

users = [
    {
        "username": "admin",
        "password": "Admin@123",
        "email": "admin@credsense.com",
        "role": "Administrator"
    },
    {
        "username": "yazhini",
        "password": "Yazhini@2026",
        "email": "yazhini@gmail.com",
        "role": "Developer"
    },
    {
        "username": "samvardhini",
        "password": "Sam@Secure456",
        "email": "samvardhini@gmail.com",
        "role": "Security Analyst"
    },
    {
        "username": "sudharshan",
        "password": "Sudharshan#789",
        "email": "sudharshan@gmail.com",
        "role": "Team Lead"
    }
]

# Fake API key (for demo scanning)
API_KEY = "sk-demo123456789abcdefghijklmnopqrstuvwxyz"

@app.get("/users")
def get_users():
    return users

@app.post("/login")
def login(username: str, password: str):
    for user in users:
        if user["username"] == username and user["password"] == password:
            return {
                "message": "Login Successful",
                "user": user["username"],
                "role": user["role"]
            }

    return {"message": "Invalid Username or Password"}