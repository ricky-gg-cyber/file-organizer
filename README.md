# file-organizer

A command-line tool that sorts the files in a folder into subfolders by extension.

## Features
- Creates one subfolder per file extension (e.g. `jpg/`, `txt/`)
- Puts files without an extension in `Others/`
- Renames duplicates instead of overwriting them
- `--dry-run` mode to preview changes without moving anything

## Requirements
- Python 3.x (no external packages)

## Installation
```bash
git clone https://github.com/ricky-gg-cyber/file-organizer.git
cd file-organizer
```

## Usage
```bash
python organizer.py /path/to/folder
python organizer.py /path/to/folder --dry-run
```

## Example
Before:
```
folder/
  a.txt
  photo.jpg
```
After:
```
folder/
  txt/a.txt
  jpg/photo.jpg
```

## Notes
- Hidden files are skipperd.
- If the file .py with the program itself is in the folder that is getting organized it will be moved inside the py folder.
- Duplicates are renamed as `name_1.ext`, `name_2.ext`, ...

## Running the tests
```bash
pytest
```