document.getElementById('CreateUserForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;
    const senha = document.getElementById('senha').value;
    const longitude = document.getElementById('longitude').value;
    const latitude = document.getElementById('latitude').value;

    const formData = new URLSearchParams();
    formData.append('nome', nome);
    formData.append('email', email);
    formData.append('senha', senha);
    formData.append('longitude', longitude);
    formData.append('latitude', latitude);

    try {
        const response = await fetch('http://127.0.0.1:8081/api/createuser', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();
        document.getElementById('response').textContent =
            JSON.stringify(result, null, 2);

    } catch (error) {
        console.error('Erro:', error);
        document.getElementById('response').textContent =
            'Erro ao enviar os dados';
    }
});
