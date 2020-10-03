/* 
Implements clipboard.js API to allow the user to copy their created URL to 
the clipboard. The function below is linked to the "COPY LINK" button located 
on the "your_url.html" file.
 */
var clipboard = new ClipboardJS('.copy-button');

clipboard.on('success', function(e) {
    console.log(e);
});

clipboard.on('error', function(e) {
    console.log(e);
});