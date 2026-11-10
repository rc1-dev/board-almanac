const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + __dirname + '/proposal.html');
  await p.pdf({ path: __dirname + '/almanac-round1-proposal.pdf', format: 'A4', printBackground: true, preferCSSPageSize: true });
  await b.close();
})();
