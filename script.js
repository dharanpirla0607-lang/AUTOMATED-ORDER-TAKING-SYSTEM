<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Smart Canteen – Please Wait</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/static/style.css">
</head>
<body class="status-page">

  <div class="status-wrapper">
    <div class="status-card" id="waitingCard">
      <div class="status-icon" style="animation:pulse 1.2s ease-in-out infinite">⏳</div>
      <h1 class="status-title">Canteen is Full!</h1>
      <p class="status-sub">
        Hi <strong>{{ name }}</strong>, all 10 order slots are currently occupied.<br><br>
        Your order is saved. We are automatically waiting for a slot to free up and will place your order the moment one becomes available.
      </p>

      <div class="waiting-dots">
        <span></span><span></span><span></span>
      </div>

      <div class="waiting-status-box">
        <div class="waiting-status-label">Status</div>
        <div class="waiting-status-val" id="statusMsg">Checking for a free slot…</div>
        <div class="waiting-attempt-label">Attempts: <span id="attemptCount">0</span></div>
      </div>
    </div>

    <!-- Shown once a slot is found -->
    <div class="status-card hidden" id="successCard">
      <div class="status-icon success-anim">🎉</div>
      <h1 class="status-title">Slot Found!</h1>
      <p class="status-sub">Your order has been placed.<br>Redirecting you now…</p>
    </div>
  </div>

  <div class="dev-credit">Developed by CS KARTHIK AND DHARAN</div>

  <script>
    let attempts = 0;
    let polling  = null;

    async function tryClaimToken() {
      attempts++;
      document.getElementById('attemptCount').textContent = attempts;
      document.getElementById('statusMsg').textContent =
        'Checking for a free slot… (attempt ' + attempts + ')';

      try {
        const res  = await fetch('/claim_token', { method: 'POST' });
        const data = await res.json();

        if (data.success) {
          // Got a token!
          clearInterval(polling);
          document.getElementById('waitingCard').classList.add('hidden');
          document.getElementById('successCard').classList.remove('hidden');
          setTimeout(() => { window.location.href = '/order_status'; }, 1500);

        } else if (data.still_waiting) {
          const occupied = data.active || 10;
          document.getElementById('statusMsg').textContent =
            'All ' + occupied + '/10 slots still busy. Retrying in 3 s…';

        } else {
          // Session expired or other error
          clearInterval(polling);
          alert(data.message || 'Something went wrong. Please start again.');
          window.location.href = '/';
        }
      } catch (e) {
        document.getElementById('statusMsg').textContent = 'Network error. Retrying…';
      }
    }

    // First attempt after 1 s, then every 3 s
    setTimeout(() => {
      tryClaimToken();
      polling = setInterval(tryClaimToken, 3000);
    }, 1000);
  </script>

</body>
</html>
