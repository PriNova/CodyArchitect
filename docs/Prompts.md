1. Prompt to gather information based on the execution flow number 4.

    ```
    Analyze the provided documentation and extract the most relevant information to give a concise overview of the software project. Include the following details in your summary:

    1. Project Description:
    - Briefly describe the purpose and main functionality of the project.
    - Highlight the key features or unique aspects of the project.

    2. Architecture Overview:
    - Provide a high-level overview of the project's architecture.
    - Mention the main components, modules, or layers of the system.
    - Describe how these components interact with each other.

    3. Dependencies and Requirements:
    - List the major dependencies, libraries, or frameworks used in the project.
    - Specify any specific versions or compatibility requirements.

    4. Setup and Configuration:
    - Summarize the steps required to set up and configure the project.
    - Include any necessary environment variables, configuration files, or database setup.

    5. Usage Instructions:
    - Provide a brief explanation of how to use the project or run the application.
    - Include any command-line arguments, API endpoints, or user interface interactions.

    6. Contribution Guidelines:
    - Summarize the guidelines for contributing to the project.
    - Mention any coding conventions, branch naming, or pull request processes.

    7. Testing and Deployment:
    - Briefly explain how to run tests for the project.
    - Provide an overview of the deployment process or any specific deployment considerations.

    8. Additional Resources:
    - List any additional resources, such as API documentation, examples, or troubleshooting guides.
    - Provide links to these resources if available.

    Please generate a concise summary that covers these key points based on the provided documentation. The summary should be clear, well-structured, and easy to understand for developers who are new to the project.
    ```

2. Prompt to structure the extracted information into a JSON format:

    ```
    Please structure the extracted information from the documentation into a JSON format using the following guidelines:

    1. Create a JSON object with the following keys:
    - "project_description"
    - "architecture_overview"
    - "dependencies"
    - "requirements"
    - "setup_instructions"
    - "configuration_instructions"
    - "usage_instructions"
    - "contribution_guidelines"
    - "testing_instructions"
    - "deployment_instructions"
    - "additional_resources"

    2. For each key, provide the corresponding information extracted from the documentation very briefly.

    3. If any information is missing, couldn't be extracted or is not known, set the value of the corresponding key to "UNKNOWN".

    4. Ensure that the JSON object is well-formatted, with proper indentation and syntax.

    5. If there are any code snippets or examples in the extracted information, format them as strings within the JSON object.

    6. Use clear and concise language in the JSON values, avoiding any ambiguity or redundancy.

    7. If there are multiple points or steps for a particular key (e.g., setup instructions), represent them as an array of strings.

    Here's an example of the desired JSON format:

        ```json
        {
            "project_description": "A powerful tool for analyzing codebases.",
            "architecture_overview": "The project follows a modular architecture with three main components: parser, analyzer, and reporter.",
            "dependencies": [
                "Python 3.8+",
                "OpenAI API",
                "ChromaDB"
            ],
            "setup_instructions": [
                "Clone the repository",
                "Install dependencies using pip",
                "Set up the required environment variables"
            ],
            "usage_instructions": "Run the main script with the codebase directory as an argument.",
            "contribution_guidelines": "UNKNOWN",
            "testing_instructions": "Run the test suite using the command `pytest tests/`.",
            "deployment_instructions": "UNKNOWN",
            "additional_resources": [
                "API documentation: https://example.com/api-docs",
                "Troubleshooting guide: https://example.com/troubleshooting"
            ]
        }
        ```

    Please generate the JSON object based on the extracted information, following the provided guidelines and example format.
    ```