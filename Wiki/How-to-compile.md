# How to compile SPP-IN-Soundux on Windows? 
`last update: 31.10.2024`

<br>
<br>

## Step 1: Install Python

1. Download the Python 3.11 installer from the [official website](https://www.python.org/downloads/).
2. Run the installer, selecting the option **"Add Python to PATH"**.
3. After installation, open the terminal or command prompt and enter:

## Step 2: Download the repository

1. Go to the [SPP-IN-Soundux page on GitHub](https://github.com/Agzes/SPP-IN-Soundux).
2. Click on the **"Code"** button and select **"Download ZIP"**.
3. Extract the downloaded ZIP file to a convenient location.

## Step 3: Set up a virtual environment (recommended)

Creating a virtual environment will isolate the project dependencies from the global Python libraries.

1. Navigate to the extracted repository folder:
   ```bash
   cd path/to/your/repository
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   ```bash
   venv/Scripts/activate
   ```

## Step 4: Install dependencies

The repository includes a `requirements.txt` file. Install all dependencies using the following command:
```bash
pip install -r requirements.txt
```

## Step 5: Run the Python file

After installing dependencies, you can run the main Python file to check the installed libraries.

```bash
python main.py
```

## Step 6: Compile using PyInstaller

1. Install PyInstaller:
   ```bash
   pip install PyInstaller
   ```
2. Run the compilation for the `tools.py` file (remember to replace `C:\Path\To\`):
   ```bash
   pyinstaller --noconfirm --onefile --windowed --icon "C:\Path\To\SPP-IN-Soundux\Data\logo\tools.ico" --name "tools" --clean  "C:\Path\To\SPP-IN-Soundux\main.py"
   ```
3. Navigate to the folder created by PyInstaller and move the `tools.exe` file into the repository folder.
4. Run the compilation for the `main.py` file (remember to replace `C:\Path\To\`):
    ```bash
    pyinstaller --noconfirm --onefile --windowed --icon "C:\Path\To\SPP-IN-Soundux\Data\logo\logo.ico" --name "SPP-IN-Soundux" --clean --add-data "C:\Path\To\SPP-IN-Soundux\tools.exe;." --add-data "C:\Path\To\SPP-IN-Soundux\Data;Data/" --collect-all "fake_useragent"  "C:\Path\To\SPP-IN-Soundux\main.py" 
    ```
5. Move the `SPP-IN-Soundux.exe` file into the repository folder or paste a folder `Data` to exe file.

## Finishing up

To deactivate the virtual environment, run:
```bash
deactivate
```

