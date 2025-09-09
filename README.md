# task-manager-fastapi

# User Management System  

A simple user management system with **JWT authentication** and **route protection**, following the best practice of separating **user profile data** from **user credentials** (“Profile-Per-User” model).  

---

## Features
- **Register New Users**  
  - Stores user profile data and credentials in separate tables.  
  - Passwords are hashed before storage for security.  
- **Login with JWT Authentication**  
  - Generates secure tokens for authenticated sessions.  
- **Protected Routes**  
  - Only logged-in users can access certain endpoints.  
- **Session Management**  
  - Active sessions are tracked, and users can log out anytime.  

---

## Database Schema  

### 1. User Table  

| Column        | Type        | Description                     |
|---------------|------------|---------------------------------|
| userID         | INT (PK)    | Unique ID for the user           |
| username       | VARCHAR     | Unique username                  |
| name           | VARCHAR     | Full name of the user            |
| DOB            | DATE        | Date of birth                    |
| email          | VARCHAR     | User’s email                     |
| created_at     | TIMESTAMP   | Record creation timestamp        |
| updated_at     | TIMESTAMP   | Record last update timestamp     |

---

### 2. User Credential Details Table  

| Column          | Type        | Description                                     |
|------------------|------------|-------------------------------------------------|
| credentialsID    | INT (PK)    | Unique ID for credentials record                |
| userID           | INT (FK)    | References User Table                            |
| hashed_password  | VARCHAR     | Securely hashed password                         |
| isCurrent        | BOOLEAN     | Indicates if this is the current password        |
| created_at       | TIMESTAMP   | When the password was created                    |

---

### 3. User Sessions Table  

| Column        | Type        | Description                             |
|---------------|------------|-----------------------------------------|
| sessionID      | INT (PK)    | Unique session ID                        |
| userID         | INT (FK)    | References User Table                    |
| created_at     | TIMESTAMP   | When the session was created             |
| is_active      | BOOLEAN     | Indicates if the session is active        |

---

## Services Required  

| Service Name             | Description                                       |
|---------------------------|--------------------------------------------------|
| `create_new_user`          | Sign up → Add user details & credentials          |
| `update_user_password`     | Change Password → Add new credentials record      |
| `create_new_session`       | Sign in → Verify credentials, generate JWT token  |
| `update_session`           | Logout → Mark session inactive                   |
| `update_user_details`      | Update profile data → Modify user table fields    |

---

## Interesting Points  

- **Profile-Per-User Pattern**: Separating **profile data** (e.g., name, email, DOB) from **credentials** (passwords) improves security and flexibility.  
- **Password Rotation Support**: Multiple records for credentials allow tracking password history.  
- **Session Management**: Maintains active/inactive sessions for security and audit purposes.  

---

## Suggested Tech Stack  

- **Backend**: Node.js / Express or Python / FastAPI  
- **Database**: PostgreSQL / MySQL  
- **Authentication**: JWT (JSON Web Tokens)  
- **Password Hashing**: bcrypt / Argon2  

---

## Setup Instructions  

1. Clone the repository:  
   ```bash
   git clone <repo-url>
   cd user-management-system