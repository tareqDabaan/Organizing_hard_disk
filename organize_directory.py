import os
import shutil


# Set a variable to store extensions 
image_extensions = (".png", ".jpg", ".jpeg")
code_extensions = (".html", ".js", ".cpp")
file_extensions = (".pdf")
microsoft_extensions = (".accdt", ".pptx", ".docx", "xlsx")
executable_files_extensions = (".exe")
compressed_files_extensions = (".rar", ".zip")

current_code_directory = os.path.dirname(os.path.realpath(__file__))


def organize():
    # Start looping on all files in the current directory
    for filename in os.listdir(current_code_directory):
        
        # Organizing images to a specific folder
        if filename.endswith(image_extensions):
            
            if not os.path.exists("Images"):
                os.mkdir('Images')
            shutil.copy(filename, "Images")
            os.remove(filename)
        
        # Organizing codes to a specific folder
        elif filename.endswith(code_extensions):
            
            if not os.path.exists("Code"):
                os.mkdir('Code')
            shutil.copy(filename, "Code")
            os.remove(filename)
        
        # Organizing PDF to a specific folder    
        elif filename.endswith(file_extensions):
            
            if not os.path.exists("Pdf"):
                os.mkdir('Pdf')
            shutil.copy(filename, "Pdf")
            os.remove(filename)

        # Organizing microsoft files to a specific folder    
        elif filename.endswith(microsoft_extensions):
            
            if not os.path.exists("Microsoft"):
                os.mkdir('Microsoft')
            shutil.copy(filename, "Microsoft")
            os.remove(filename)

        # Organizing exe files to a specific folder    
        elif filename.endswith(executable_files_extensions):
            
            if not os.path.exists("Executable_files"):
                os.mkdir('Executable_files')
            shutil.copy(filename, "Executable_files")
            os.remove(filename)
            
        # Organizing compressed files to a specific folder    
        elif filename.endswith(compressed_files_extensions):
            
            if not os.path.exists("Compressed_files"):
                os.mkdir('Compressed_files')
            shutil.copy(filename, "Compressed_files")
            os.remove(filename)

            print("Organized your hard disk successfully.")

organize()