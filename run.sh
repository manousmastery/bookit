#!/bin/bash

# Ensure that the script is being run from the root of the Django project (where pyproject.toml is located)
if [ ! -f "pyproject.toml" ]; then
    echo "Error: pyproject.toml not found. Please run this script from the root of your project."
    exit 1
fi

# Check if PDM is installed
if ! command -v pdm &> /dev/null
then
    echo "Error: PDM is not installed. Please install PDM first."
    exit 1
fi

# Install dependencies (if not already installed)
echo "Installing dependencies using PDM..."
pdm install

# Activate the virtual environment (if necessary)
echo "Activating virtual environment..."
pdm run python manage.py migrate  # Apply migrations

# Optionally, run tests (uncomment if you need to run tests before starting the server)
# pdm run python manage.py test

echo "Django project is running!"
