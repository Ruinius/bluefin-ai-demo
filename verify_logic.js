const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

// Quick check if the JS handles Product UI fade out correctly
if (html.includes('if (pClosing1 >= 0 || pPreview > 0.85)')) {
    console.log("Check 1: Found the UI fade out logic");
} else {
    console.log("Check 1: Failed to find UI fade out logic");
}

if (html.includes('msg1.style.opacity = o;')) {
    console.log("Check 2: Found msg1 opacity logic");
}
