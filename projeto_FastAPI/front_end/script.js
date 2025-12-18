// Seleciona o botão "Voltar ao Topo"
const botaoVoltarTopo = document.getElementById("voltar-topo");

// Adiciona um evento de rolagem na janela
window.onscroll = function() {
    // Se o usuário rolou mais de 100px para baixo
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        // Mostra o botão
        botaoVoltarTopo.style.display = "block";
    } else {
        // Esconde o botão
        botaoVoltarTopo.style.display = "none";
    }
};

// Validação do Formulário de Registro
const form = document.getElementById('register-form');
const nomeInput = document.getElementById('nome');
const emailInput = document.getElementById('email');
const senhaInput = document.getElementById('senha');

const nomeError = document.getElementById('nome-error');
const emailError = document.getElementById('email-error');
const senhaError = document.getElementById('senha-error');

// Adiciona validação em tempo real (ao sair do campo)
nomeInput.addEventListener('blur', validateNome);
emailInput.addEventListener('blur', validateEmail);
senhaInput.addEventListener('blur', validateSenha);

form.addEventListener('submit', async function(event) {
    // Previne o envio do formulário para realizar a validação
    event.preventDefault();

    // Roda todas as validações antes de tentar enviar
    const isNomeValid = validateNome();
    const isEmailValid = validateEmail();
    const isSenhaValid = validateSenha();

    if (isNomeValid && isEmailValid && isSenhaValid) {

        const submitButton = form.querySelector('button[type="submit"]');
        const originalButtonText = submitButton.textContent;
        submitButton.disabled = true;
        submitButton.textContent = 'Criando conta...';

        const formData = {
            nome: nomeInput.value,
            email: emailInput.value,
            senha: senhaInput.value
        };

        try {
            // Para desenvolvimento local, use a URL completa do seu backend
            const response = await fetch('http://127.0.0.1:8000/auth/criar_conta', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            });

            const data = await response.json();

            if (response.status === 200) { // 200 OK (ou 201 Created, dependendo do seu backend)
                alert(data.mensagem || 'Usuário criado com sucesso!');
                form.reset(); // Limpa o formulário
                // Limpa as classes de erro após o envio bem-sucedido
                nomeInput.classList.remove('invalid');
                emailInput.classList.remove('invalid');
                senhaInput.classList.remove('invalid');
            } else if (response.status === 400) { // Erro de validação (ex: e-mail já existe)
                alert(data.detail || 'Erro ao criar usuário. Verifique os dados.');
            } else {
                alert('Ocorreu um erro inesperado no servidor. Tente novamente.');
            }
        } catch (error) {
            console.error('Erro na requisição:', error);
            alert('Não foi possível conectar ao servidor. Verifique sua conexão e tente novamente.');
        } finally {
            // Restaura o botão ao estado original, independentemente do resultado
            submitButton.disabled = false;
            submitButton.textContent = originalButtonText;
        }
    }
});

function validateNome() {
    if (nomeInput.value.trim() === '') {
        nomeError.textContent = 'O campo nome é obrigatório.';
        nomeInput.classList.add('invalid');
        return false;
    }
    nomeError.textContent = '';
    nomeInput.classList.remove('invalid');
    return true;
}

function validateEmail() {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (emailInput.value.trim() === '' || !emailRegex.test(emailInput.value)) {
        emailError.textContent = 'Por favor, insira um e-mail válido.';
        emailInput.classList.add('invalid');
        return false;
    }
    emailError.textContent = '';
    emailInput.classList.remove('invalid');
    return true;
}

function validateSenha() {
    if (senhaInput.value.trim().length < 6) {
        senhaError.textContent = 'A senha deve ter pelo menos 6 caracteres.';
        senhaInput.classList.add('invalid');
        return false;
    }
    senhaError.textContent = '';
    senhaInput.classList.remove('invalid');
    return true;
}