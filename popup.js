// Get the current active tab and then send a message to the background page
function sendMessageToBackground(bucketName) {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        const tab = tabs[0];
        chrome.runtime.sendMessage({
            action: "addToBucket",
            bucket: bucketName,
            url: tab.url  // Sending the URL directly from here
        });
    });
}

document.getElementById('addBucketOne').addEventListener('click', function() {
    sendMessageToBackground("Bucket One");
});

document.getElementById('addBucketTwo').addEventListener('click', function() {
    sendMessageToBackground("Bucket Two");
});

document.getElementById('addBucketThree').addEventListener('click', function() {
    sendMessageToBackground("Bucket Three");
});
