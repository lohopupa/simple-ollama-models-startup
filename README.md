# Project README

## Project Overview

This project sets up and runs [Ollama](https://github.com/ollama/ollama/tree/main) in a Docker container and installs the necessary models for usage. The purpose is to streamline the installation and running process by using Docker, ensuring a consistent environment for all users.

## Prerequisites

Before you begin, ensure you have the following installed:

Docker: Make sure Docker is installed and running on your machine. You can download Docker from [here](https://docs.docker.com/engine/install/).

## Getting Started
### Follow these steps to set up and run the project:

1. Clone the Repository
Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/lohopupa/simple-ollama-models-startup.git
```

2. Navigate to the Project Directory
Change your directory to the project folder:

```bash
cd simple-ollama-models-startup
```

3. Add neccesary models to list inside load_models.py file

4. Run docker compose
Build and run containers using the provided docker-compose file:

```bash
docker compose up -d
```

## License
This project is licensed under the MIT License. See the LICENSE file for more information.
