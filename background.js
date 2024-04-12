chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.action === "addToBucket") {
    // Example of adding to a bucket (you will expand this with actual logic)
    console.log(`Adding ${sender.tab.url} to bucket ${request.bucket}`);
    // Here, you would handle the logic to save the URL to a file or storage
  }
});