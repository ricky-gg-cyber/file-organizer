# file-organizer

A command-line tool that sorts the files in a folder into subfolders by extension.

## Features
- Creates one subfolder per file extension (e.g. `jpg/`, `txt/`)
- Puts files without an extension in `Others/`
- Renames duplicates instead of overwriting them
- `--dry-run` mode to preview changes without moving anything

## Requirements
- Python 3.6 or newer (no external packages)

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
  photo.JPG
  b.txt
  notes
```
After:
```
folder/
 txt/
    a.txt
    b.txt
  jpg/
    photo.JPG
  Others/
    notes
```

## dry-run example
Given this folder:

```
demo/
  a.txt
  b.txt
  photo.JPG
  notes
  .hidden
  txt/
    a.txt
```

Running:

```bash
python organizer.py demo --dry-run
```
prints:

```
a.txt --> txt/a_1.txt
b.txt --> txt/b.txt
notes --> Others/notes
photo.JPG --> jpg/photo.JPG
```
Nothing is changed on disk. Hidden files (`.hidden`) and existing subfolders
are ignored, and `a.txt` is shown with its new name because `txt/a.txt`
already exists. Run the command again without `--dry-run` to apply the changes.


## Notes
- Hidden files are skipped.
- If the file .py with the program itself is in the folder that is getting organized it will be moved inside the py folder.
- Duplicates are renamed as `name_1.ext`, `name_2.ext`, ...
