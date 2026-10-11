from pathlib import Path
from markdown_it import MarkdownIt
import re,html
root=Path(__file__).resolve().parent
parser=MarkdownIt("commonmark",{"html":False,"linkify":True}).enable("table")
files={"cpp_pointers_references.md":"cpp-pointers-references.html","four_consecutive_squares.md":"four-consecutive-squares.html","odd_squares_mod8.md":"odd-squares-mod8.html","consecutive_integer_sums.md":"consecutive-integer-sums.html"}
for name,html_name in files.items():
 p=root/"content/blog"/name
 text=p.read_text()
 rendered=parser.render(text)
 rendered=re.sub(r'<pre><code class="language-mermaid">(.*?)</code></pre>',lambda m:'<div class="mermaid">'+html.unescape(m.group(1))+'</div>',rendered,flags=re.S)
 rendered=re.sub(r'^<h1>.*?</h1>\s*','',rendered,count=1,flags=re.S)
 rendered=re.sub(r'^<p><em>.*?</em></p>\s*','',rendered,count=1,flags=re.S)
 target=root/html_name
 page=target.read_text()
 start=page.index('<div class="article-copy markdown-body math-article">')+len('<div class="article-copy markdown-body math-article">')
 end=page.index('</div><div class="article-end">',start)
 target.write_text(page[:start]+rendered+page[end:])
 print("updated",html_name)
