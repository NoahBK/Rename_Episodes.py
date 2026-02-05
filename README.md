# Rename_Episode.py

This Python script automates the renaming of video files in a directory based on embedded metadata, ensuring consistent, clean filenames that match the official episode or movie titles.

## Features

- Automatically scans the current folder (or a specified directory) for video files (`.mp4`, `.mkv`, `.avi`, etc.)
- Extracts detailed metadata from each file using `pymediainfo` (a wrapper around the MediaInfo library)
- Retrieves key information such as:
  - `Title` (e.g., `S01:E01 - Episode Name`)
  - `Season` and `Episode` numbers
  - Optional descriptions or part identifiers
  - File-specific attributes like duration, bitrate, codec, and creation/modification dates
- Normalizes and formats titles for safe filenames:
  - Removes or replaces invalid filesystem characters
  - Preserves official punctuation (e.g., ellipses in `Denise Says...`)
  - Zero-pads episode numbers for proper sorting (e.g., `S01E01`)
- Compares current filenames to metadata-derived target names
- Renames files if discrepancies are found while:
  - Avoiding overwriting existing files
  - Handling filesystem errors gracefully
- Provides detailed logs:
  - Metadata retrieved for each file
  - Whether a rename was needed
  - Old and new filenames for renamed files
  - Warnings if metadata is missing or malformed

## Technical Details

- Uses `pymediainfo` to parse each file’s General track for reliable metadata extraction
- Works independently in any folder without hardcoding paths
- Preserves special characters and Unicode (apostrophes, ellipses, etc.) exactly as in the metadata
- Does not modify video or audio streams; only renames files
- Ideal for preparing media libraries for Plex, Jellyfin, Kodi, or other media servers that require consistent naming

## Use Cases

- Cleaning up downloaded TV shows or movies from streaming sources
- Ensuring consistent, standardized filenames for media server metadata matching
- Saving time when managing large collections

