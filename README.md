# Computer Village Parts Network

A private B2B platform designed to help laptop parts dealers in Computer Village quickly find and source laptop parts from other verified dealers.

The system allows dealers to post requests for specific laptop parts and receive responses from other shops that have the requested item available. Once a dealer responds, the request owner can initiate a private conversation to negotiate pricing and complete the transaction offline.

This platform is not a social media platform. It is a coordination tool built specifically for laptop parts dealers.

---

# Problem

Laptop parts dealers in Computer Village often struggle to quickly locate specific parts when customers request them.

Most dealers rely on WhatsApp groups, which are:

- noisy  
- unstructured  
- slow  
- difficult to search  
- filled with repeated messages  

Requests get buried quickly and finding a reliable supplier becomes inefficient.

---

# Solution

Computer Village Parts Network provides a structured request-based system where dealers can:

- Post laptop part requests  
- Respond with **"I Have It"**  
- Start a private one-to-one conversation with the request owner  
- Negotiate pricing privately  
- Complete transactions physically in their shops  

---

# Core Features

## Account Approval System

Only verified laptop part dealers can access the platform.

- Users register with phone or email  
- Admin manually approves accounts  
- Only approved users can access the system  

---

## Item Request System

Dealers can post requests for parts including:

- Category (Charger, Battery, Screen, Keyboard, Hinge)  
- Brand  
- Model  
- Description  
- Optional image  

Requests appear in a shared timeline visible to all approved dealers.

---

## "I Have It" Response System

Other dealers can respond to a request by clicking:

**I Have It**

This creates a visible response under the request showing which shops have the item available.

No pricing is shown publicly to prevent price wars.

---

## Private Messaging

Once a dealer responds to a request, the request owner can start a private chat.

Features:

- One-to-one messaging  
- Private negotiation  
- No public price discussions  
- Conversation linked to the request  

---

## Request Status System

Request owners can update the status of their request.

Possible statuses:

- Active  
- Negotiating  
- Bought  
- Cancelled  

Requests marked **Bought** are removed from the main timeline.

---

## Moderation System

To maintain trust within the network:

- Users can report other users  
- Reports increase a user's report count  
- Users with too many reports may be suspended  

---

# System Architecture

The project is structured into multiple Django apps to keep the system modular and scalable.

```
core/
accounts/
requests_app/
responses/
chat/
moderation/
notifications/
```

---

# Backend Optimizations

- Implemented Redis caching for frequently accessed GET endpoints to improve performance  
- Added database indexing and select_related optimizations to reduce query load  
- Applied pagination for efficient data loading in list views  
- Implemented rate limiting to prevent API abuse and spam requests  

---

### accounts
Handles user accounts and shop profiles.

### requests_app
Handles item requests posted by dealers.

### responses
Stores **"I Have It"** responses from other dealers.

### chat
Manages private conversations between dealers.

### moderation
Handles user reports and suspension logic.

### notifications
Manages in-app notifications.

---

# Request Flow

1. A dealer posts a laptop part request.
2. Other dealers respond by clicking **I Have It**.
3. The request owner sees the list of responders.
4. The owner selects a responder and starts a private chat.
5. Dealers negotiate privately.
6. The request owner updates the request status once the deal is complete.

---

# Technology Stack

**Backend**  
Django

**Database**  
PostgreSQL

**Authentication**  
Django Authentication System

**Messaging (MVP)**  
AJAX Polling

**Future Upgrade**  
Django Channels for real-time chat

---

# Future Features

Possible improvements after validation:

- Push notifications  
- Voice alerts for new requests  
- Dealer reputation system  
- Inventory listing  
- Phone repair parts support  
- Expansion beyond Computer Village  

---

# Important Product Focus

The biggest challenge for this platform is **adoption**, not technology.

The platform must onboard an initial group of Computer Village dealers so requests and responses happen consistently.

Without active dealers, the network will not function.

---

# API Structure

The platform exposes RESTful API endpoints for managing users, requests, responses, and messaging.

## Authentication

```
POST   /api/auth/register/
POST   /api/auth/login/
POST   /api/auth/logout/
GET    /api/auth/me/
```

---

## Accounts

```
GET    /api/accounts/profile/
PUT    /api/accounts/profile/update/
```

---

## Item Requests

```
GET    /api/requests/                # list active requests
GET   /api/requests?category=charger     # list active requests filterd by category

POST   /api/requests/create/        # create new request
GET    /api/requests/<id>/          # request details
PATCH  /api/requests/<id>/status/   # update request status
DELETE /api/requests/<id>/delete/
```

---

## Responses ("I Have It")

```
POST   /api/responses/<request_id>/respond/
GET    /api/responses/<request_id>/list/
```

---

## Conversations

```
POST   /api/chat/start/<request_id>/<seller_id>/
GET    /api/chat/conversations/
GET    /api/chat/<conversation_id>/
```

---

## Messages

```
GET    /api/chat/<conversation_id>/messages/
POST   /api/chat/<conversation_id>/send/
```

---

## Moderation

```
POST   /api/reports/report-user/
GET    /api/reports/my-reports/
```

---

# Getting Started

Follow the steps below to run the project locally.

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/computer-village-parts-network.git
cd computer-village-parts-network
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment.

### Windows

```bash
venv\Scripts\activate
```

### Mac / Linux

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Apply Database Migrations

```bash
python manage.py migrate
```

---

## 5. Create Superuser

```bash
python manage.py createsuperuser
```

This account will be used to approve dealer registrations from the admin panel.

---

## 6. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at:

```
http://127.0.0.1:8000/
```

---

# Admin Panel

Django admin can be accessed at:

```
http://127.0.0.1:8000/admin
```

Admin users can:

- approve dealer accounts
- suspend users
- monitor reports
- manage requests
- moderate conversations

---
