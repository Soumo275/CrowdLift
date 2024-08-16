
document.getElementById('rzp-button').onclick = async function (e) {
  e.preventDefault();
  try {
    const response = await fetch('http://localhost:3000/create-order', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ amount: document.getElementById("amt").value, currency: 'INR' })
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const order = await response.json();
    console.log('Order created:', order);

    const options = {
      "key": "OWN_KEY",
      "amount": order.amount,
      "currency": order.currency,
      "name": "Soumyadip",
      "description": "Test Transaction",
      "order_id": order.id,
      "handler": function (response) {
        alert(`Payment successful! Payment ID: ${response.razorpay_payment_id} and amount : ${document.getElementById("amt").value}`);
        increaseValue(document.getElementById("amt").value);
      },
      "prefill": {
        "name": "Customer Name",
        "email": "customer@example.com",
        "contact": "9999999999"
      },
      "theme": {
        "color": "#3399cc"
      }
    };

    const rzp1 = new Razorpay(options);
    rzp1.on('payment.failed', function (response){
      alert(`Payment failed: ${response.error.description}`);
    });

    rzp1.open();
  } catch (error) {
    console.error('Error:', error);
  }
}

  let currentValue = 0;
  const maxValue = 1000; // Adjust this to set the maximum value of the bar

  function increaseValue(amt) {
      if (currentValue < maxValue) {

          currentValue += amt; // Adjust this to change the amount added
          const fillElement = document.getElementById('fill');
          const valueElement = document.getElementById('current-value');
          const percentage = (currentValue / maxValue) * 100;

          fillElement.style.width = percentage + '%';
          valueElement.textContent = currentValue;
      }
  }
