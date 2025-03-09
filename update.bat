@echo off
echo Suppression des anciens fichiers...
rmdir /s /q dist build
del generateur_id.spec

echo Compilation du nouvel exe...
pyinstaller --onefile --noconsole generateur_id.py

echo Mise à jour terminée !
pause
