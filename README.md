# Chat Application

A modern, scalable enterprise chat application built with FastAPI, featuring multi-LLM support, enterprise-grade security, and comprehensive integration capabilities for business workflows.

## Goals & Vision

This enterprise chat application is designed to revolutionize business communication by providing an intelligent, secure, and highly customizable chat platform that integrates seamlessly with existing enterprise infrastructure.

### Core Objectives

- **Enterprise-First Design**: Built specifically for enterprise environments with scalability, reliability, and enterprise-grade features
- **Multi-LLM Support**: Seamlessly integrate with multiple Large Language Model providers including:
  - OpenAI (GPT-4, GPT-3.5)
  - DeepSeek
  - Anthropic Claude
  - Azure OpenAI
  - Custom/Self-hosted models
- **Enterprise Security & Compliance**:
  - SOC 2, GDPR, HIPAA compliance support
  - Data residency controls
  - Advanced encryption (at rest and in transit)
  - Audit logging and monitoring
  - Role-based access control (RBAC)
- **Knowledge Integration**:
  - Connect to enterprise data sources (databases, file systems, SharePoint, etc.)
  - Vector database integration for semantic search
  - Document processing and indexing
  - Real-time knowledge base updates
- **Hybrid Deployment**:
  - Cloud-native architecture
  - On-premises deployment options
  - Air-gapped environments support
  - Offline mode capabilities
- **Advanced Prompt Management**:
  - Template library and versioning
  - A/B testing for prompts
  - Performance analytics
  - Custom prompt workflows
- **Enterprise Integrations**:
  - CRM systems (Salesforce, HubSpot, etc.)
  - ERP platforms (SAP, Oracle, etc.)
  - HR systems (Workday, BambooHR, etc.)
  - Collaboration tools (Slack, Teams, etc.)
  - Custom API integrations
- **Workflow Automation**:
  - Business process automation
  - Conditional conversation flows
  - Escalation management
  - Integration with RPA tools
  - Custom scripting capabilities

### Target Use Cases

- **Customer Support**: AI-powered support with enterprise knowledge base integration
- **Internal Help Desk**: Employee assistance with access to company policies and procedures
- **Sales Enablement**: Lead qualification and product information assistance
- **HR Assistant**: Employee onboarding, policy questions, and HR process automation
- **Technical Documentation**: Code assistance and technical knowledge sharing
- **Compliance Monitoring**: Automated compliance checking and regulatory guidance

## Features

- **FastAPI Framework**: High-performance async API with automatic OpenAPI documentation
- **User Authentication**: JWT-based authentication with access and refresh tokens
- **User Management**: Complete user registration and profile management
- **Database Integration**: PostgreSQL with SQLAlchemy ORM and Alembic migrations
- **Security**: Password hashing with bcrypt, CORS middleware
- **API Versioning**: Structured API versioning with `/api/v1/` prefix
- **Health Checks**: Built-in health monitoring endpoints
- **Development Ready**: Hot reload, structured logging, and comprehensive error handling

## Requirements

- Python 3.11+
- PostgreSQL database

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/coralcoffee/chat
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

## Running the Application

### Development Server

```bash
uvicorn app.main:app --reload
```

The API will be available at: <http://127.0.0.1:8000>

## API Documentation

Once the server is running, you can access:

- **Swagger UI**: <http://127.0.0.1:8000/api/v1/docs>
- **OpenAPI Spec**: <http://127.0.0.1:8000/api/v1/openapi.json>

## Project Structure

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

## Available Endpoints

### Authentication

- `POST /api/v1/auth/login` - User login
- `POST /api/v1/auth/refresh` - Refresh access token

### Users

- `POST /api/v1/users/` - Create new user
- `GET /api/v1/users/me` - Get current user profile
- `PUT /api/v1/users/me` - Update user profile

### Health

- `GET /api/v1/health/` - Application health check

## Development

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

## Security Features

- JWT token-based authentication
- Password hashing with bcrypt
- CORS middleware configuration
- Rate limiting support (with Redis)
- Input validation with Pydantic

## Configuration

The application uses environment variables for configuration. All settings are defined in `app/core/config.py` and can be overridden using environment variables with the `APP_` prefix.

Key configuration options:

- `APP_ENV`: Environment (dev/staging/prod)
- `APP_JWT_SECRET`: JWT signing secret
- `APP_DATABASE_URL`: PostgreSQL connection string
- `APP_ENABLE_PROMETHEUS`: Enable metrics endpoint

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and commit: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
