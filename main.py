""" 1. The directory path of the codebase to be analyzed
2. The output directory for the generated reports

To implement this step, we'll break it down into smaller tasks:

1. Create a command-line interface (CLI) for the program
2. Prompt the user to enter the codebase directory path
3. Validate the provided codebase directory path
4. Prompt the user to enter the output directory path
5. Validate the provided output directory path
6. Store the user input for later use in the program """

import argparse
import os

def validate_codebase_dir(codebase_dir):
    if not os.path.exists(codebase_dir):
        raise argparse.ArgumentTypeError(f"Codebase directory '{codebase_dir}' does not exist.")
    
    git_dir = os.path.join(codebase_dir, '.git')
    if not os.path.isdir(git_dir):
        raise argparse.ArgumentTypeError(f"Codebase directory '{codebase_dir}' is not a local GitHub repository.")
    
    return codebase_dir

def main():
    # Create a command-line interface (CLI) for the program
    parser = argparse.ArgumentParser(description='CodyArchitect')
    parser.add_argument('codebase_dir', type=validate_codebase_dir, help='Path to the codebase directory')
    parser.add_argument('--output_dir', '-o', help='Path to the output directory for generated reports')
    
    # Prompt the user to enter the codebase directory path
    args = parser.parse_args()
    
    # Store the user input for later use in the program
    codebase_dir = args.codebase_dir
    output_dir = args.output_dir
    
    # If the user did not provide an output directory path, create one in the codebase directory
    if not output_dir:
        output_dir = os.path.join(codebase_dir, '.codyarchitect')
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
if __name__ == '__main__':
    main()
