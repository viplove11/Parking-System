# Parking System Management

This Python script provides functionality for managing a parking system with support for both four-wheeler and two-wheeler vehicles. It allows administrators to register, login, and perform various operations such as parking vehicles, removing vehicles, checking parking status, adding and removing parking slots.

## Dependencies
- `mysql-connector-python`: for connecting to the MySQL database
- `os`: for system operations like clearing the screen
- `time`: for time-related operations

## Database Setup
1. Install MySQL and create a database named `Parkingsystem`.
2. Below are the details of the database tables:

### Table: `adminTable`
- Columns:
  - `admin_id` (Primary Key, Auto Increment)
  - `admin_name`
  - `admin_password`

### Table: `fourwheeler`
- Columns:
  - `parking_id` (Primary Key)
  - `vehicle_no`
  - `entry_time`
  - `exit_time`
  - `occupied`

### Table: `twowheeler`
- Columns:
  - `parking_id` (Primary Key)
  - `vehicle_no`
  - `entry_time`
  - `exit_time`
  - `occupied`

## Usage
1. Run the script.
2. Choose between registration and login options.
3. After logging in as an admin, you can manage parking slots and vehicles.
4. Select the type of vehicle (four-wheeler or two-wheeler) and perform the desired operation.
5. Follow the on-screen prompts to park or remove vehicles, check parking status, add or remove parking slots, etc.

## Features
- Separate parking management for four-wheelers and two-wheelers.
- Secure admin login functionality.
- CRUD operations for parking slots and vehicles.
- Real-time display of parking status.
- Simple and intuitive interface.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.