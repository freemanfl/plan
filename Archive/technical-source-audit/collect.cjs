const fs = require('fs');
const dir = __dirname;
(async () => {
  const paths = ['/about/','/contact/','/web-design/','/faq/','/blog/','/blog/best-of-whidbey-digital-marketing-and-web-design/','/robots.txt','/sitemap.xml','/assets/js/nav.js','/assets/js/dark.js'];
  await Promise.all(paths.map(async p => {
    const r = await fetch('https://oakharborwebdesigns.com'+p);
    const t = await r.text();
    const name = 'live-'+p.split('/').filter(Boolean).join('_');
    fs.writeFileSync(dir+'/'+name+(p.endsWith('/')?'.html':''),t);
    console.log(r.status,p,t.length);
  }));
  for(const name of fs.readdirSync(dir).filter(n=>n.endsWith('.html')&&!n.includes('readable'))){
    fs.writeFileSync(dir+'/'+name.replace('.html','-readable.html'),fs.readFileSync(dir+'/'+name,'utf8').replace(/></g,'>\n<'));
  }
})();
