document.getElementById('scanButton').addEventListener('click', async () => {
  let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    function: scanPage,
  });
});

function scanPage() {
  const keywords = ["age", "height", "disease", "username", "credit card number", "password", "account number", "phone number", "login"];
  const pageText = document.body.innerText.toLowerCase();
  const found = keywords.filter(word => pageText.includes(word));

  alert(found.length > 0 
    ? `Found sensitive health terms: ${found.join(', ')}`
    : 'No sensitive health terms detected.');
}
