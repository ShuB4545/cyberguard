
// Adds an extra button that sends the same analysis to the backend API and uses the existing displayAnalysisResults UI.
(function () {
  function formatTime(seconds) {
    if (seconds < 60) return `${seconds.toFixed(1)} seconds`;
    if (seconds < 3600) return `${(seconds / 60).toFixed(1)} minutes`;
    if (seconds < 86400) return `${(seconds / 3600).toFixed(1)} hours`;
    if (seconds < 31536000) return `${(seconds / 86400).toFixed(1)} days`;
    if (seconds < 31536000000) return `${(seconds / 31536000).toFixed(1)} years`;
    return `${(seconds / 31536000000).toFixed(1)} centuries`;
  }

  function addApiButton() {
    const analyzeBtn = document.getElementById('analyzeBtn');
    if (!analyzeBtn) return;

    const apiBtn = document.createElement('button');
    apiBtn.id = 'analyzeApiBtn';
    apiBtn.className = 'w-full bg-gradient-to-r from-purple-500 to-blue-500 hover:from-purple-600 hover:to-blue-600 py-4 rounded-lg font-medium transition-all transform hover:scale-105 mt-3';
    apiBtn.innerHTML = '<i class="fas fa-cloud mr-2"></i>Analyze (API)';

    analyzeBtn.parentNode.appendChild(apiBtn);

    apiBtn.addEventListener('click', async () => {
      const password = document.getElementById('passwordInput').value;
      const method = document.getElementById('attackMethod').value;
      const hardware = document.getElementById('hardwareConfig').value;

      if (!password) {
        alert('Please enter a password to analyze');
        return;
      }

      try {
        const resp = await fetch('http://127.0.0.1:8000/api/analyze', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            password,
            attack_method: method,
            hardware_config: hardware
          })
        });
        const data = await resp.json();

        // Build an object compatible with the existing displayAnalysisResults function
        const analysis = {
          score: data.score,
          entropy: data.entropy,
          characterSpace: data.character_space,
          combinations: data.combinations
        };

        // If backend returns "crack_time" as text, pass it through; otherwise format seconds
        const crackTime = (typeof data.crack_time === 'string') ? data.crack_time :
                          (typeof data.crack_time_seconds === 'number') ? formatTime(data.crack_time_seconds) : '—';

        displayAnalysisResults(password, analysis, crackTime);
      } catch (e) {
        alert('API call failed. Is the FastAPI server running on http://127.0.0.1:8000 ?');
        console.error(e);
      }
    });
  }

  document.addEventListener('DOMContentLoaded', addApiButton);
})();
