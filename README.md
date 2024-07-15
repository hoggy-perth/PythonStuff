# PythonStuff
Learning some Python programming 

So far have:

Installed Python as admin on Windows PC so that it gets installed for all users.

I also installed GIT and then Visual Studio Code 

Installed the Python extension into Visual Studio Code

Note when using the python installer (pip) if you execute from a terminal in Visual Studio Code it will run as user not admin so puts stuff into user directory. 

So when I did this for pyinstaller got this message:

Installing collected packages: altgraph, setuptools, pywin32-ctypes, pefile, packaging, pyinstaller-hooks-contrib, pyinstaller
  WARNING: The scripts pyi-archive_viewer.exe, pyi-bindepend.exe, pyi-grab_version.exe, pyi-makespec.exe, pyi-set_version.exe and pyinstaller.exe are installed in 'C:\Users\hogg_\AppData\Roaming\Pytho  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

So had to uninstall (pip uninstall pyinstaller) and then reinstall using command prompt from Task Manager with admin privs then run this command.

pip install pyinstaller --no-cache-dir 

The no chache option forces download

