var elementos = document.querySelectorAll('.player-options div > img');
var playerOpt = '';
var inimigoOpt = '';

function validarVitoria(){
    let resultado = document.querySelector('.resultado');
    
    if (playerOpt=='Paper'){
        if (inimigoOpt == 'Paper'){
            resultado.style.color = 'black';
            resultado.innerHTML = 'Empate!';
        }
        else if (inimigoOpt == 'Scissor'){
            resultado.style.color = 'Red';
            resultado.innerHTML = 'Derrota!';
        }
        else if (inimigoOpt == 'Rock'){
            resultado.style.color = 'Green';
            resultado.innerHTML = 'Vitória!';
        }
    }
    else if (playerOpt=='Scissor'){
        if (inimigoOpt == 'Paper'){
            resultado.style.color = 'Green';
            resultado.innerHTML = 'Vitória!';
        }
        else if (inimigoOpt == 'Scissor'){
            resultado.style.color = 'black';
            resultado.innerHTML = 'Empate!';
        }
        else if (inimigoOpt == 'Rock'){
            resultado.style.color = 'Red';
            resultado.innerHTML = 'Derrota!';
        }
    }
    else if (playerOpt=='Rock'){
        if (inimigoOpt == 'Paper'){
            resultado.style.color = 'Red';
            resultado.innerHTML = 'Derrota!';
        }
        else if (inimigoOpt == 'Scissor'){
            resultado.style.color = 'Green';
            resultado.innerHTML = 'Vitória!';
        }
        else if (inimigoOpt == 'Rock'){
            resultado.style.color = 'black';
            resultado.innerHTML = 'Empate!';
        }
    }
}

function resetOpacityPlayer(){
    for(var i = 0; i < elementos.length;i++){

       elementos[i].style.opacity = '0.3';

    }
}

function resetInimigo(){
    const enemyOptions = document.querySelectorAll('.enemy-options div');
    for(var i = 0; i < enemyOptions.length; i++){
            enemyOptions[i].childNodes[0].style.opacity = '0.3';
    }
}

function inimigoJogar(){
    let rand = Math.floor(Math.random()*3);

    const enemyOptions = document.querySelectorAll('.enemy-options div');
    resetInimigo();

    for(var i = 0; i < enemyOptions.length; i++){
        if(i == rand){
            enemyOptions[i].childNodes[0].style.opacity = '1';
            inimigoOpt = enemyOptions[i].childNodes[0].getAttribute('opt');
        }
    }

    validarVitoria();


    //alert(playerOpt);
    //alert(inimigoOpt);
}

for(var i = 0; i < elementos.length;i++){

    elementos[i].addEventListener('click',(t)=>{
        resetOpacityPlayer();
        t.target.style.opacity = '1';
        playerOpt = t.target.getAttribute('opt');

        inimigoJogar();

        
    });
}