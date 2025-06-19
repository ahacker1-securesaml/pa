#!/usr/bin/env python3
"""
Simple test for the issue processor.
"""

import unittest
import sys
import os

# Add the current directory to the path to import our module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from issue_processor import process_issue_data, display_issue
import io
from contextlib import redirect_stdout


class TestIssueProcessor(unittest.TestCase):
    
    def test_process_issue_data(self):
        """Test that issue data is processed correctly."""
        test_data = """
data:
- url: https://github.com/test/repo/issues/1
  state: "open"
  title: "Test Issue"
  number: 1
  author: testuser
  labels:
  - name: "bug"
"""
        
        issues = process_issue_data(test_data)
        
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0]['number'], 1)
        self.assertEqual(issues[0]['title'], "Test Issue")
        self.assertEqual(issues[0]['state'], "open")
        self.assertEqual(issues[0]['author'], "testuser")
        self.assertEqual(len(issues[0]['labels']), 1)
        self.assertEqual(issues[0]['labels'][0]['name'], "bug")
    
    def test_display_issue(self):
        """Test that issue display works correctly."""
        test_issue = {
            'number': 42,
            'title': 'Test Issue',
            'state': 'open',
            'author': 'testuser',
            'url': 'https://github.com/test/repo/issues/42',
            'labels': [{'name': 'bug'}, {'name': 'enhancement'}]
        }
        
        # Capture output
        f = io.StringIO()
        with redirect_stdout(f):
            display_issue(test_issue)
        
        output = f.getvalue()
        
        self.assertIn('Issue #42: Test Issue', output)
        self.assertIn('State: open', output)
        self.assertIn('Author: testuser', output)
        self.assertIn('Labels: bug, enhancement', output)
    
    def test_empty_data(self):
        """Test handling of empty data."""
        issues = process_issue_data("")
        self.assertEqual(issues, [])
    
    def test_invalid_yaml(self):
        """Test handling of invalid YAML."""
        issues = process_issue_data("invalid: yaml: [")
        self.assertEqual(issues, [])


if __name__ == '__main__':
    unittest.main()