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