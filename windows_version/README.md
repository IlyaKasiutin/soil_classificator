# How to make an executable from src
Option №1:
1. Install Pyinstaller following official manual: https://pyinstaller.org/en/stable/
2. Type in windows terminal command:
```shell
pyinstaller predictor.spec
```
3. Run predictor.exe from the dist folder

__Important__: the current version requires a folder called 'images' with the source images and a 'model_params' file in the same directory as the .exe file.
The program will write processed images to the folder 'labeled_images'.
