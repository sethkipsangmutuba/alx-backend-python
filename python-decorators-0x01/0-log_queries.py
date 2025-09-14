#!/usr/bin/python3
import sqlite3
import functools

def log_queries(func):
    """Decorator that logs SQL queries"""
    @functools.wraps(func)
    def wrapper(query):
        print(f"[LOG] Executing query: {query}")
        return func(query)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Call the function exactly as shown in instructions
fetch_all_users("SELECT * FROM users")
