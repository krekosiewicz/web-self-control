document.getElementById('addBucketOne').addEventListener('click', function() {
  chrome.runtime.sendMessage({action: "addToBucket", bucket: 1});
});

// Repeat for other buttons/buckets


// In your background.js or options.js
// function addToBucket(url, bucketNumber) {
//   // Example: Load, update, and save the bucket list
//   chrome.storage.local.get({buckets: {}}, function(data) {
//     if (!data.buckets[bucketNumber]) data.buckets[bucketNumber] = [];
//     data.buckets[bucketNumber].push(url);
//     chrome.storage.local.set({buckets: data.buckets});
//   });
// }