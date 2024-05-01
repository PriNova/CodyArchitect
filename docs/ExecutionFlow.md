1. User Input:
   - Prompt the user to provide the directory path of the codebase they want to analyze.

2. Codebase Traversal:
   - Recursively traverse the provided codebase directory and its subdirectories.
   - Identify and collect all relevant source code files based on their file extensions.

3. Code Analysis:
   - For each source code file:
     - Read the file contents.
     - Extract relevant information such as module names, class names, function names, and their respective descriptions or comments.
     - Identify dependencies, libraries, and frameworks used in the file.
     - Store the extracted information in a structured format (e.g., a dictionary or a custom data structure).

4. LLM Interaction:
   - For each module, class, or function:
     - Prepare a prompt for the LLM, including the extracted information and any relevant context.
     - Send the prompt to the LLM via the OpenAI API.
     - Receive the LLM's response, which should provide a concise description or summary of the module, class, or function.
     - Store the LLM-generated descriptions alongside the corresponding code elements.

5. Embedding Generation:
   - For each module, class, or function:
     - Generate a vector embedding using the extracted information and the LLM-generated description.
     - Store the vector embedding in ChromaDB along with relevant metadata (e.g., file path, module name, class name, function name).

6. Report Generation:
   - High-level Overview:
     - Retrieve the stored information and embeddings from ChromaDB.
     - Generate a high-level overview of the codebase's architecture and structure based on the collected information.
     - Include a summary of the modules, classes, and functions, along with their descriptions.
   - Detailed Reports:
     - Generate separate reports for each module, class, or function, providing more detailed information and descriptions.
     - Include information about dependencies, libraries, and frameworks used.
   - Save the generated reports in Markdown format within the codebase directory or a specified output directory.

7. Error Handling:
   - Implement error handling mechanisms to gracefully handle any exceptions or errors that may occur during the execution of the program.
   - Display appropriate error messages to the user and terminate the program if necessary.

8. CLI Interface:
   - Implement a command-line interface (CLI) that allows users to specify the codebase directory they want to analyze.
   - Provide options for generating different types of reports (e.g., high-level overview, detailed reports) based on user preferences.


**Hierarchical Execution Flow**

1. User Input:
   - Prompt the user to provide the directory path of the codebase they want to analyze.

2. Codebase Traversal:
   - Recursively traverse the provided codebase directory and its subdirectories.
   - Identify and collect all relevant documentation files (e.g., README, CONTRIBUTING, LICENSE) and source code files based on their file extensions.

3. Documentation Analysis:
   - For each documentation file:
     - Read the file contents.
     - Provide the entire content of the file to the LLM.
     - Let the LLM identify and extract relevant information such as:
       - Project description
       - Architecture overview
       - Dependencies and requirements
       - Setup instructions
       - Configuration instructions
       - Examples or usage instructions
       - API documentation
       - Contribution guidelines
       - Testing instructions
       - Deployment instructions
       - Troubleshooting tips
       - Best practices and coding conventions
       - Roadmap or future plans
       - Related projects or resources
     - Store the LLM-generated summary or extracted information in a structured [format](StructuredInformationFormat.md)

4. LLM Interaction (Documentation):
   - Prepare a [prompt](Prompts.md) for the LLM, including the extracted documentation information.
   - Send the prompt to the LLM via the OpenAI API.
   - Receive the LLM's response, which should provide a concise summary of the project's purpose, key features, and high-level architecture based on the documentation.
   - Store the LLM-generated summary ([prompt](Prompts.md)).

5. Embedding Generation (Documentation):
   - Generate a vector embedding using the extracted documentation information and the LLM-generated summary.
   - Store the vector embedding in ChromaDB along with relevant metadata (e.g., file paths, document types).

6. Code Analysis (High-level):
   - Identify the main modules or packages within the codebase based on the directory structure and file naming conventions.
   - For each main module or package:
     - Recursively traverse its subdirectories and collect relevant source code files.
     - Extract high-level information such as module or package names, their purposes, and dependencies.
     - Store the extracted information in a structured format.

7. LLM Interaction (High-level):
   - Prepare a prompt for the LLM, including the extracted high-level code information and the documentation summary.
   - Send the prompt to the LLM via the OpenAI API.
   - Receive the LLM's response, which should provide an overview of the codebase's high-level architecture, module or package relationships, and their roles within the project.
   - Store the LLM-generated overview.

8. Embedding Generation (High-level):
   - Generate vector embeddings for each main module or package using the extracted high-level information and the LLM-generated overview.
   - Store the vector embeddings in ChromaDB along with relevant metadata (e.g., module or package names).

9. Code Analysis (Detailed):
   - For each source code file within the main modules or packages:
     - Read the file contents.
     - Extract detailed information such as class names, function names, and their respective descriptions or comments.
     - Identify dependencies, libraries, and frameworks used in the file.
     - Store the extracted information in a structured format.

10. LLM Interaction (Detailed):
    - For each class or function:
      - Prepare a prompt for the LLM, including the extracted detailed code information, the high-level overview, and the documentation summary.
      - Send the prompt to the LLM via the OpenAI API.
      - Receive the LLM's response, which should provide a detailed description or summary of the class or function, its purpose, and how it fits into the overall architecture.
      - Store the LLM-generated descriptions alongside the corresponding code elements.

11. Embedding Generation (Detailed):
    - For each class or function:
      - Generate a vector embedding using the extracted detailed information and the LLM-generated description.
      - Store the vector embedding in ChromaDB along with relevant metadata (e.g., file path, class name, function name).

12. Report Generation:
    - High-level Overview:
      - Retrieve the stored documentation information, high-level code information, and their respective embeddings from ChromaDB.
      - Generate a high-level overview of the codebase's architecture, purpose, and key features based on the collected information.
      - Include a summary of the main modules or packages and their relationships.
    - Detailed Reports:
      - Generate separate reports for each main module or package, providing more detailed information about the classes and functions within them.
      - Include descriptions of the classes and functions, along with their dependencies and relationships.
    - Save the generated reports in Markdown format within the codebase directory or a specified output directory.

13. Error Handling:
    - Implement error handling mechanisms to gracefully handle any exceptions or errors that may occur during the execution of the program.
    - Display appropriate error messages to the user and terminate the program if necessary.

14. CLI Interface:
    - Implement a command-line interface (CLI) that allows users to specify the codebase directory they want to analyze.
    - Provide options for generating different types of reports (e.g., high-level overview, detailed reports) based on user preferences.
