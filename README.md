# pa

A simple project automation tool for processing issue data.

## Overview

This project provides utilities for processing and displaying issue data in YAML format, as demonstrated in issue #22.

## Usage

Run the issue processor:

```bash
python3 issue_processor.py
```

This will process and display sample issue data in a formatted output.

## Data Format

The tool processes issue data in the following YAML format:

```yaml
data:
- url: https://github.com/example/repo/issues/1
  state: "open"
  draft: false
  title: "Issue title"
  number: 1
  author: username
  created_at: "2025-03-27T12:00:00Z"
  closed_at: "2025-03-27T12:00:00Z"
  labels:
  - name: "bug"
  - name: "good first issue"
```

## Requirements

- Python 3.6+
- PyYAML (for YAML parsing)

## Installation

```bash
pip install PyYAML
```