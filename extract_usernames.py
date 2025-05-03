import re
import csv
import os

def extract_instagram_usernames(file_path):
    """Extracts Instagram usernames from an HTML file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Use a regular expression to find usernames
        pattern = r'href="https://www\.instagram\.com/([a-zA-Z0-9._]+)"'
        usernames = re.findall(pattern, content)
        
        return usernames
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return []

def save_to_csv(usernames, output_file):
    """Saves a list of usernames to a CSV file."""
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Username'])  # Write header
            for username in usernames:
                writer.writerow([username])
        return True
    except Exception as e:
        print(f"Error saving {output_file}: {str(e)}")
        return False

def extract_and_save_usernames(input_folder='data', output_folder='processed_data'):
    """Extracts usernames from HTML files and saves them to CSV files."""
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Input files
    followers_file = os.path.join(input_folder, 'followers_1.html')
    following_file = os.path.join(input_folder, 'following.html')

    # Extract usernames from both files
    followers_usernames = extract_instagram_usernames(followers_file)
    following_usernames = extract_instagram_usernames(following_file)

    # Output CSV file paths in the output folder
    followers_csv = os.path.join(output_folder, 'followers.csv')
    following_csv = os.path.join(output_folder, 'following.csv')

    # Save each list to its own CSV file
    save_to_csv(followers_usernames, followers_csv)
    save_to_csv(following_usernames, following_csv)

    # Print results
    print(f"Followers extracted and saved to {followers_csv}")
    print(f"Total followers: {len(followers_usernames)}")

    print(f"Following extracted and saved to {following_csv}")
    print(f"Total following: {len(following_usernames)}")
    
    return len(followers_usernames), len(following_usernames)

# If this script is run directly
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Extract Instagram usernames from HTML files.')
    parser.add_argument('input_folder', nargs='?', default='data', 
                      help='Folder containing the HTML files')
    parser.add_argument('--output', '-o', default='processed_data',
                      help='Folder to save the results')
    
    args = parser.parse_args()
    extract_and_save_usernames(args.input_folder, args.output)