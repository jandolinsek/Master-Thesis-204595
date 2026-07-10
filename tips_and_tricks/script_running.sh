#!/bin/bash

# 1. Ensure ~/bin exists and is on PATH (idempotent)
mkdir -p "$HOME/bin"
if ! echo "$PATH" | tr ':' '\n' | grep -qx "$HOME/bin"; then
  echo 'export PATH="$HOME/bin:$PATH"' >> "$HOME/.bashrc"
  export PATH="$HOME/bin:$PATH"
fi

# 2. Make the script executable
chmod +x $HOME/00_scripts/create_directories.py
chmod +x $HOME/00_scripts/read_analysis.py

# 3. Create (or update) the symlink in ~/bin
ln -sf $HOME/00_scripts/create_directories.py "$HOME/bin/cdir"
ln -sf $HOME/00_scripts/read_analysis.py "$HOME/bin/run"

# 4. Make sure the scripts have Unix line endings
# dos2unix $HOME/00_scripts/create_directories.py 
# dos2unix $HOME/00_scripts/read_analysis.py

