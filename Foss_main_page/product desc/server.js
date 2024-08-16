const express = require('express');
const Razorpay = require('razorpay');
const bodyParser = require('body-parser');
const cors = require('cors');
const app = express();

app.use(bodyParser.json());
app.use(cors());

const razorpay = new Razorpay({
    key_id: 'OWN_KEY',
    key_secret: 'OWN_KEY',
});



app.post('/create-order', async (req, res) => {
  const { amount, currency } = req.body;

  const options = {
    amount: amount*100, // amount in the smallest currency unit
    currency,
  };

  try {
    const order = await razorpay.orders.create(options);
    res.json(order);
  } catch (error) {
    console.error(error);
    res.status(500).send(error);
  }
});

app.listen(3000, () => console.log('Server running on port 3000'));
