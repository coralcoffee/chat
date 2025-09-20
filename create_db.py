"""
Script to create the PostgreSQL database for the chat application.
Run this before running alembic migrations.
"""
import asyncio
import asyncpg
from app.core.config import settings

async def create_database():
    """Create the chat_db database if it doesn't exist."""
    # Parse the database URL to get connection details
    url_parts = settings.database_url.replace("postgresql+asyncpg://", "").split("/")
    db_name = url_parts[-1]  # chat_db
    
    # Connection string without the database name (connect to postgres db instead)
    conn_parts = url_parts[0].split("@")
    user_pass = conn_parts[0]
    host_port = conn_parts[1]
    
    # Connect to postgres database to create our database
    postgres_url = f"postgresql://{user_pass}@{host_port}/postgres"
    
    try:
        # Connect to postgres database
        conn = await asyncpg.connect(postgres_url)
        
        # Check if database exists
        exists = await conn.fetchval(
            "SELECT 1 FROM pg_database WHERE datname = $1", db_name
        )
        
        if not exists:
            # Create the database
            await conn.execute(f'CREATE DATABASE "{db_name}"')
            print(f"✅ Database '{db_name}' created successfully!")
        else:
            print(f"ℹ️  Database '{db_name}' already exists.")
            
        await conn.close()
        
    except Exception as e:
        print(f"❌ Error creating database: {e}")
        print("Make sure PostgreSQL is running and credentials are correct.")
        print(f"Connection string: {postgres_url}")
        return False
    
    return True

if __name__ == "__main__":
    print("Creating PostgreSQL database...")
    success = asyncio.run(create_database())
    
    if success:
        print("\n🎉 Database setup complete! You can now run:")
        print("alembic revision --autogenerate -m 'Initial migration'")
        print("alembic upgrade head")