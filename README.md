# Desktop Cleaner

A Python script that automatically organizes files on your desktop by categorizing them into specific folders based on their file extensions.

## Features

* Automatically scans desktop for files
* Creates organized category folders (Images, Documents, Videos, etc.)
* Moves files to appropriate folders based on file type
* Provides a summary of actions taken

## Supported Categories

* Images (".jpg", ".jpeg", ".png", ".gif", ".bmp")
* Documents (".txt", ".pdf", ".doc", ".docx", ".xlsx", ".pptx")
* Videos (".mp4", ".mkv", ".avi", ".mov")
* Audio (".mp3", ".wav", ".aac", ".flac")
* Games and apps (".url", ".lnk")
* Others (any unmatched extensions)

## Prerequisites

* Python 3.6 or higher
* No additional packages required (uses only standard library)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/desktop-cleaner.git
```

2. Navigate to the project directory:
```bash
cd desktop-cleaner
```

## Usage

1. Place the script on your desktop or copy it to the location you want to organize
2. Run the script:
```bash
python desktop_cleaner.py
```

The script will:
1. Create category folders if they don't exist
2. Move files to their respective folders
