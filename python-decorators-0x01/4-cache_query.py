import time
import sqlite3
import functools

# Global query cache
query_cache = {}

# Reuse the with_db_connection decorator from Task 1
def with_db_connection(func):
    """Decorator that opens a DB connection, passes it to the function, and closes it."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users.db")
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

# Decorator to cache query results
def cache_query(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get("query") or (args[1] if len(args) > 1 else None)
        if query in query_cache:
            print(f"[CACHE] Returning cached result for query: {query}")
            return query_cache[query]
        result = func(*args, **kwargs)
        query_cache[query] = result
        print(f"[CACHE] Caching result for query: {query}")
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")
print(users)

# Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
print(users_again)
