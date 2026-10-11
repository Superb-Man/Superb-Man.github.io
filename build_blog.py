from pathlib import Path
import html,re
from markdown_it import MarkdownIt

root=Path(__file__).resolve().parent
src=root/'content/blog/timer_dispatcher_full_original.md'
md=src.read_text(encoding='utf-8')
parser=MarkdownIt('commonmark', {'html':False, 'linkify':True}).enable('table')
rendered=parser.render(md)
rendered=re.sub(r'<pre><code class="language-mermaid">(.*?)</code></pre>',lambda m:'<div class="mermaid">'+html.unescape(m.group(1))+'</div>',rendered,flags=re.S)
rendered=re.sub(r'^<h1>.*?</h1>\s*','',rendered,count=1,flags=re.S)
# Sidebar TOC sourced directly from article headings.
headings=re.findall(r'^## (.+)$',md,re.M)
toc=''.join('<li><a href="#section-'+str(i)+'">'+html.escape(h)+'</a></li>' for i,h in enumerate(headings,1))
for i,h in enumerate(headings,1):
    rendered=rendered.replace('<h2>'+html.escape(h)+'</h2>','<h2 id="section-'+str(i)+'">'+html.escape(h)+'</h2>',1)
nav='<header class="site-header"><div class="container nav-inner"><a class="wordmark" href="./index.html">Kazi Istiak Toriqe</a><nav><a href="./index.html">About</a><a href="./index.html#research">Research</a><a href="./index.html#projects">Projects</a><a href="./blog.html">Blog</a><a href="./index.html#contact">Contact</a></nav></div></header>'
content=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="A complete technical walkthrough of a Unix-style C++ timer dispatcher"><title>One Alarm Clock, Many Jobs | Kazi Istiak Toriqe</title><link rel="stylesheet" href="./assets/css/style.css"></head><body>{nav}<main class="container article-layout"><aside class="article-side"><a class="minor-link" href="./blog.html">← All posts</a><div class="side-label">Systems / C++</div><p>Timers · Concurrency · Scheduling</p><details class="article-toc"><summary>In this article ({len(headings)} sections)</summary><ol>{toc}</ol></details><a class="side-link" href="./content/blog/timer_dispatcher_full_original.md">Original Markdown ↗</a></aside><article class="article-paper"><p class="eyebrow">ENGINEERING NOTES · C++ / UNIX</p><h1>One Alarm Clock,<br><em>Many Jobs.</em></h1><p class="article-lead">Building a Simple Timer Dispatcher in C++ · The complete technical walkthrough</p><div class="article-divider"></div><div class="article-copy markdown-body">{rendered}</div><div class="article-end">End of article · <a href="./blog.html">More writing</a></div></article></main><footer class="container footer"><span>© 2026 Kazi Istiak Toriqe</span><a href="./blog.html">← All writing</a></footer><script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script><script>if(window.mermaid){{mermaid.initialize({{startOnLoad:true,theme:'neutral',securityLevel:'strict'}});}}</script></body></html>'''
(root/'timer-dispatcher.html').write_text(content,encoding='utf-8')
print('Generated complete article:',len(headings),'sections',len(content),'bytes')
