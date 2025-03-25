# file-flattener

A simple Python utility that recursively extracts all files from nested directories and copies them to a single destination folder.

## Description

`file-flattener` is a lightweight tool that traverses through complex directory structures and copies all files to a single destination folder. It maintains the original filenames while flattening the directory hierarchy, making it useful for consolidating files scattered across nested folders.

## Features

- Recursively traverses all subdirectories in the source folder
- Copies all files to a single destination directory
- Preserves original file metadata using `shutil.copy2`
- Creates the destination directory if it doesn't exist
- Provides error handling and logging during the copy process


## Limitations

- Files with identical names will overwrite each other in the destination folder
- The original folder structure is not preserved
- Large file collections may take significant time to process
