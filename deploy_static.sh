#!/bin/bash

# Capture arguments passed from Flask app
process_name=$1
github_url=$2
local_directory=$3
docker_image=$4
container_port=$5
access_port=$6

# Function to check if Docker and Docker Compose are installed
check_docker() {
    if ! command -v docker &> /dev/null; then
        echo "Docker is not installed. Please install Docker and try again."
        exit 1
    fi

    if ! command -v docker-compose &> /dev/null; then
        echo "Docker Compose is not installed. Please install Docker Compose and try again."
        exit 1
    fi
}

# Function to deploy static website
deploy_static() {
    echo "Deploying static web app..."

    # Validate process name follows Kubernetes naming conventions
    if [[ ! "$process_name" =~ ^[a-z0-9]([-a-z0-9]*[a-z0-9])?$ ]]; then
        echo "Invalid process name. It must contain lowercase alphanumeric characters and be hyphen or period separated."
        exit 1
    fi

    # If a GitHub URL is provided, clone the repository
    if [[ -n "$github_url" ]]; then
        echo "Cloning repository from GitHub..."
        git clone "$github_url" app
        local_directory="./app"
    fi

    # Ensure the provided directory exists and contains an 'index.html' file
    if [[ -f "$local_directory/index.html" ]]; then
        # Use existing Docker image or create a new one
        if [[ -z "$docker_image" ]]; then
            echo "Using an existing Docker image."
        fi

        # Create Dockerfile
        echo "Creating Dockerfile in $local_directory..."
        cat > "$local_directory/Dockerfile" <<EOL
FROM nginx:alpine
COPY . /usr/share/nginx/html
EOL

        # Create docker-compose.yml
        echo "Creating docker-compose.yml in $local_directory..."
        cat > "$local_directory/docker-compose.yml" <<EOL
version: '3'
services:
  web:
    build:
      context: .
    image: $docker_image
    ports:
      - "$access_port:$container_port"
    restart: always
EOL

        # Navigate to the source code directory
        cd "$local_directory" || exit

        # Build and start the Docker container using Docker Compose
        echo "Building and starting the application with Docker Compose..."
        docker-compose up --build -d

        echo "Static website deployed! Access it at http://localhost:$access_port"
    else
        echo "Error: 'index.html' not found in the specified directory."
        exit 1
    fi
}

# Main function to handle deployment
main() {
    # Check if Docker and Docker Compose are installed
    check_docker

    # Proceed to deploy the static web app
    deploy_static
}

# Execute the main function
main
