const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
app.use(bodyParser.json());
app.use(cors());

app.get('/bfhl', (req, res) => {
    res.status(200).json({ operation_code: 1 });
});

app.post('/bfhl', (req, res) => {
    const { data } = req.body;
    const userId = "rameez_baig";
    const email = "rameezbaig.m2021@vitstudent.ac.in";
    const rollNumber = "21BCT0214";
    
    const numbers = data.filter(item => !isNaN(item));
    const alphabets = data.filter(item => isNaN(item));
    const highestLowercaseAlphabet = alphabets
        .filter(char => char === char.toLowerCase())
        .sort().reverse()[0] || null;

    res.json({
        is_success: true,
        user_id: userId,
        email: email,
        roll_number: rollNumber,
        numbers,
        alphabets,
        highest_lowercase_alphabet: highestLowercaseAlphabet ? [highestLowercaseAlphabet] : []
    });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
