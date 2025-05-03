import re
import csv
import os
import json

def extract_instagram_usernames_from_html(file_path):
    """Extracts Instagram usernames from an HTML file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Use a regular expression to find usernames
        pattern = r'href="https://www\.instagram\.com/([a-zA-Z0-9._]+)"'
        usernames = re.findall(pattern, content)
        
        return usernames
    except Exception as e:
        print(f"Error processing HTML file {file_path}: {str(e)}")
        return []

def extract_instagram_usernames_from_json(file_path):
    """Extracts Instagram usernames from a JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        usernames = []
        
        # Navigate the JSON structure to find usernames
        # This structure might need to be adjusted based on the actual JSON format
        if isinstance(data, list):
            # If the JSON is a list of users
            for item in data:
                if 'string_list_data' in item and item['string_list_data']:
                    for user_data in item['string_list_data']:
                        if 'value' in user_data:
                            usernames.append(user_data['value'])
        elif isinstance(data, dict):
            # If the JSON has a different structure
            # Try to find relationships -> data which is common in Instagram data
            if 'relationships_following' in data:
                for item in data.get('relationships_following', []):
                    if 'string_list_data' in item and item['string_list_data']:
                        for user_data in item['string_list_data']:
                            if 'value' in user_data:
                                usernames.append(user_data['value'])
            elif 'relationships_followers' in data:
                for item in data.get('relationships_followers', []):
                    if 'string_list_data' in item and item['string_list_data']:
                        for user_data in item['string_list_data']:
                            if 'value' in user_data:
                                usernames.append(user_data['value'])
            # Additional structure checks can be added here
        
        return usernames
    except Exception as e:
        print(f"Error processing JSON file {file_path}: {str(e)}")
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

def extract_and_save_usernames(input_folder='data', output_folder='processed_data', file_type=None):
    """Extracts usernames from HTML or JSON files and saves them to CSV files."""
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Auto-detect file type if not specified
    if file_type is None:
        # Try HTML first
        followers_html = os.path.join(input_folder, 'followers_1.html')
        following_html = os.path.join(input_folder, 'following.html')
        
        if os.path.exists(followers_html) and os.path.exists(following_html):
            followers_file = followers_html
            following_file = following_html
            extract_function = extract_instagram_usernames_from_html
            file_type = 'html'
        else:
            # Try JSON
            followers_json = os.path.join(input_folder, 'followers_1.json')
            following_json = os.path.join(input_folder, 'following.json')
            
            if os.path.exists(followers_json) and os.path.exists(following_json):
                followers_file = followers_json
                following_file = following_json
                extract_function = extract_instagram_usernames_from_json
                file_type = 'json'
            else:
                print("Error: Could not find Instagram data files.")
                return 0, 0
    else:
        # Use the specified file type
        if file_type == 'html':
            followers_file = os.path.join(input_folder, 'followers_1.html')
            following_file = os.path.join(input_folder, 'following.html')
            extract_function = extract_instagram_usernames_from_html
        else:  # json
            followers_file = os.path.join(input_folder, 'followers_1.json')
            following_file = os.path.join(input_folder, 'following.json')
            extract_function = extract_instagram_usernames_from_json

    # Extract usernames from both files
    print(f"Processing {file_type.upper()} files...")
    followers_usernames = extract_function(followers_file)
    following_usernames = extract_function(following_file)

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
    
    parser = argparse.ArgumentParser(description='Extract Instagram usernames from HTML or JSON files.')
    parser.add_argument('input_folder', nargs='?', default='data', 
                      help='Folder containing the HTML or JSON files')
    parser.add_argument('--output', '-o', default='processed_data',
                      help='Folder to save the results')
    
    args = parser.parse_args()
    extract_and_save_usernames(args.input_folder, args.output)