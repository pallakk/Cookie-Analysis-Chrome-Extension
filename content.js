chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "getText") {
    const pageText = document.body.innerText;
    sendResponse({ text: pageText });
  }
});
