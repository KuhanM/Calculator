document.getElementById('calc-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const formData = new FormData(this);
    
    try {
        const response = await fetch('/calculate', {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        const resultDiv = document.getElementById('result');
        if (response.ok) {
            resultDiv.textContent = `Result: ${data.result}`;
            resultDiv.style.color = '#333';
        } else {
            resultDiv.textContent = `Error: ${data.error}`;
            resultDiv.style.color = 'red';
        }
    } catch (error) {
        document.getElementById('result').textContent = 'Error: Something went wrong';
        document.getElementById('result').style.color = 'red';
    }
});