import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize a list to store the data temporarily
data = []

# Database connection
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Waleed#07",
    database="flask"
)

# Create a cursor to interact with the database
db_cursor = db_connection.cursor()

# Create a table to store the data
db_cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        age INT
    )
''')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get data from the form
        name = request.form.get('name')
        age = int(request.form.get('age'))

        # Insert data into the database
        insert_query = "INSERT INTO user_data (name, age) VALUES (%s, %s)"
        db_cursor.execute(insert_query, (name, age))
        db_connection.commit()
    # Retrieve data from the database
    select_query = "SELECT name, age FROM user_data"
    db_cursor.execute(select_query)
    data = db_cursor.fetchall()
    print(data)

    return render_template('base.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
