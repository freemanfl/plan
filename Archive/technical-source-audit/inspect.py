from pathlib import Path
from html.parser import HTMLParser
from collections import Counter, defaultdict
import json
root=Path(__file__).parent
class Scan(HTMLParser):
 def __init__(self):
  super().__init__(); self.tags=Counter(); self.attrs=defaultdict(set); self.elements=[]
 def handle_starttag(self,tag,attrs):
  self.tags[tag]+=1; self.attrs[tag].update(k for k,v in attrs); self.elements.append((self.getpos()[0],tag,dict(attrs)))
summaries={}
for file in sorted(root.glob('live-*-readable.html')):
 s=Scan(); s.feed(file.read_text(encoding='utf8'))
 summaries[file.name]={'tags':dict(s.tags),'attributes':{k:sorted(v) for k,v in s.attrs.items()},'missingImageAlt':[n for n,t,a in s.elements if t=='img' and 'alt' not in a], 'missingImageDimensions':[n for n,t,a in s.elements if t=='img' and not('width' in a and 'height' in a)],'duplicateIds':{k:v for k,v in Counter(a['id'] for n,t,a in s.elements if 'id' in a).items() if v>1}}
(root/'inventory.json').write_text(json.dumps(summaries,indent=2),encoding='utf8')
seen=set(); output=[]
for file in sorted(root.glob('live-*-readable.html')):
 output.append('\nFILE '+file.name)
 for i,line in enumerate(file.read_text(encoding='utf8').splitlines(),1):
  if line not in seen:
   seen.add(line); output.append(f'{i}: {line}')
(root/'live-unique-lines.txt').write_text('\n'.join(output),encoding='utf8')
print('Unique lines:',len(output));print(json.dumps({k:{a:v for a,v in x.items() if a!='attributes'} for k,x in summaries.items()},indent=2))
