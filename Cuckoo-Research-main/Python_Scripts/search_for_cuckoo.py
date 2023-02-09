# Bella Wengappuly      31 Jan 2023         Cuckoo Research
# This script should allow you to search all files in a folder for 
# the string "Cuckoo". 

# Global code variables at the top of the page allow for folder and 
# search term modification. 
import os

SEARCH_TERM = "Black-billed Cuckoo"
SEARCH_TERM2 = "Yellow-billed Cuckoo"
# for path, all \ must be changed to \\
PATH_TO_FOLDER = "E:\\BirdNET_Classifier_Runs\\2022_FWPR7_Classifier_Runs\\BUR-2"

def searchText(SEARCH_TERM, path):
    positive_count = 0
    os.chdir(path)
    files = os.listdir()
    #print(files)
    for file_name in files:
        #print(file_name)
        abs_path = os.path.abspath(file_name)
        
        if os.path.isdir(abs_path):
            searchText(abs_path)
            
        if os.path.isfile(abs_path):
             with open(file_name, 'r', encoding='utf-8') as f:
                if SEARCH_TERM in f.read():
                    final_path = os.path.abspath(file_name)
                    # print(SEARCH_TERM + " word found in this path " + final_path)
                    # print(file_name)
                    val1 = file_name.split(".")
                    print(val1[0])
                    positive_count += 1
                # else:
                #     print("No match found in " + abs_path)
    print("\nNumber of files found with word", SEARCH_TERM, ":", positive_count, "\n")
    pass

searchText(SEARCH_TERM, PATH_TO_FOLDER)
searchText(SEARCH_TERM2, PATH_TO_FOLDER)
