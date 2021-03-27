@echo off
set "Browser"Dir=C:\"the path to your browser's user data file"

del /q /s /f ""%BrowserDir%""
rd /s /q ""%BrowserDir%""
