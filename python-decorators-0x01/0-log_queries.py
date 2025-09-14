#!/usr/bin/python3
import sqlite3
import functools

def log_queries():
    """Decorator that logs SQL queries"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            query = kwargs.get("query")
            if query is None and args:
                query = args[0]
            if query:
                print(f"[LOG] Executing query: {query}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_queries()
def fetch_all_users(query):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Execute function as instructed
fetch_all_users(query="SELECT * FROM users")
