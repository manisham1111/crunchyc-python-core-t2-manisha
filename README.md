\# Smart Downloads Folder Organizer



A modular Python CLI tool that automatically organizes files into categories using file extensions.



\## Features

\- Modular Python architecture

\- CLI using argparse

\- YAML configuration

\- Dry-run support

\- Logging and custom exceptions

\- Automatic file categorization

\- Duplicate file protection



\## Installation



```cmd

git clone https://github.com/manisham1111/crunchyc-python-core-t2-manisha.git

cd crunchyc-python-core-t2-manisha

python -m venv .venv

.venv\\Scripts\\activate

pip install -r requirements.txt

```



\## Usage



\### Preview files

```cmd

python main.py --source test\_downloads --target test\_output --dry-run

```



\### Organize files

```cmd

python main.py --source test\_downloads --target test\_output

```



\### Verbose mode

```cmd

python main.py --source test\_downloads --target test\_output --verbose

```



\### Help

```cmd

python main.py --help

```



\## Configuration



Edit `config.yaml` to customize folders, categories, and logging.



\## Detailed Usage



See \[USAGE.md](USAGE.md).



\## Author

Manisha M

