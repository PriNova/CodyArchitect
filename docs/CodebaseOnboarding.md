**Goal**

The goal is to implement a program (CodyArchitect) that is powered by LLM for software developers. The objective of this program is to provide a comprehensive overview of an unknown codebase, which would facilitate the onboarding process. The program should include the following features:

1. The program should provide an overview of the purpose of the codebase.
2. The program should provide a comprehensive overview of the architecture, modules, and classes.
3. Provide an overview of the functions of the codebase.

It is necessary that the LLM be provided with access to a terminal for the execution of commands, the reading of files, and the saving of documentation. The development of the program necessitates the input of your expertise in the form of assistance with the design phase.

Here's a summary of our discussion:

**Program Overview**

* The program will analyze a codebase and generate a comprehensive report to help developers understand the codebase's architecture, functionality, and conventions.
* The program will be language-agnostic and adaptable to various codebases.

**Program Features**

* The program will generate multiple reports, each focusing on a specific aspect of the codebase, such as:
	+ High-level overview of the codebase's architecture and structure
	+ List of modules, classes, and functions, along with their descriptions
	+ Information about dependencies, libraries, and frameworks used
* The program will utilize a Large Language Model (LLM) to analyze the codebase's syntax and semantics, understand documentation and comments, and identify patterns and relationships within the codebase.

**Program Output**

* The program will generate reports in Markdown format and store them on the file system.
* The reports will provide a comprehensive overview of the codebase, including its architecture, functionality, and conventions.

**User Interface**

* The program will have a simple command-line interface (CLI) where the user can specify the directory of the codebase they want to analyze.

**Design Considerations**

* The program should provide a unified view of the entire codebase, highlighting language-specific components and interactions.
* The program should focus on the code within the codebase, but mention third-party libraries and services for their interfacing.
* The program should incorporate code comments and documentation, but distill the information into a brief form.
* The program should handle codebases with a large number of modules, classes, and functions by generating hierarchical reports.
* The reports should be limited in size to facilitate transformation into vector embeddings for the LLM.
* The program should update the reports accordingly as changes are made to the codebase.
* The program should highlight conflicts or inconsistencies in the codebase, such as contradictory comments or unclear documentation.
* The program should mask sensitive information, such as API keys or encryption keys, with a placeholder.
* The program should handle custom or proprietary frameworks, libraries, or tools used within the codebase equally to standard technologies.
* The program will be designed as a standalone tool, allowing developers to use it independently of their existing workflows and tools.
* The program will rely on manual updates by the user, rather than automatically checking for updates.
* The program will simply notify the user of an error and terminate, rather than providing detailed error messages.
* The program should be able to identify and highlight dependencies and interactions between different languages and components within the codebase.
* The program should be flexible enough to provide both high-level overviews of interactions and dependencies, as well as more detailed information about API calls, data formats, and communication protocols, depending on the developer's needs and preferences.

**Technology, Frameworks and Libraries**

- The program will be written in Python, and uses the [codypy Python wrapper](https://github.com/PriNova/codypy), the OpenAI API via Ollama for the Large Language Model (LLM) capabilities, ChromaDB for storing vector embeddings with metadata annotations, and keep dependencies to a minimum.

**Implementation Plan**

The high-level components of the program:

1. Code Analyzer: responsible for parsing the codebase, extracting relevant information, and generating reports.
2. LLM Interface: interacts with the OpenAI API to leverage the Large Language Model capabilities.
3. Embedding Generator: generates vector embeddings for the codebase components (e.g., modules, classes, functions).
4. ChromaDB Interface: stores and retrieves vector embeddings with metadata annotations.
5. Report Generator: generates comprehensive reports in Markdown format.

[Execution Flow](ExecutionFlow.md)