# **Frobarn Tailoring App - System Architecture Design**

## **1. Overview**

Frobarn is a technology company that connects users in the **USA** with tailors in **Africa** for custom clothing. The system integrates **AI-driven body measurement**, **order management**, and **logistics handling**, similar to how Uber connects riders with drivers.

---

## **2. System Components**

The application consists of **three main interfaces**:

### **1️⃣ User Web Interface**
- Users **select clothing designs** and proceed for measurements.
- Redirects users to **"Abody"**, an AI-powered body measurement tool.
- Receives measurement data via **cookies stored in the browser**.
- Sends measurement data to the backend via **Django API**.
- Stores measurements and user order details in the database.

### **2️⃣ Tailor Web Interface**
- Displays the **list of sewing requests** from users.
- Shows the **measurement data** for each request.
- Allows tailors to **update order status** as they work on it.

### **3️⃣ Frobarn Admin Interface**
- Manages **users, tailors, and order tracking**.
- Resolves disputes between **users and tailors**.
- Manages the **shipping process** of completed orders back to the USA.

---

## **3. System Workflow**

### **🔹 Step 1: User Selects Clothing Design**
- The user browses **available clothing designs**.
- Clicks **"Proceed to Measurement"** button.

### **🔹 Step 2: AI-Powered Body Measurement (Abody Integration)**
- User is redirected to **Abody**.
- Abody uses the **phone camera to take real-time body measurements**.
- The measurement data is **returned as cookies** to the user's browser.

### **🔹 Step 3: Sending Data to the Backend**
- The frontend extracts the **measurement data from cookies**.
- Sends the data to the **Django backend via API**.
- Stores **user order details and measurements in the database**.

### **🔹 Step 4: Tailor Processes the Order**
- The tailor sees the **new order request in the Tailor Web UI**.
- They use the **measurement data to start sewing**.
- Updates the **order status** (e.g., "In Progress", "Completed").

### **🔹 Step 5: Frobarn Oversees the Process & Shipping**
- Frobarn **manages the logistics** of sending the sewn clothes to the USA.
- Handles **dispute resolution** between users and tailors.
- Manages **payments and tailor payouts**.

---

## **4. System Architecture Diagram**

The architecture follows a **three-tier design**:

```
+--------------------------+      +-------------------------+      +-----------------------+
|   User Web Interface     | ---> |    Django Backend API   | ---> |  PostgreSQL Database  |
| (React.js/Next.js)       |      | (Django REST Framework) |      | (Stores user data)    |
+--------------------------+      +-------------------------+      +-----------------------+
       |                                                        |
       |                                                        |
       V                                                        |
+----------------+                                             |
|  Abody AI App | <---- (Redirect & Receive) -----------------|
| (3rd Party)   |                                             |
+----------------+                                             |
                                                              |
       +------------------------------------------------------+
       |
       V
+--------------------------+      +-------------------------+
|  Tailor Web Interface    | ---> |   Django Backend API   |
|  (React.js/Next.js)      |      |  (Processes Orders)    |
+--------------------------+      +-------------------------+

+--------------------------+      +-------------------------+
|  Frobarn Admin Interface | ---> |   Django Backend API   |
|  (React.js/Next.js)      |      |  (Admin Operations)    |
+--------------------------+      +-------------------------+
```

---

## **5. Technologies Used**

### **Frontend (User & Tailor Web UI)**
- **React.js / Next.js** (For a responsive UI)
- **Cookie storage** (For capturing Abody measurement data)
- **REST API calls** (To communicate with Django backend)

### **Backend (Django API)**
- **Django REST Framework (DRF)** (For API development)
- **PostgreSQL** (For storing user & tailor data)
- **Celery & Redis** (For asynchronous tasks like order notifications)

### **External Integration**
- **Abody AI App** (For real-time body measurements)
- **Stripe/PayPal** (For user payments and tailor payouts)
- **Shipping API** (To handle logistics of completed clothes)

### **Deployment & Infrastructure**
- **GitHub Actions** (For CI/CD)
- **Docker & Kubernetes** (For containerized deployments)
- **DigitalOcean Kubernetes** (For scalable backend hosting)

---

## **6. Security Considerations**
- **OAuth2 Authentication** (For secure user & tailor logins)
- **JWT Tokens** (For API security)
- **Data Encryption** (For securely storing user data)
- **Role-Based Access Control (RBAC)** (For admin, tailor, and user privileges)

---

## **7. Future Enhancements**
- **AI Recommendation System** (Suggest designs based on user preferences)
- **Multi-language Support** (For global accessibility)
- **Mobile App** (For users to track orders on mobile devices)
- **Chat Feature** (For direct user-tailor communication)

---

## **8. Summary**

This document outlines the **architecture and workflow** of the Frobarn tailoring platform, which connects **users in the USA with tailors in Africa**. The platform integrates **AI-powered body measurement**, **order management**, and **logistics tracking**, ensuring a seamless experience for both users and tailors.


