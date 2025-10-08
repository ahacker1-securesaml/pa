#!/usr/bin/env python3
"""
Simple issue data processor for the 'pa' project.
Processes issue data in the format specified in issue #22.
"""

import yaml
import sys
from typing import Dict, List, Any


def process_issue_data(data_text: str) -> List[Dict[str, Any]]:
    """
    Process issue data from YAML format.
    
    Args:
        data_text: YAML formatted issue data
        
    Returns:
        List of processed issue dictionaries
    """
    try:
        # Parse the YAML data
        parsed_data = yaml.safe_load(data_text)
        
        if isinstance(parsed_data, dict) and 'data' in parsed_data:
            return parsed_data['data']
        
        return []
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}", file=sys.stderr)
        return []


def display_issue(issue: Dict[str, Any]) -> None:
    """Display a single issue in a formatted way."""
    print(f"Issue #{issue.get('number', 'N/A')}: {issue.get('title', 'No title')}")
    print(f"  State: {issue.get('state', 'unknown')}")
    print(f"  Author: {issue.get('author', 'unknown')}")
    print(f"  URL: {issue.get('url', 'N/A')}")
    
    labels = issue.get('labels', [])
    if labels:
        label_names = [label.get('name', '') for label in labels if isinstance(label, dict)]
        print(f"  Labels: {', '.join(label_names)}")
    
    print()


def main():
    """Main function to demonstrate issue processing."""
    # Sample data from issue #22
    sample_data = """
data:
- url: https://github.com/Project-Testing-H1/Private-Repo/issues/21
  state: "open"
  draft: false
  title: "u"
  number: 21
  author: ahacker1-securesaml
  created_at: "2025-03-27T12:00:00Z"
  closed_at: "2025-03-27T12:00:00Z"
  labels:
  - name: "bug"
  - name: "good first issue"
"""
    
    print("PA Issue Processor")
    print("==================")
    print()
    
    issues = process_issue_data(sample_data)
    
    if issues:
        print(f"Processed {len(issues)} issue(s):")
        print()
        
        for issue in issues:
            display_issue(issue)
    else:
        print("No issues found or error processing data.")


if __name__ == "__main__":
    main()