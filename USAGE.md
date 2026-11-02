# Smart Downloads Organizer – Usage Guide

## Overview

A Python command-line tool that automatically organizes files into categories using their extensions.

## Installation

```bash
pip install -r requirements.txt
```

## Basic Usage

```bash
python main.py
```

## Example 1: Preview file organization

```bash
python main.py --source downloads --target organized --dry-run
```

## Example 2: Organize files automatically

```bash
python main.py --source downloads --target organized
```

## Example 3: Verbose mode

```bash
python main.py --source downloads --target organized --verbose
```

## Configuration

Edit `config.yaml` to change default folders, categories, and logging level.

## Help

```bash
python main.py --help
```

## Safety

Use `--dry-run` to preview file movements before actual execution.