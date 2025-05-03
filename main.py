import os
import sys
import time
import argparse
from extract_usernames import extract_and_save_usernames
from compare_followers import compare_and_save_results

def print_separator():
    """Prints a separator line to the console."""
    print("=" * 60)

def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description='Analyze who doesn\'t follow you back on Instagram.')
    parser.add_argument('input_folder', nargs='?', default='data', 
                      help='Folder containing HTML files (followers_1.html and following.html)')
    parser.add_argument('--output', '-o', 
                      help='Folder to save results (default: processed_[input_folder])')
    
    # Parse the arguments
    args = parser.parse_args()
    input_folder = args.input_folder
    
    # Generate output folder name based on input folder if not specified
    if args.output:
        output_folder = args.output
    else:
        # Extract only the base name of the folder, without the full path
        base_folder_name = os.path.basename(input_folder)
        output_folder = f"processed_{base_folder_name}"
    
    # Verify that the input folder exists
    if not os.path.exists(input_folder):
        print(f"Error: The folder '{input_folder}' does not exist.")
        print("Create the folder and place followers_1.html and following.html files inside.")
        return 1
    
    # Verify that the necessary HTML files exist
    followers_file = os.path.join(input_folder, 'followers_1.html')
    following_file = os.path.join(input_folder, 'following.html')
    
    if not os.path.exists(followers_file):
        print(f"Error: File {followers_file} not found")
        return 1
    
    if not os.path.exists(following_file):
        print(f"Error: File {following_file} not found")
        return 1
    
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Show information to the user
    print_separator()
    print("NOT-A-FAN")
    print_separator()
    print(f"Input folder: {input_folder}")
    print(f"Output folder: {output_folder}")
    
    # STEP 1: Extract usernames from HTML files
    print_separator()
    print("STEP 1: Extracting usernames...")
    followers_count, following_count = extract_and_save_usernames(
        input_folder, output_folder
    )
    
    # STEP 2: Compare followers and following
    print_separator()
    print("STEP 2: Comparing followers and following...")
    not_following_count = compare_and_save_results(output_folder)
    
    # Final summary
    print_separator()
    print("ANALYSIS SUMMARY")
    print_separator()
    print(f"Total followers: {followers_count}")
    print(f"Total following: {following_count}")
    print(f"Users you follow who DON'T follow you back: {not_following_count}")
    print_separator()
    print("Generated files:")
    print(f"- {os.path.join(output_folder, 'followers.csv')}")
    print(f"- {os.path.join(output_folder, 'following.csv')}")
    print(f"- {os.path.join(output_folder, 'not_following_back.csv')}")
    print_separator()
    
    return 0

if __name__ == "__main__":
    start_time = time.time()
    exit_code = main()
    elapsed_time = time.time() - start_time
    print(f"Execution time: {elapsed_time:.2f} seconds")
    sys.exit(exit_code)