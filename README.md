# File Organizer CLI

A simple Python command-line tool that organizes files into folders based on their type.

## Usage

```bash
python src/main.py --source-dir <source> --target-dir <target>
```

Example:

```bash
python src/main.py --source-dir ~/Downloads --target-dir ~/Organized
```

## Demo

A `demo/` folder is included so you can safely test the script.

* `demo/source_dir` → contains sample files
* `demo/target_dir` → output will be created here

Run:

```bash
python src/main.py --source-dir demo/source_dir --target-dir demo/target_dir
```

## Features

* Organizes files by type (images, PDFs, text, music, etc.)
* Automatically creates folders
* Prevents file overwrites

## Requirements

No external dependencies required (Python standard library only)
