# Result Scraper: CVMU 
A simple python script to scrape results from CVMU result pages.

## Getting Started

1. Create a virtual environment
```bash
python3 -m venv venv
```

2. Activate the virtual environment
```bash
# Only run one of the following commands
.venv/bin/activate.ps1              # For PowerShell
.venv/bin/activate                  # For Bash
.venv/Scripts/activate.bat          # For CMD
source .venv/Scripts/activate.fish  # For Fish
```

3. Install from requirements.txt
```bash
pip install -r requirements.txt
```

4. Add your start and end roll numbers in `scrapData.py`
```python
...
base_url = "https://ums.cvmu.ac.in/GenerateResultHTML/2143/"
# Note: CSE IoT Sem5 Range Jan 2024
start = '5211001'
end = '5211060'
...
```

5. Run the script
```bash
python3 scrapData.py
```

6. This will generate a `results.json` file in the same directory
> TODO: Add support for configs, pull requests are welcome.

## Generating Results

1. Install `pandoc` and a latex engine (e.g. `texlive`) for your OS (optional)
2. If you are using `pandoc` then enable `systemHasPandoc` in `generateMarkdown.py`
```python
...
systemHasPandoc = True
...
```
3. Generate a markdown file from the json file
```
python3 generateMarkdown.py
```
4. Generate a pdf file from the markdown file
```
pandoc results.md -o results.pdf
```