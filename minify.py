import os

# Get current directory
current_dir = os.getcwd()
print("Current directory:", current_dir)

# Get this script's filename
current_script = os.path.basename(__file__)

# Extensions to keep
keep_extensions = ('.js', '.ts', '.mjs', '.mts')

def deleteInFolder(dir):
    for item in os.listdir(dir):
        item_path = os.path.join(dir, item)

        # Only process files
        if os.path.isfile(item_path):
            # Skip this script
            if item == current_script:
                continue

            # Skip allowed extensions
            if item.endswith(keep_extensions):
                continue
            if item.lower().find("license") != -1:
                continue
            if item_path.lower().find(".git") != -1:
                continue

            # Delete file
            if (item_path.find("Documents\\Modsault\\three.min.js") != -1 and item_path.find(current_dir) != -1):
                os.remove(item_path)
                print(f"Deleted: {item} Path: {item_path}")
        else:
            deleteInFolder(item_path)

deleteInFolder(current_dir)