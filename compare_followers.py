import csv
import os

def load_usernames_from_csv(csv_file):
    """Loads usernames from a CSV file."""
    usernames = []
    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if row:  # Avoid empty rows
                    usernames.append(row[0])
        return usernames
    except Exception as e:
        print(f"Error loading {csv_file}: {str(e)}")
        return []

def find_not_following_back(following_list, followers_list):
    """Finds users that you follow but they don't follow you back."""
    return [user for user in following_list if user not in followers_list]

def save_results_to_csv(usernames, output_file):
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

def compare_and_save_results(output_folder='processed_data'):
    """Compares followers and following lists, and saves the results."""
    # File paths
    followers_csv = os.path.join(output_folder, 'followers.csv')
    following_csv = os.path.join(output_folder, 'following.csv')
    not_following_back_csv = os.path.join(output_folder, 'not_following_back.csv')

    # Load data
    followers = load_usernames_from_csv(followers_csv)
    following = load_usernames_from_csv(following_csv)

    # Find users who don't follow you back
    not_following_back = find_not_following_back(following, followers)

    # Save results
    save_results_to_csv(not_following_back, not_following_back_csv)

    # Print results
    print(f"Analysis completed and saved to {not_following_back_csv}")
    print(f"Users who you follow but don't follow you back: {len(not_following_back)}")
    
    # Show some examples
    if not_following_back:
        print("\nSome examples (first 5):")
        for user in not_following_back[:5]:
            print(f"- {user}")
        if len(not_following_back) > 5:
            print(f"... and {len(not_following_back) - 5} more")
    
    return len(not_following_back)

# If this script is run directly
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Compare Instagram followers.')
    parser.add_argument('--folder', '-f', default='processed_data',
                      help='Folder containing the CSV files')
    
    args = parser.parse_args()
    compare_and_save_results(args.folder)