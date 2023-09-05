# gpt-grader
A simple program to test how feasibly GPT3.5 can grade assignments. This is for reserach purposes only and not intended for use in any academic setting or commercial use.

# Usage
- Download necessary dependencies
- Configure config.json to
  - use the appropriate API key for GPT3.5.
  - Set your "rubric" or grading criteria
- Launch the program GPTGraderGUI.py
  - select a source directory of files (assumes they are all in docx format)
  - select the destination directory of files (this is the workspace and where feedback will go)

# Dependencies
- Python 3.0 or above
- python libraries
  - openai
  - pypandoc
  - json
  - codecs
