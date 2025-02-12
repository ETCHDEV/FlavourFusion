# Recipe Generator

## Overview
Recipe Generator is a Python-based application that helps users find recipes based on available ingredients or specific categories. The application features a user-friendly GUI built with Tkinter and stores recipe data using MySQL.

## Features
- **Search by Ingredients**: Enter available ingredients to find matching recipes.
- **Search by Category**: Select a category from a dropdown menu to browse recipes.
- **Recipe Details**: View detailed recipe instructions and ingredients.
- **Intuitive UI**: Designed using Tkinter Designer for an enhanced user experience.
- **MySQL Database**: Stores recipes and related information efficiently.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- MySQL Server
- Required Python packages:
  ```sh
  pip install mysql-connector-python tkinter
  ```

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/ETCHDEV/FlavourFusion.git
   cd FlavourFusion
   ```
2. Set up the database:
   - Create a MySQL database.
   - Import the provided SQL schema.
3. Configure the database connection in `config.py`:
   ```python
   DB_CONFIG = {
       'host': 'your_host',
       'user': 'your_user',
       'password': 'your_password',
       'database': 'flavourfusion'
   }
   ```
4. Run the application:
   ```sh
   python Search_Ingredients.py
   ```
   or
   ```sh
   python Search_Category.py
   ```

## Usage
- **Searching by Ingredients**: Enter ingredients in the input field and click the search button to get relevant recipes.
- **Searching by Category**: Select a category from the dropdown menu to view available recipes.
- **Viewing Recipe Details**: Double-click on a recipe in the results table to open a window with full details.

## Project Structure
```
recipe-generator/
│-- controllers/
│   ├── rating_controller.py
│   ├── recipe_controller.py
│   ├── user_controller.py
│-- db_helper.py
│-- config.py
│-- Search_Ingredients.py
│-- Search_Category.py
 .
 .
 .
│-- assets/
│-- README.md
```

## Contributing
Contributions are welcome! Feel free to submit issues and pull requests.

## License
This project is licensed under the MIT License.

