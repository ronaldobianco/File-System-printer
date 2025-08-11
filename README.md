# File-System-printer

# README — Word-Friendly Folder Tree

A tiny Python script that prints a **folder & file tree** using simple hyphens and spaces—perfect to **copy-paste into Microsoft Word** (or email, tickets, docs).

## Requirements

* Python **3.8+**
* Works on macOS, Linux, and Windows (PowerShell or CMD)

## Quick Start

1. Save the script as `tree_for_word.py`.
2. Run it on a folder:

   ```bash
   python tree_for_word.py /path/to/folder
   ```
3. (Recommended) Save to a text file, then paste into Word:

   ```bash
   python tree_for_word.py /path/to/folder --out tree.txt
   # or
   python tree_for_word.py /path/to/folder > tree.txt
   ```

## Usage

```bash
python tree_for_word.py [PATH] [--all] [--max-depth N] [--out FILE]
```

**Options**

* `PATH` — root folder (default: `.` current directory)
* `--all` — include hidden files/folders
* `--max-depth N` — limit how deep to traverse (e.g., `2`)
* `--out FILE` — write the output to a file (e.g., `tree.txt`)

## Examples

Show current folder:

```bash
python tree_for_word.py
```

Include hidden items and limit depth:

```bash
python tree_for_word.py ~/Projects --all --max-depth 2
```

Write directly to a file:

```bash
python tree_for_word.py C:\Work --out folder_tree.txt
```

## Output Format (copy this into Word)

```
- my_project/
  - src/
    - app.py
    - utils/
      - io.py
  - README.md
```

## Tips

* **Tabs instead of spaces?** In the script, replace:

  ```python
  indent = "  " * (depth + 1)
  ```

  with:

  ```python
  indent = "\t" * (depth + 1)
  ```
* **Windows PowerShell:** `>` redirection works:

  ```powershell
  python .\tree_for_word.py . > tree.txt
  ```

## Troubleshooting

* **“No such file or directory”** — check the `PATH`.
* **PermissionError** — the script skips folders it can’t read.
* **Weird characters in Word** — make sure the file is saved as UTF-8 (the script does this with `--out`).

That’s it—clean, paste-ready folder trees in seconds.
