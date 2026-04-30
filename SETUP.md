# Setup Instructions for the Boxing App

## Prerequisites
Before setting up the application, ensure you have the following installed:
- Python 3.8+
- PostgreSQL 12+
- Flutter SDK

## Backend Setup (FastAPI Server)
1. Clone the repository:
   ```
   git clone https://github.com/ahmdkhalifa2026-ui/Boxing-App.git
   cd Boxing-App/back_end
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate  # For Windows
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up your PostgreSQL database:
   - Create a database for the application.
   - Update the database configuration in `config.py` with your database credentials.

5. Run the FastAPI server:
   ```
   uvicorn main:app --reload
   ```

## Database Setup (PostgreSQL)
1. Access the PostgreSQL command line:
   ```
   psql -U your_username
   ```

2. Create a new database:
   ```
   CREATE DATABASE boxing_app;
   ```

3. Create the necessary tables by running the migration scripts provided in the `migrations` folder.

## Frontend Setup (Flutter Application)
1. Navigate to the frontend directory:
   ```
   cd ../front_end
   ```

2. Install Flutter dependencies:
   ```
   flutter pub get
   ```

3. Run the Flutter application:
   ```
   flutter run
   ```

## Conclusion
You can now access the application through your browser or the Flutter app on your device. Make sure to check for any additional configuration or permissions needed in the respective documentation for FastAPI and Flutter.
