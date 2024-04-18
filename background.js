// background.js
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    console.log("Received message from popup:", request);
    if (request.action === "addToBucket") {
        console.log(`Request to add URL to bucket: ${request.bucket}`);
        console.log(`URL to add: ${request.url}`);

        chrome.storage.local.get({buckets: {}}, function(data) {
            const updatedBuckets = data.buckets;
            console.log(`Current bucket data retrieved: `, updatedBuckets);

            if (!updatedBuckets[request.bucket]) {
                updatedBuckets[request.bucket] = [];
                console.log(`Created new bucket: ${request.bucket}`);
            }
            updatedBuckets[request.bucket].push(request.url);

            chrome.storage.local.set({buckets: updatedBuckets}, function() {
                if (chrome.runtime.lastError) {
                    console.error(`Error updating storage: ${chrome.runtime.lastError.message}`);
                } else {
                    console.log(`Added ${request.url} to ${request.bucket} successfully.`);
                    sendResponse({status: 'success'});
                }
            });
        });

        return true; // Indicates that the response will be sent asynchronously
    }
});
