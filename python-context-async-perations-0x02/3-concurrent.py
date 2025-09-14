import asyncio
import aiosqlite

DB_NAME = "users.db"

async def async_fetch_users():
    """Fetch all users asynchronously."""
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            results = await cursor.fetchall()
            return results

async def async_fetch_older_users():
    """Fetch users older than 40 asynchronously."""
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT * FROM users WHERE age > ?", (40,)) as cursor:
            results = await cursor.fetchall()
            return results

async def fetch_concurrently():
    """Run both queries concurrently using asyncio.gather."""
    all_users, older_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    print("All Users:", all_users)
    print("Users older than 40:", older_users)

# Execute concurrent fetch
asyncio.run(fetch_concurrently())
