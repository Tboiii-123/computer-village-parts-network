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
