import sqlite3

# Initialize the database connection
conn = sqlite3.connect('new_devices.db')
cursor = conn.cursor()

# Create the table to store device information if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS new_devices (
        ip_address TEXT ,
        mac_adress TEXT,
        device_name TEXT,
        status STRING,
        connected_devices TEXT     
    )
''')
conn.commit()



# Close the database connection
conn.close()