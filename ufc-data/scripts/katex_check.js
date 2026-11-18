// Check a JSON list of LaTeX strings with KaTeX; prints a JSON list of 1/0 (parses or not).
// Needs: npm install katex
const katex = require('katex');
const items = JSON.parse(require('fs').readFileSync(process.argv[2], 'utf8'));
console.log(JSON.stringify(items.map(s => { try { katex.renderToString(s, {throwOnError: true, displayMode: true}); return 1; } catch (e) { return 0; } })));
