# Project Todo Management System

A simple web-based application for managing your to-do list efficiently.

## Flask MongoDB Todo App

### Overview

This is a web-based Todo application built with Flask, a Python web framework, and MongoDB, a NoSQL database. The app allows users to create, edit, and delete tasks, providing a seamless experience for managing their to-do lists. The integration of Flask and MongoDB enables a flexible and scalable solution for handling data storage and retrieval.

### Features

- **Create Todo:** Users can easily add new tasks to their to-do list by providing a task name, description, and completion status through a user-friendly interface.

- **Edit and Delete:** The app supports editing and deleting tasks, allowing users to update task details or remove completed or unnecessary items.

- **Page Navigation:** Multiple pages provide a well-organized structure, enhancing user experience and facilitating efficient task management.

### Technologies Used

- **Flask:** A lightweight and extensible web framework in Python that simplifies the development of web applications.

- **MongoDB:** A NoSQL database, chosen for its flexibility and scalability, offering a dynamic schema and easy integration with Python applications.

- **Flask-PyMongo:** A Flask extension that simplifies the interaction between Flask applications and MongoDB databases.

### Installation

1. Clone the repository:

    ```bash
    git clone [https://github.com/IISuperheroII/Todo-App]
    ```

2. Navigate to the project directory:

    ```bash
    cd todo-management-system
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the MongoDB URI in the `config.py` file:

    ```python
    MONGO_URI = "your-mongodb-uri"
    ```

5. Run the application:

    ```bash
    python app.py
    ```

Visit [http://localhost:5000](http://localhost:5000) in your web browser to access the Todo app.

### Usage

1. Open the app in your web browser.

2. Create a new task by providing a name, description, and completion status.

3. Edit or delete tasks as needed.

4. Navigate between different pages to manage your to-do list effectively.

### Contributing

Contributions are welcome! If you have suggestions, bug reports, or would like to add new features, feel free to open an issue or submit a pull request.


---

For more information about the project, contact [wael22ka@hotmail.com].
