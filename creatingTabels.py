import sqlite3

# Connect to the database
conn = sqlite3.connect('conference_scheduling.db')  # Replace with your desired database filename

# Create the Users table
users_table = """
CREATE TABLE Users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
"""

# Create the Events table
events_table = """
CREATE TABLE Events (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  title TEXT NOT NULL,
  description TEXT,  # Corrected indentation here
  date DATE NOT NULL,
  start_time TIME NOT NULL,
  end_time TIME NOT NULL,
  room_id INTEGER,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES Users(id)
);
"""

# Execute the CREATE TABLE statements
conn.execute(users_table)
conn.execute(events_table)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Tables created successfully!")
