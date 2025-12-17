# Inside file_cd, insert commands to create three new folders (directories).

New-Item -ItemType Directory -Path "Folder1"
New-Item -ItemType Directory -Path "Folder2"
New-Item -ItemType Directory -Path "Folder3"

# Insert commands to navigate inside one of the folders you created 

Set-Location -Path "Folder2"

# Create three new folders inside this folder.

New-Item -ItemType Directory -Path "Folder2.1"
New-Item -ItemType Directory -Path "Folder2.2"
New-Item -ItemType Directory -Path "Folder2.3"

# Insert commands to remove two of the folders you created

Set-Location -Path "Folder2.1"
Remove-Item -Path "..\Folder2.2" -Recurse
Remove-Item -Path "..\Folder2.3" -Recurse