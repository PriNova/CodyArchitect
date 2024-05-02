import argparse
import os

from codypy import log_message, setup_logger
from pathspec import PathSpec


def validate_codebase_dir(codebase_dir):
    if not os.path.exists(codebase_dir):
        raise argparse.ArgumentTypeError(
            f"Codebase directory '{codebase_dir}' does not exist."
        )

    git_dir = os.path.join(codebase_dir, ".git")
    if not os.path.isdir(git_dir):
        raise argparse.ArgumentTypeError(
            f"Codebase directory '{codebase_dir}' is not a local GitHub repository."
        )

    return codebase_dir


def collect_documentation_files(codebase_dir):
    documentation_files = []
    gitignore_path = os.path.join(codebase_dir, ".gitignore")
    gitignore_spec = None

    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r") as gitignore_file:
            gitignore_spec = PathSpec.from_lines("gitwildmatch", gitignore_file)

    for root, dirs, files in os.walk(codebase_dir):
        if gitignore_spec:
            dirs[:] = [
                d for d in dirs if not gitignore_spec.match_file(os.path.join(root, d))
            ]

        for file in files:
            file_path = os.path.join(root, file)
            if gitignore_spec and gitignore_spec.match_file(file_path):
                continue

            if file.endswith(".md") or file.endswith(".txt"):
                documentation_files.append(file_path)

    return documentation_files


def main(codebase_dir=None, output_dir=None):
    if codebase_dir is None:
        # Create a command-line interface (CLI) for the program
        parser = argparse.ArgumentParser(description="CodyArchitect")
        parser.add_argument(
            "codebase_dir",
            type=validate_codebase_dir,
            help="Path to the codebase directory",
        )
        parser.add_argument(
            "--output_dir",
            "-o",
            help="Path to the output directory for generated reports",
        )

        # Prompt the user to enter the codebase directory path
        args = parser.parse_args()

        # Store the user input for later use in the program
        codebase_dir = args.codebase_dir
        output_dir = args.output_dir

    # If the user did not provide an output directory path, create one in the codebase directory
    if not output_dir:
        output_dir = os.path.join(codebase_dir, ".codyarchitect")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    documentation_files = collect_documentation_files(codebase_dir)
    log_message("Main: ", f"{documentation_files}")


if __name__ == "__main__":

    setup_logger("CodyArchitect", "logs")
    codebase_dir = "."
    main(codebase_dir)
