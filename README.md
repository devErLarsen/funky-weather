# funky-weather

check out the previous tasks by using git checkout '[tag-name]'

ex.
```
git checkout 1.0
```

and return to latest version
```
git checkout main
```

## Running the Project

This guide will walk you through setting up and running this Python project on your local machine, with instructions for both Git and direct download methods.
Prerequisites

Before you begin, ensure you have the following installed on your system:

    Python 3.6 or higher
    pip (Python package installer)

### Setup
#### Option 1: Using Git (Recommended)

  Clone the Repository

  Open your terminal or command prompt, navigate to the directory where you want to clone the repository, and run:

  ```sh
  git clone https://github.com/deverlarsen/funky-weather.git
  ```

#### Option 2: Direct Download

Download the Project ZIP
    Navigate to the project's GitHub page.
    Click the green Code button, then select Download ZIP.
    Once the download is complete, extract the ZIP file to your desired location.

### Continue with Project Setup

Navigate to the Project Directory

Change your current directory to the project's directory:

```sh
cd funky-weather
```

### Create a Virtual Environment

Create a virtual environment in the project directory by running:

```sh
python -m venv venv
```
Activate the Virtual Environment

On Windows:

```cmd
.\venv\Scripts\activate
```
On macOS and Linux:

```sh
source venv/bin/activate
```
### Install Dependencies

With the virtual environment activated, install the project's dependencies using pip:

```sh
pip install -r requirements.txt
```
### Running the Project

With the setup complete, you can now run the project:

```sh
python main.py
```
### Deactivating the Virtual Environment

To deactivate the virtual environment and return to your system's default Python interpreter, run:

```sh
deactivate
```

Weather data from MET norway
