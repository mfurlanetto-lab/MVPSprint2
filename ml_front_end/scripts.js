function validarAno(ano) {
    // Expressão regular para um ano de 4 dígitos
    var regexAno = /^\d{4}$/;

    // Testa se a string atende à expressão regular
    return regexAno.test(ano);
}


const realizarPrevisao = () => {

    document.getElementById('leaveOrNot').innerText = "";

    console.log('Início Realizar previsão...');

    let inputEducation = document.getElementById("education").value;
    let inputJoiningYear = document.getElementById("joiningYear").value;
    let inputPaymentTier = document.getElementById("paymentTier").value;
    let inputAge = document.getElementById("age").value;
    let inputGender = document.getElementById("gender").value;
    let inputEverBenched = document.getElementById("everBenched").value;
    let inputExperienceInCurrentDomain = document.getElementById("experienceInCurrentDomain").value;

    if (inputEducation == '' || inputJoiningYear == '' || inputPaymentTier == '' || inputAge == '' || inputGender == '' || inputEverBenched == '' || inputExperienceInCurrentDomain == '') {
        alert('Informações não preenchidas. Verifique!');
        return;
    }

    if (validarAno(inputJoiningYear) == false) {
        alert('Ano de admissão inválido. Verifique!');
        return;
    }

    if (inputAge < 16) {
        alert('Idade inválida para um empregado. Verifique!');
        return;
    }

    const formData = new FormData();
    formData.append('education', inputEducation);
    formData.append('joiningYear', inputJoiningYear);
    formData.append('paymentTier', inputPaymentTier);
    formData.append('age', inputAge);
    formData.append('gender', inputGender);
    formData.append('everBenched', inputEverBenched);
    formData.append('experienceInCurrentDomain', inputExperienceInCurrentDomain);


    console.log('Fetch...');
    let url = 'http://127.0.0.1:5000/prever';

    // Enviar dados para o servidor
    fetch(url, {
        method: 'POST',
        body: formData
    })
        .then(response => {
            console.log('Resposta do servidor...:', response);
            return response.json();
        })
        .then(data => {
            console.log('Dados recebidos...:', data);
            // Exibir o resultado no elemento desejado
            if (data.resultado == "1") {
                document.getElementById('leaveOrNot').innerText = "Deixará o emprego (positivo)";
                document.getElementById('leaveOrNot').style.color = "red";
            }
            else {
                document.getElementById('leaveOrNot').innerText = "Não deixará o emprego (negativo)";
                document.getElementById('leaveOrNot').style.color = "green";
            }
        })
        .catch(error => {
            console.error('Erro:', error);
            console.log('Error status:', error.status);
            console.log('Error message:', error.message);
        });

    console.log('Fim Realizar previsão...');

}
