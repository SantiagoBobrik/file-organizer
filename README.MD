# File Organizer

A Python script to categorize and organize files in a folder based on their file extension.

## Table of contents

*   [Features](#features)
*   [Usage](#usage)
    *   [Prerequisites](#prerequisites)
*   [Before and After Example](#before-and-after-example)
*   [File Types](#file-types)
## Features

*   Supports Windows and macOS.
*   Creates separate folders for different file types (e.g. images, documents, etc.).
*   Renames files if they already exist in the destination folder with a timestamp prefix.

## Usage

1.  Clone or download the repository.
2.  Run the `main.py` file.
3.  The script will automatically categorize and organize files in the default download folder.

### Prerequisites

*   Python installed

## Before and After example
 
Before 

```
downloads/
|
|-- file1.jpg
|-- file2.pdf
|-- file3.mp3
|-- file4.docx
|-- file5.zip

```

After

```
downloads/
|
|-- images/
|   |
|   |-- file1.jpg
|
|-- documents/
|   |
|   |-- file2.pdf
|   |-- file4.docx
|
|-- sounds/
|   |
|   |-- file3.mp3
|
|-- compressed/
|   |
|   |-- file5.zip
```

## File Types

The `file_extensions` dictionary stores a list of file extensions for different file categories. You can modify it to suit your needs by adding, removing, or changing the file extensions as needed. 
The current file categories are:

*   Images: `jpg`, `jpeg`, `png`, `gif`, `svg`, `bmp`, `ico`, `psd`, `tif`, `tiff`, `webp`
*   Documents: `doc`, `docx`, `pdf`, `txt`, `xls`, `xlsx`, `ppt`, `pptx`, `md`, `epub`, `csv`
*   Apps: `exe`, `dmg`, `pkg`, `deb`, `rpm`
*   Compressed: `zip`, `rar`, `tar`, `gz`, `7z`, `iso`
*   Sounds: `mp3`, `wav`, `ogg`, `flac`, `aac`
*   Videos: `mp4`, `mkv`, `avi`, `mov`, `wmv`, `flv`, `webm`, `3gp`
*   Other: `bin`, `dat`, `db`, `log`, `msi`, `part`, `torrent`, `nupkg`


