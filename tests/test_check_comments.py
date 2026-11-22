import unittest

from scripts.check_comments import comment_lines


class CommentLintTest(unittest.TestCase):
    def test_python_shebang_and_string(self):
        self.assertEqual(comment_lines('#!/usr/bin/env python3\nx = "https://x/#part"\n# old', '.py'), [3])

    def test_python_inline_comment(self):
        self.assertEqual(comment_lines('x = 1  # old\n', '.py'), [1])

    def test_shell_shebang_string_and_comment(self):
        self.assertEqual(comment_lines('#!/bin/sh\nprintf "%s" "# literal"\n# old\n', '.sh'), [3])

    def test_html_with_embedded_code(self):
        source = '<!DOCTYPE html>\n<style>a{content:"/* literal */"}/* old */</style>\n<script>const url="https://x"; // old\n</script>'
        self.assertEqual(comment_lines(source, '.html'), [2, 3])

    def test_yaml_string_and_comment(self):
        self.assertEqual(comment_lines('name: "# literal"\nvalue: yes # old\n', '.yaml'), [2])


if __name__ == "__main__":
    unittest.main()
