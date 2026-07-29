# FastAPI Auth Boilerplate

A modular, lightweight authentication starter template built with FastAPI. This project demonstrates how to structure a backend application with clear separation between routing, schemas, and authentication logic.

## Features
- **Modular Structure**: Logic is separated into `main.py`, `auth.py`, and `schemas.py`.
- **User Authentication**: Register and Login endpoints with password hashing.
- **Security**: Uses `pwdlib` (Argon2) for secure password storage and `PyJWT` for token generation.
- **Validation**: Pydantic models for request validation.

## Prerequisites
- Python 3.10+
- `pip`

## Installation

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/Bohanos/FastAPI-Auth-Boilerplate.git](https://github.com/Bohanos/FastAPI-Auth-Boilerplate.git)
   cd FastAPI-Auth-Boilerplate