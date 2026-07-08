# MIGRATION REPORT

## C4 Level 2 Container Diagram

## Code Smells

### Code Smell 1

### Code Smell 2

### Code Smell 3

## Refactoring Process

## Manual AI Corrections

                    +----------------------+
                    |        User          |
                    +----------+-----------+
                               |
                               | Uses
                               v
+-------------------------------------------------------------------+
|                  Library Management System (Monolith)             |
|-------------------------------------------------------------------|
| Technology: Python                                                |
|                                                                   |
|  +----------------+                                               |
|  | app.py         |                                               |
|  |----------------|                                               |
|  | Entry Point    |                                               |
|  | Controls flow  |                                               |
|  +-------+--------+                                               |
|          |                                                        |
|          | calls                                                  |
|          v                                                        |
|  +----------------+                                               |
|  | auth.py        |                                               |
|  |----------------|                                               |
|  | User Login     |                                               |
|  | Authentication |                                               |
|  +-------+--------+                                               |
|          |                                                        |
|          | accesses                                               |
|          v                                                        |
|  +----------------+                                               |
|  | database.py    |                                               |
|  |----------------|                                               |
|  | Users          |                                               |
|  | Borrowed Books |                                               |
|  +-------+--------+                                               |
|          ^                                                        |
|          |                                                        |
|          | accesses                                               |
|  +-------+--------+                                               |
|  | processor.py   |                                               |
|  |----------------|                                               |
|  | Borrow Books   |                                               |
|  | View Books     |                                               |
|  +----------------+                                               |
|                                                                   |
+-------------------------------------------------------------------+

### Code Smell 1
Tight Coupling between app.py and processor.py.

### Code Smell 2
Global variables inside database.py.

### Code Smell 3
Authentication logic mixed directly into application flow.
## JWT Cryptographic Handshake

1. User enters username and password.
2. The authentication service validates the credentials.
3. A JWT is generated and digitally signed using HS256.
4. The token is returned to the client.
5. The client includes the token in future requests.
6. The server verifies the token signature before granting access.