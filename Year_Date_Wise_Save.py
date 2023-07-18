import os
import shutil
from datetime import datetime

# Prompt the user for the location of the media files
location = input("Enter the location of the media files: ")

# Create a new directory to store the organized media files
organized_folder = "Organized Media Files"
os.makedirs(organized_folder, exist_ok=True)

# Loop through all the files in the original location
for filename in os.listdir(location):
    # Get the full path of the file
    filepath = os.path.join(location, filename)
    
    # Get the modification timestamp of the file
    timestamp = os.path.getmtime(filepath)
    modified_date = datetime.fromtimestamp(timestamp)
    
    # Create the year and month folders if they don't exist
    year_folder = os.path.join(organized_folder, str(modified_date.year))
    os.makedirs(year_folder, exist_ok=True)
    month_folder = os.path.join(year_folder, modified_date.strftime("%B"))
    os.makedirs(month_folder, exist_ok=True)
    
    # Copy the file to the appropriate folder
    shutil.copy2(filepath, month_folder)
    


    #this is the second change that did to this source code 
print("Media files organized successfully!")
