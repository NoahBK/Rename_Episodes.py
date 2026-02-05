import os
import subprocess
import re
import json

FOLDER = "."
VIDEO_EXTENSIONS = ['.mp4', '.mkv', '.avi', '.mov']
LOG_FILE = os.path.join(FOLDER, "log.txt")

def sanitize_filename(name):
    # Replace illegal characters with dot
    name = re.sub(r'[<>:"/\\|?*\uFF1A]', '.', name)
    # Replace multiple dots with single, but preserve trailing dots before extension
    if '.' in name:
        parts = name.rsplit('.', 1)
        parts[0] = re.sub(r'\.{2,}', '.', parts[0])
        name = '.'.join(parts)
    else:
        name = re.sub(r'\.{2,}', '.', name)
    return name.strip()

def get_mediainfo(file_path):
    try:
        result = subprocess.run(
            ["mediainfo", "--Output=JSON", file_path],
            capture_output=True, text=True, check=True
        )
        return json.loads(result.stdout)
    except Exception as e:
        log(f"Error reading mediainfo for {file_path}: {e}")
        return None

def log(message):
    print(message)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(message + "\n")

def generate_filename(info):
    general = next((t for t in info['media']['track'] if t.get('@type') == "General"), None)
    if not general:
        return None

    # Season and Episode
    season = int(general.get("Season", 0))
    episode = int(general.get("Part", 0))

    # Episode title: optional
    ep_title = general.get("extra", {}).get("Part_ID", "").strip()
    if ep_title == "":
        ep_title = None
    else:
        ep_title = ep_title.replace('：', ':').strip()
        # Keep trailing dots in title
        ep_title = re.sub(r'\.{2,}', '.', ep_title)

    # Video info
    video = next((t for t in info['media']['track'] if t.get('@type') == 'Video'), None)
    resolution = f"{video.get('Height', '')}p" if video else ""
    vcodec = video.get('Format', 'H.264').replace('AVC', 'H.264') if video else 'H.264'

    # Audio info
    audio = next((t for t in info['media']['track'] if t.get('@type') == 'Audio'), None)
    if audio:
        channels = audio.get('Channel_s_', '2').replace(' ', '')
        acodec = audio.get('Format', 'AAC').replace('LC','').strip()
        acodec_str = f"{acodec}{channels}"
    else:
        acodec_str = "AAC2.0"

    # Source from Comment URL
    comment = general.get('Comment', '').lower()
    source = "WEB-DL"
    if 'tubi' in comment:
        source = "Tubi.WEB-DL"

    # Extension
    ext = os.path.splitext(general.get("CompleteName", ""))[1] or ".mp4"

    # Build filename
    parts = [f"S{season:02d}E{episode:02d}"]
    if ep_title:
        parts.append(ep_title)
    parts.extend([resolution, source, acodec_str, vcodec])
    new_name = '.'.join(filter(None, parts)) + "-NoahBK" + ext
    return sanitize_filename(new_name)

# Clear previous log
if os.path.exists(LOG_FILE):
    os.remove(LOG_FILE)

log("Starting renaming process...\n")

for file in os.listdir(FOLDER):
    file_path = os.path.join(FOLDER, file)
    ext = os.path.splitext(file)[1].lower()

    if not os.path.isfile(file_path) or ext not in VIDEO_EXTENSIONS or file.lower().endswith('.py'):
        continue

    info = get_mediainfo(file_path)
    if not info:
        log(f"Skipping {file} (no mediainfo)")
        continue

    general = next((t for t in info['media']['track'] if t.get('@type') == "General"), None)
    log(f"\nFile: {file}")
    log(f"General track: {general}")

    new_name = generate_filename(info)
    if not new_name:
        log(f"Skipping {file} (could not generate filename)")
        continue

    new_path = os.path.join(FOLDER, new_name)
    if file_path != new_path:
        log(f"Renaming:\n  {file}\n  -> {new_name}\n")
        os.rename(file_path, new_path)
    else:
        log(f"No rename needed for {file}")

log("\nDone renaming all video files.")