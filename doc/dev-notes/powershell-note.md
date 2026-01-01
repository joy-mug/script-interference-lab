
# C:\Program Files\PTC 這個資料夾開始，遞迴搜尋它底下所有子資料夾，找出檔名符合 *ipfc*.jar 的檔案。」
dir "C:\Program Files\PTC" -Recurse -Filter *ipfc*.jar

# 刪單一檔案
Remove-Item "C:\path\to\file.txt"

# 刪除所有(相同副檔檔案) .extand
Remove-Item "C:\path\to\folder\*.extand*"

# 先「看會刪哪些」
Get-ChildItem "C:\path\to\folder\*.pdf"

Remove-Item -path ".\output\*.pdf"

# 刪除「目標資料夾內所有檔案（含子資料夾）
Get-ChildItem "C:\path\to\target" -File -Recurse | Remove-Item

Get-ChildItem -path ".\output" -File -Recurse | Remove-Item


# 一行安全清除（PowerShell，已納入 docs）

Get-ChildItem -Force |
Where-Object {
    $_.Name -notin @(
        "drawing_edit.py",
        "pdf_handler.py",
        "dwg_handler.py",
        "naming_rules.py",
        "README.md",
        "sample_input",
        "output",
        "docs",
        ".git"
    )
} |
Remove-Item -Recurse -Force

# Create the folder docs\dev-notes
New-Item -ItemType Directory -Path docs\dev-notes

# Create files inside the folder
New-Item -ItemType File -Path docs\dev-notes\powershell.md

# Copy a whole folder (recommended)
Copy-Item -Path docs\dev-notes -Destination C:\Projects\other-repo\docs\dev-notes -Recurse

# Copy a single file
Copy-Item -Path docs\dev-notes\git.md -Destination C:\Projects\other-repo\docs\dev-notes\git.md

# Copy from current repo to target repo (safe workflow)
cd C:\Users\11006189\creo-drawing-automation
Copy-Item -Path doc -Destination C:\Users\11006189\script-interference-lab\doc\dev-notes -Recurse


# cut / move instead of copy
Move-Item -Path docs\dev-notes -Destination C:\Projects\other-repo\docs\dev-notes

# Remove a folder with files inside
Remove-Item -Path docs\dev-notes -Recurse
# -Recurse = delete all contents

# Restore again from the committed branch
git restore --source feature/drawing-edit doc

# Check the current working directory
pwd

# Copy all files with ONE extension
Copy-Item -Path *.md -Destination C:\Target\Folder
# Copy MULTIPLE extensions at once
Get-ChildItem -Recurse -Include *.md, *.txt | Copy-Item -Destination C:\Target\Folder

# Copy files (single folder) and replace same-name files
Copy-Item -Path *.md -Destination C:\Target\Folder -Force

# Verify files
Get-ChildItem -Recurse -Filter *.md

# display the tree
tree /f

# Using an explicit path variable (clean & safe)
$path = "src\hp_reviewer"
New-Item "$path\a.py", "$path\b.py", "$path\c.py" -ItemType File -Force

# Get the absolute path of your repo
 $repo = git rev-parse --show-toplevel 

# Build an absolute target path
$target = Join-Path $repo "src\hp_reviewer"

# Create files using the absolute path
 New-Item "$target\a.py", "$target\b.py", "$target\c.py" -ItemType File -Force

# Session-scoped variable (TEMPORARY)
 $target = "C:\path\to\folder"
# Global variable (still TEMPORARY, but wider)
 $global:target = "C:\path"
# Permanent variable (profile-based)
# Step 1 — Open your PowerShell profile
 notepad $PROFILE
# Step 2 — Add the variable
 $targetRepo = "C:\Users\11006189\creo-drawing-automation"


# This moves you back one folder (parent directory)
 cd ..

# Quick directory listing
 ls