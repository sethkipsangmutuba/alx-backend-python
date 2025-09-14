import sqlite3

class ExecuteQuery:
    """Custom context manager to execute a query and return the result."""

    def __init__(self, query, params=None, db_name="users.db"):
        self.query = query
        self.params = params or ()
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.result = None

    def __enter__(self):
        """Open the connection, execute the query, and store the result."""
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query, self.params)
        self.result = self.cursor.fetchall()
        return self.result

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close the connection after execution."""
        if self.conn:
            self.conn.close()

# Usage example
query = "SELECT * FROM users WHERE age > ?"
params = (25,)

with ExecuteQuery(query, params) as results:
    print(results)
