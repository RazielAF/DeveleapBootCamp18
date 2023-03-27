#!/bin/bash

# Stop and remove any running Docker Compose instances
docker-compose down --volumes --remove-orphans

# Start a new Docker Compose instance
docker-compose up