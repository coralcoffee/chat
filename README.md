# Chat API

A modern, scalable chat API built with FastAPI, featuring user authentication, real-time messaging capabilities, and comprehensive API documentation.

## 🚀 Features

- **FastAPI Framework**: High-performance async API with automatic OpenAPI documentation
- **User Authentication**: JWT-based authentication with access and refresh tokens
- **User Management**: Complete user registration and profile management
- **Database Integration**: PostgreSQL with SQLAlchemy ORM and Alembic migrations
- **Security**: Password hashing with bcrypt, CORS middleware
- **API Versioning**: Structured API versioning with `/api/v1/` prefix
- **Health Checks**: Built-in health monitoring endpoints
- **Development Ready**: Hot reload, structured logging, and comprehensive error handling

## 📋 Requirements

- Python 3.11+
- PostgreSQL database
- Redis (optional, for caching and rate limiting)

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd chat
```

### 2. Create and activate virtual environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install .
```

### 4. Environment Configuration

Create a `.env` file in the root directory:

```env
APP_ENV=dev
APP_JWT_SECRET=your-secret-key-here
APP_DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/chat_db
APP_ENABLE_PROMETHEUS=false
```

### 5. Database Setup

Make sure PostgreSQL is running, then create the database:

```bash
createdb chat_db
```

Run database migrations:

```bash
alembic upgrade head
```

## 🚀 Running the Application

### Development Server

```bash
uvicorn app.main:app --reload
```

The API will be available at: <http://127.0.0.1:8000>

## 📖 API Documentation

Once the server is running, you can access:

- **Swagger UI**: <http://127.0.0.1:8000/api/v1/docs>
- **OpenAPI Spec**: <http://127.0.0.1:8000/api/v1/openapi.json>

## 🗂️ Project Structure

```text
chat/
├── app/
│   ├── main.py              # FastAPI application entry point
│   ├── api/
│   │   └── v1/
│   │       ├── auth.py      # Authentication endpoints
│   │       ├── users.py     # User management endpoints
│   │       ├── health.py    # Health check endpoints
│   │       └── routers.py   # API router configuration
│   ├── core/
│   │   ├── config.py        # Application settings
│   │   └── security.py      # Security utilities
│   ├── domain/
│   │   └── users/
│   │       ├── schemas.py   # Pydantic models
│   │       └── services.py  # Business logic
│   └── infra/
│       ├── db/              # Database configuration
│       └── repositories/    # Data access layer
├── alembic/                 # Database migrations
├── pyproject.toml          # Project configuration
└── README.md
```

## 🔧 Available Endpoints

### Authentication

- `POST /api/v1/auth/login` - User login
- `POST /api/v1/auth/refresh` - Refresh access token

### Users

- `POST /api/v1/users/` - Create new user
- `GET /api/v1/users/me` - Get current user profile
- `PUT /api/v1/users/me` - Update user profile

### Health

- `GET /api/v1/health/` - Application health check

## 🧪 Development

### Database Migrations

Create a new migration:

```bash
alembic revision --autogenerate -m "Description of changes"
```

Apply migrations:

```bash
alembic upgrade head
```

Rollback migration:

```bash
alembic downgrade -1
```

### Code Structure

This project follows Domain-Driven Design (DDD) principles:

- **API Layer**: HTTP request/response handling
- **Domain Layer**: Business logic and entities
- **Infrastructure Layer**: Database, external services

## 🔒 Security Features

- JWT token-based authentication
- Password hashing with bcrypt
- CORS middleware configuration
- Rate limiting support (with Redis)
- Input validation with Pydantic

## 📝 Configuration

The application uses environment variables for configuration. All settings are defined in `app/core/config.py` and can be overridden using environment variables with the `APP_` prefix.

Key configuration options:

- `APP_ENV`: Environment (dev/staging/prod)
- `APP_JWT_SECRET`: JWT signing secret
- `APP_DATABASE_URL`: PostgreSQL connection string
- `APP_ENABLE_PROMETHEUS`: Enable metrics endpoint

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and commit: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
