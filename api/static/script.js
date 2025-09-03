document.addEventListener('DOMContentLoaded', () => {
    const amountInput = document.getElementById('amount');
    const fromCurrencySelect = document.getElementById('fromCurrency');
    const toCurrencySelect = document.getElementById('toCurrency');
    const convertButton = document.getElementById('convertButton');
    const conversionResult = document.getElementById('conversionResult');
    const errorMessage = document.getElementById('errorMessage');

    // REMOVEMOS A URL FIXA PARA 'localhost'

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
            // CORREÇÃO AQUI: Usamos um caminho relativo. 
            // O navegador chamará 'https://seu-site.onrender.com/single/' automaticamente.
            const response = await fetch(`/single/`, {
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
                // Tenta ler a resposta de erro como JSON, se falhar, usa o texto do status
                let errorMsg = `Erro na API: ${response.status} ${response.statusText}`;
                try {
                    const errorData = await response.json();
                    errorMsg = errorData.detail || errorMsg;
                } catch (e) {
                    // Ignora o erro de parsing do JSON se a resposta de erro não for JSON
                }
                throw new Error(errorMsg);
            }

            const data = await response.json();
            // A resposta já é o JSON correto, não precisa de .model_dump() aqui
            conversionResult.textContent = `${data.result.toFixed(2)} ${toCurrency}`;

        } catch (error) {
            console.error('Erro ao converter:', error);
            // Mostra a mensagem de erro que vem da API ou do fetch
            errorMessage.textContent = `${error.message}`;
        }
    });
});