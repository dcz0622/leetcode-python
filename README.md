# leetcode

This repository contains solutions to LeetCode. It uses venv for managing Python environments.

* Create a new virtual environment:
  
  ```bash
  python3 -m venv ${virtual_environment_name}
  ```
  
* Activating the virtual environment:
  
  ```bash
  cd ${virtual_environment_name}
  source ./bin/activate
  ```
  
* Deactivating the virtual environment:
  
  ```bash
  deactivate
  ```
  
* Configure VS Code to use the virtual Python interpreter (Mac OS):
  * Go to Command Palette (shortcut: "cmd-shift-P").
  * Go to "Python: Select Interpreter".
  * Enter Python interpreter path. Note: Manually enter the path to your virtual Python executable (can be found using
    `which python`), instead of choosing from Finder. Reason: We don't want to follow the symbolic link.
