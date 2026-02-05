# Rename_Episodes.py

![Rename_Episodes](https://i.ibb.co/PzZw701x/54b5505c-f950-48ef-9c65-94f020dd85fe.png)

---

## Overview

**Rename_Episodes.py** is a Python script that automates the renaming of video files in a directory based on embedded metadata, ensuring clean, consistent filenames that match official episode or movie titles. It’s perfect for anyone who wants a professional, organized media library without spending hours manually renaming files.

The script works in any folder, automatically scanning video files (.mp4, .mkv, .avi, etc.), extracting metadata, and applying a standardized naming convention while handling special characters, punctuation, and edge cases like ellipses in titles.

---

## Features

- Automatically scans the current folder (or a specified directory) for video files
- Extracts detailed metadata from each file using pymediainfo (a wrapper around MediaInfo)
- Retrieves key information such as:
  - Title (e.g., S01E01 - Episode Name)
  - Season and Episode numbers
  - Optional descriptions or part identifiers
  - File-specific attributes like duration, bitrate, codec, and creation/modification dates
- Normalizes and formats titles for safe filenames:
  - Removes or replaces invalid filesystem characters
  - Preserves official punctuation (e.g., ellipses in Denise Says...)
  - Zero-pads episode numbers for proper sorting (e.g., S01E01)
- Compares current filenames to metadata-derived target names
- Renames files if discrepancies are found while:
  - Avoiding overwriting existing files
  - Handling filesystem errors gracefully
- Provides detailed logs:
  - Metadata retrieved for each file
  - Whether a rename was needed
  - Old and new filenames for renamed files
  - Warnings if metadata is missing or malformed

---

## Example

Before Renaming:

S01E01.On the Straight and Narrow.720p.Tubi.WEB-DL.AAC2.H.264.mp4  
S01E14.Denise Says.720p.Tubi.WEB-DL.AAC2.H.264.mp4

After Renaming:

S01E01.On the Straight and Narrow.720p.Tubi.WEB-DL.AAC2.H.264-NoahBK.mp4  
S01E14.Denise Says...720p.Tubi.WEB-DL.AAC2.H.264-NoahBK.mp4

Notice how the script preserves ellipses and appends the NoahBK tag only in the after filenames for consistency and professional presentation.

---

## How It Works (Technical)

1. File Scanning: Detects all supported video files in the directory.  
2. Metadata Extraction: Uses pymediainfo to read metadata, including Title, Season, Episode, comments, and file attributes.  
3. Filename Formatting: Builds clean, standardized filenames:  
   S{season:02}E{episode:02}.{title}.{resolution}.{source}.{audio}.{codec}-{tag}.ext  
   - Handles invalid filesystem characters  
   - Preserves stylistic punctuation and Unicode characters  
4. Conflict Avoidance: Prevents duplicate filenames and appends indices if needed.  
5. Renaming: Updates the file on disk while logging changes.  
6. Reporting: Prints a summary of renamed and untouched files for verification.  

This ensures professional, consistent filenames ready for Plex, Jellyfin, Kodi, or any media server.

---

## Use Cases

- Cleaning up downloaded TV shows or movies from streaming sources  
- Standardizing filenames for media server metadata matching  
- Saving time managing large collections  
- Maintaining organized libraries without manual editing

---

## Installation

1. Make sure you have Python 3.10 or higher installed. You can download it from the [official Python website](https://www.python.org/downloads/).

2. Install the required Python library by running *pip install pymediainfo* in your terminal or command prompt.

3. Place the `Rename_Episode.py` script in the folder containing your video files.

---

## Usage

Run the script from the terminal or command prompt:

python Rename_Episodes.py

The script will scan all video files in the folder, extract metadata, and rename them according to the embedded information. It logs all actions and reports any missing or malformed metadata.

---

## Screenshots / Visual Examples

Before / After Comparison:  
[![Descriptive Alt Text](https://i.ibb.co/qM50TPDv/a0988278-7b99-467f-9622-6c7c8e983117.png)](https://ibb.co/5WFYbf1P)

---

## License

MIT License

---

## Credits

- Developed by NoahBK
- With an insane amount of help from ole' ChatGPT (I am retarded)
- Uses pymediainfo for metadata extraction  
- Header and promotional images generated with AI
