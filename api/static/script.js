document.addEventListener('DOMContentLoaded', () => {
    const amountInput = document.getElementById('amount');
    const fromCurrencySelect = document.getElementById('fromCurrency');
    const toCurrencySelect = document.getElementById('toCurrency');
    const convertButton = document.getElementById('convertButton');
    const conversionResult = document.getElementById('conversionResult');
    const errorMessage = document.getElementById('errorMessage');

    // URL base do seu backend FastAPI
    const BACKEND_URL = 'http://localhost:8000'; 

    convertButton.addEventListener('click', async () => {
        const value = parseFloat(amountInput.value);
        const fromCurrency = fromCurrencySelect.value;
        const toCurrency = toCurrencySelect.value;

        // Limpa mensagens anteriores
        conversionResult.textContent = '--';
        errorMessage.textContent = '';

        if (isNaN(value) || value <= 0) {
            errorMessage.textContent = 'Por favor, insira um valor válido e positivo.';
            return;
        }

        try {
            const response = await fetch(`${BACKEND_URL}/single/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    value: value,
                    from_currency: fromCurrency,
                    to_currency: toCurrency
                })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || `Erro na API: ${response.status}`);
            }

            const data = await response.json();
            conversionResult.textContent = `${data.result.toFixed(2)} ${toCurrency}`;

        } catch (error) {
            console.error('Erro ao converter:', error);
            errorMessage.textContent = `Erro ao converter: ${error.message}`;
        }
    });
});