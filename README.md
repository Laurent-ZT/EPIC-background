## Daily NASA EPIC-DSCOVR background

Set your desktop background to the latest natural color image of Earth captured by NASA's EPIC camera aboard the DSCOVR spacecraft.

### Customize the script for your preferred longitude

To see the closest picture from your preferred longitude, modify the `LONGITUDE_CITY` variable in the script. By default, the script displays the closest picture to Paris.

### Configure the script to start automatically on Windows

1. Create a shortcut to your Python script by right-clicking on it and selecting "Create Shortcut".
2. Right-click on the new shortcut and choose "Properties".
3. In the "Target" field, add the full path to your Python executable before the path to your script, like this:
    ```
    "C:\Path\To\Python\python.exe" "C:\Path\To\Your\Script.py"
    ```
    Make sure to replace `C:\Path\To\Python` with the actual path to your Python installation directory, and `C:\Path\To\Your\Script.py` with the full path to your script file.
4. Press the Windows key + R to open the Run dialog box, then type `shell:startup` and press Enter.
5. Drag the shortcut you just created into the Startup folder that opens.
6. To prevent a terminal window from opening when the script runs at startup, use `pythonw.exe` instead of `python.exe` in the "Target" field of the shortcut.
