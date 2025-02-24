# 🔥 Gas Utility Service - Django Application  
A Django-based web application that allows customers to submit, track, and manage service requests for gas utilities. The system also provides an admin panel for support agents to handle customer requests efficiently.

---

## 📌 Features
✅ **User Registration & Login** (JWT Authentication)  
✅ **Submit Service Requests** (Gas Leakage, Billing Issues, New Connection)  
✅ **Track Service Request Status** (Open, In Progress, Resolved)  
✅ **Admin Panel for Support Agents**  
✅ **REST API Integration with Frontend (AJAX)**  
✅ **Fully Responsive UI (HTML, CSS, JavaScript)**  

---

## 📂 Project Structure


```
myproject/
│── myapp/                     # Main Django App
│   ├── migrations/            # Database Migrations
│   ├── templates/             # HTML Templates
│   │   ├── login.html         # Login Page
│   │   ├── register.html      # Registration Page
│   │   ├── dashboard.html     # User Dashboard
│   ├── views.py               # Handles Requests & Responses
│   ├── models.py              # Database Models
│   ├── serializers.py         # API Data Serialization
│   ├── urls.py                # URL Routing
│   ├── admin.py               # Django Admin Config
│── myproject/                 # Django Project Settings
│   ├── settings.py            # Project Configuration
│   ├── urls.py                # Main URL Routing
│── manage.py                  # Django Command-Line Utility
│── requirements.txt           # Python Dependencies
```

---

## 🚀 Installation & Setup
### 🔹 Step 1: Clone the Repository
Clone the repository and navigate into the project directory.
```sh
git clone https://github.com/sarthaktayal174/Gas-utility.git
cd myproject
```

### 🔹 Step 2: Set Up a Virtual Environment
Create and activate a virtual environment.
```
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```
### 🔹 Step 3: Install Dependencies
Install the required Python packages.
```
pip install -r requirements.txt
```
### 🔹 Step 4: Set Up the Database
Apply database migrations.
```
python manage.py makemigrations
python manage.py migrate
```
### 🔹 Step 5: Create a Superuser (For Admin Panel)
Create an admin user for managing service requests.
```
python manage.py createsuperuser
```
### 🔹 Step 6: Run the Development Server
Start the Django development server and access the application.
```
python manage.py runserver
```
---

## 🛠️ API Endpoints
| **Method** | **Endpoint**                | **Description**                     |
|-----------|----------------------------|-------------------------------------|
| **POST**  | `/api/register/`           | Register a new user                |
| **POST**  | `/api/login/`              | Authenticate & receive JWT token   |
| **GET**   | `/api/service-requests/`   | View user’s service requests       |
| **POST**  | `/api/service-requests/`   | Submit a new service request       |
| **PATCH** | `/api/service-requests/{id}/` | Update request status (admin only) |
| **DELETE** | `/api/service-requests/{id}/` | Delete a request (admin only)      |

To use the API, include the JWT token in headers:  
`Authorization: Bearer <your-access-token>`

---

## 🎨 Frontend Features
- Uses AJAX (JavaScript Fetch API) to interact with the Django REST API.
- Automatically loads user requests from the database.
- Users submit new requests without page reload.
- JWT Authentication for login & logout.

---

## 🎯 Future Enhancements
- ✅ Email Notifications when a request is updated.  
- ✅ Admin Dashboard UI for better request management.  
- ✅ Mobile-Friendly UI for better accessibility.  

---

## 🤝 Contributing
Contributions are welcome!  
1. Fork the repo  
2. Create a new branch (`feature-new-ui`)  
3. Commit changes  
4. Push to GitHub & open a **Pull Request**  

---

## 📜 License
This project is licensed under the **MIT License**.  

---

## 💡 Contact
If you have any questions or feedback, feel free to reach out:  
📧 Email: your-email@example.com  
🌍 GitHub: [your-username](https://github.com/your-username/)  

---

### 🎉 Now You Have a Fully Functional Gas Utility Service App! 🚀  
Let me know if you need any modifications! 😊

