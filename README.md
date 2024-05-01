# CodyArchitect: AI-Powered Codebase Onboarding Assistant

CodyArchitect is an innovative program designed to revolutionize the way developers understand and navigate unfamiliar codebases. Powered by advanced Large Language Model (LLM) technology, CodyArchitect provides comprehensive overviews of a codebase's architecture, functionality, and conventions, making the onboarding process smoother and more efficient.

**NOTE: This is a BUILD IN THE PUBLIC project and is not yet fully operational. You will find the documentation of the progress in the [doc](/docs/) folder**

## Sponsorship

If you find CodyArchitect valuable and would like to support its ongoing development, I am open to sponsorship. Your support will help me dedicate more time and resources to enhancing the program's features and functionality. Please reach out to me directly via [info@prinova.de](mailto:info@prinova.de?subject=Sponsorship%20CodyArchitect), over [Sourcegraph Discord](https://discord.gg/QVH2hc7a) to discuss sponsorship opportunities or use the sponsor button at the top.

## Key Features

- **Language-Agnostic**: CodyArchitect is adaptable to various programming languages and codebases, providing a unified view of the entire project.

- **Intelligent Architecture Overview**: Leveraging LLM capabilities, CodyArchitect generates high-level summaries of the codebase's architecture, highlighting the relationships between modules, packages, and their roles within the project.

- **Comprehensive Reports**: The program generates multiple reports focusing on different aspects of the codebase, such as high-level architecture, module and class descriptions, and dependencies.

- **Detailed Module and Function Reports**: CodyArchitect dives into the details of each module and function, providing descriptions, dependencies, and how they fit into the overall architecture. This granular information helps developers quickly grasp the purpose and functionality of specific code components.

- **Semantic Code Understanding**: By employing advanced natural language processing techniques, CodyArchitect understands the semantics of code elements, enabling it to provide meaningful insights and summaries.

- **Vector Embeddings and Efficient Storage**: CodyArchitect generates vector embeddings of code elements and stores them in ChromaDB, along with relevant metadata. This enables quick retrieval and similarity-based searches for efficient navigation and understanding of the codebase.

- **Markdown Output**: Reports are generated in easy-to-read Markdown format and stored on the file system for convenient access.

- **Command-Line Interface**: CodyArchitect offers a simple CLI where users can specify the directory of the codebase they want to analyze.

## How It Works

1. **User Input**: Provide the directory path of the codebase you want to analyze.
2. **Codebase Traversal**: CodyArchitect recursively traverses the codebase directory, collecting relevant documentation and source code files.
3. **Documentation Analysis**: The program extracts key information from documentation files using LLM, such as project description, architecture overview, and setup instructions.
4. **Code Analysis**: CodyArchitect identifies main modules, packages, classes, and functions within the codebase, extracting high-level and detailed information.
5. **LLM Interaction**: The extracted information is processed by the LLM to generate concise summaries and descriptions of the codebase's components and their relationships.
6. **Embedding Generation**: Vector embeddings are generated for documentation and code elements, enabling efficient storage and retrieval in ChromaDB.
7. **Report Generation**: CodyArchitect generates comprehensive reports in Markdown format, including high-level overviews and detailed module/package reports.

## Getting Started

To use CodyArchitect, follow these steps:

1. Clone the repository: `git clone https://github.com/PriNova/CodyArchitect.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up your OpenAI API credentials and ChromaDB configuration.
4. Run the program: `python codyarchitect.py /path/to/codebase`

## Roadmap and Upcoming Features

We have an exciting roadmap planned for CodyArchitect, including:

- [ ] Graphical User Interface (GUI) implementation
- [ ] Automation processes for bug fixing, feature implementations and more

## Contribution Guidelines

At this early stage of development, I am not accepting pull requests. However, I welcome feedback, suggestions, and bug reports through the issue tracker. Your input is valuable in shaping the future of CodyArchitect.

## License

CodyArchitect is released under the [MIT License](LICENSE).
