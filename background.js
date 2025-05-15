chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.status === "complete" && tab.url.startsWith("http")) {
      const domain = new URL(tab.url).hostname;
      chrome.cookies.getAll({ domain }, (cookies) => {
        const cookieTexts = cookies.map(c => `${c.name}=${c.value}`);
        fetch("http://localhost:5000/analyze", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ cookies: cookieTexts })
        })
        .then(res => res.json())
        .then(data => {
          if (data.sensitive) {
            chrome.storage.local.set({ flagged: data });
            chrome.action.openPopup();
          }
        });
      });
    }
  });
  