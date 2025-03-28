module.exports = (req, res) => {
    if (req.method !== 'POST') {
        return res.status(405).json({ error: 'Method not allowed' });
    }

    const { user_name } = req.body;
    const name = user_name || 'Гость';
    res.status(200).json({ message: `Привет, ${name}! Спасибо за интерес к TG Мастер! Скоро с вами свяжутся.` });
};