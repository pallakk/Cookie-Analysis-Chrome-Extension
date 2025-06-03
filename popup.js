document.getElementById("scanBtn").addEventListener("click", () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.tabs.sendMessage(
      tabs[0].id,
      { action: "getText" },
      (response) => {
        fetch("http://localhost:5000/scan", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ text: response.text }),
        })
          .then(res => res.json())
          .then(data => {
            const resultDiv = document.getElementById("result");
            resultDiv.innerHTML = `
              <div class='score'>Credibility Score: ${data.credibility_score}</div>
              <div>Matches: <ul>${data.matches.map(term => `<li>${term}</li>`).join("")}</ul></div>
            `;
          });
      }
    );
  });
});
