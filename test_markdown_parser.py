import pytest
from markdown_parser import parse_markdown, apply_bold, apply_italic, apply_monospace

def test_parse_markdown():
    markdown_text = """This is a paragraph with **bold text** and _italic text_.
    
This is another paragraph with `monospace text`.

Code block
with multiple lines
"""
    expected_html = """<p>This is a paragraph with <b>bold text</b> and <i>italic text</i>. </p>
<p>This is another paragraph with <tt>monospace text</tt>. </p>
<pre>
Code block
with multiple lines
</pre>
"""
    assert parse_markdown(markdown_text) == expected_html

def test_apply_bold():
    assert apply_bold("This is **bold** text.") == "This is <b>bold</b> text."

def test_apply_italic():
    assert apply_italic("This is _italic_ text.") == "This is <i>italic</i> text."


def test_apply_monospace():
    assert apply_monospace("This is `monospace` text.") == "This is <tt>monospace</tt> text."
