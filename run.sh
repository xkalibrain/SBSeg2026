#!/bin/bash

check_all_containers() {
  local containers=("$@")

  if ! docker info > /dev/null 2>&1; then
    echo "Docker info failed"
    return 1
  fi

  for container in "${containers[@]}"; do
    status=$(docker ps -a --filter "name=^${container}$" --format '{{.Status}}')

    if [[ -z "$status" ]] || [[ "$status" != Up* ]]; then
      echo "Container '$container' is status '$status', not up."
      return 1
    fi
  done

  return 0
}

run() {
  if ! command -v docker &> /dev/null; then
    echo "❌ Docker not found"
    echo "Please install Docker and try again"
    exit 1
  fi

  echo "✅ Docker already installed ($(docker --version))"

  local COMMAND
  COMMAND="docker-compose"
  $COMMAND version
  if [ $? -ne 0 ]; then
    COMMAND="docker compose"
  fi
  $COMMAND version
  if [ $? -ne 0 ]; then
    echo "❌ Docker Compose not found"
    echo "Please install Docker Compose and try again"
    exit 1
  fi

  echo "Building Docker images..."
  $COMMAND build
  if [ $? -ne 0 ]; then
    echo "❌ Docker image build failed"
    exit 1
  fi
  echo "✅ Docker images built successfully!"

  echo "Starting WebXkaliburr services..."
  $COMMAND up -d
  if [ $? -ne 0 ]; then
    echo "❌ Some error occurred while trying to start WebXkaliburr services"
    exit 1
  fi

  sleep 3
  containers=("exekaliburr-api" "exekaliburr-front" "exekaliburr-nginx")
  containers_result=$(check_all_containers "${containers[@]}")
  if [ $? -ne 0 ]; then
    echo "❌ Some service is not running properly, start up failed."
    echo $containers_result
  fi

  echo "✅ WebXkaliburr is running, you can access it by https://localhost"
}

print_header() {
  echo "__          __  _            _  __     _ _ _                            ___    ___"
  echo " \\ \\        / / | |          | |/ /    | (_) |                          |__ \\  / _ \\"
  echo "  \\ \\  /\\  / /__| |__   __  _| ' / __ _| |_| |__  _   _ _ __ _ __  __   __ ) || | | |"
  echo "   \\ \\/  \\/ / _ \\ '_ \\  \\ \\/ /  < / _\` | | | '_ \\| | | | '__| '__| \\ \\ / // / | | | |"
  echo "    \\  /\\  /  __/ |_) |  >  <| . \\ (_| | | | |_) | |_| | |  | |     \\ V // /_ | |_| |"
  echo "     \\/  \\/ \\___|_.__/  /_/\\_\\_|\\_\\__,_|_|_|_.__/ \\__,_|_|  |_|      \\_/|____(_)___/"
  echo ""
  echo "By round table team"
}

main() {
  print_header
  echo "Running WebXkaliburr with Docker"
  run
}

main
