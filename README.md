# smartorganizer

<img width="503" height="429" alt="image" src="https://github.com/user-attachments/assets/13a93c5f-6f6a-41cc-8198-0bb6609559fc" />


✨ Features

Simple graphical user interface (GUI)

Select any folder on your computer

Automatically sorts files by extension into categories:

Images → .jpg, .jpeg, .png, .gif, .bmp

Documents → .pdf, .docx, .txt, .xlsx, .pptx

Audio → .mp3, .wav, .aac, .flac

Videos → .mp4, .avi, .mkv, .mov

Other → Any unsupported file types

Real-time activity log

Success & error notifications

Automatically creates folders if they don't exist

🛠️ Requirements

Python 3.x

No external dependencies required
(Uses built-in modules: os, shutil, tkinter)

🚀 How to Run

Make sure Python 3 is installed:

python --version

Save the script as:

simple_organizer.py

Run the application:

python simple_organizer.py

In the app:

Click Select Folder

Choose the folder you want to organize

Click Start Organizing

📁 How It Works

The program:

Scans all files in the selected directory.

Checks each file's extension.

Matches it to a predefined category.

Creates category folders if they don't exist.

Moves the file into its appropriate folder.

Displays progress in the log window.

Folders created automatically:

SelectedFolder/
│
├── Images/
├── Documents/
├── Audio/
├── Videos/
└── Other/
⚙️ Customization

To add more file types or categories, modify the EXTENTIONS dictionary in the script:

EXTENTIONS = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
}

You can add new categories like:

'Archives': ['.zip', '.rar', '.7z']
⚠️ Notes

Only files in the top level of the selected folder are organized.

Subfolders are ignored.

Files without extensions are not moved.

Existing files with the same name in destination folders may cause errors.

📌 Future Improvements (Optional Ideas)

Recursive sorting (include subfolders)

Drag-and-drop folder support

Dark mode

Undo functionality

Progress bar

Duplicate file handling

📄 License

This project is open-source and free to use.
