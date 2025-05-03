# not-a-fan

## Description
This tool analyzes your Instagram followers by processing HTML files of your followers and following lists. It helps you identify users who don't follow you back and generates easy-to-use CSV files with the results.

## Features
- Extract Instagram usernames from HTML files
- Compare followers and following lists
- Identify users who don't follow you back
- Generate organized CSV files with the results
- Support for analyzing multiple accounts by specifying different input folders

## Requirements
- Python 3.6 or higher
- Required Python packages:
  - re (standard library)
  - csv (standard library)
  - os (standard library)
  - sys (standard library)
  - time (standard library)
  - argparse (standard library)

## Installation
1. Clone this repository or download the files
2. No external packages are required as the tool only uses Python standard libraries

## How to Use

### Step 1: Get your Instagram data
1. Log in to Instagram in your web browser
2. Go to your profile
3. Click on "Followers" and save the page as complete HTML (Ctrl+S or Cmd+S)
   - Name the file `followers_1.html`
4. Click on "Following" and save the page as complete HTML
   - Name the file `following.html`
5. Place both files in a folder (e.g., `data`, `data_myaccount`)

### Step 2: Run the analysis
Open a terminal and run:

```bash
python main.py [input_folder]
```

For example:
```bash
python main.py data
```

You can also specify a custom output folder:
```bash
python main.py data --output my_results
```

### Step 3: View the results
The tool will generate the following files in the output folder (default: `processed_[input_folder]`):
- `followers.csv`: List of all your followers
- `following.csv`: List of all accounts you follow
- `not_following_back.csv`: List of accounts that don't follow you back

## Advanced Usage

### Analyzing Multiple Accounts
You can analyze different Instagram accounts by organizing their HTML files in separate folders:

```bash
python main.py account1_data
python main.py account2_data
```

This will create separate output folders named `processed_account1_data` and `processed_account2_data`.

## Command Line Options
```
usage: main.py [-h] [--output OUTPUT] [input_folder]

Analyze Instagram followers.

positional arguments:
  input_folder          Folder containing HTML files (followers_1.html and following.html)

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        Folder to save results (default: processed_[input_folder])
```

## Output
The script will display a summary of the analysis in the terminal:
- Total number of followers
- Total number of accounts you follow
- Number of accounts that don't follow you back
- List of generated files
- Execution time

## License
This project is available for personal use.

## Disclaimer
This tool is intended for personal analysis only. Please respect Instagram's terms of service and privacy policies when using this tool.