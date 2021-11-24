<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="./assets/js/jquery-3.6.0.min.js"></script>
    <script src="./assets/js/index.js"></script>
    
    <link rel="stylesheet" href="assets/style.css">
    
</head>
<body>
    <div class="sect">
        <h2>Video:</h2>
        <div class="divis">
            <div>
                <input id="vid_link" type="text" placeholder="insira um link">
                <input id="vid_open" type="button" value="Abrir link">
            </div>
            <div>
                <select id="vid_pred">
                    <option value="">Selecione um predefinido</option>
                    <option value="https://www.youtube.com/watch?v=xyqJJbaMsZ4">Dale Ramon</option>
                    <option value="https://www.youtube.com/watch?v=dQw4w9WgXcQ">Rickrolling</option>
                </select>
            </div>
        </div>
        <div>
            <input type="button" id="vid_play" value="Play/Pause">
            <input type="button" id="vid_begining" value="Voltar p/ comeco">
        </div>
        <div>
            <input type="button" id="vid_fullscreen" value="Tela cheia">
            <input type="button" id="vid_esc" value="Esc">
            <input type="button" id="vid_f5" value="Recarregar">
        </div>
        <div>
            <input type="button" id="vid_ekbf" value="Esc + Pause + tela cheia + comeco">
        </div>
        <div>
            <input type="button" id="vid_volDown" value="Diminuir volume">
            <input type="button" id="vid_volUp" value="Aumentar volume">
        </div>
        <div>
            <input type="button" id="vid_go0" value="0">
            <input type="button" id="vid_go1" value="1">
            <input type="button" id="vid_go2" value="2">
            <input type="button" id="vid_go3" value="3">
            <input type="button" id="vid_go4" value="4">
            <input type="button" id="vid_go5" value="5">
            <input type="button" id="vid_go6" value="6">
            <input type="button" id="vid_go7" value="7">
            <input type="button" id="vid_go8" value="8">
            <input type="button" id="vid_go9" value="9">
        </div>
        <div class="divis">
            <div>Avançar video:</div>
            <input type="button" id="vid_back" value="-5s">
            <input type="button" id="vid_forward" value="+5s">
            <input type="number" id="vid_temp" value="5" step="5" min="5">
        </div>
    </div>

    <div class="sect">
        <h2>Guias navegador:</h2>
        
        <div>
            <input type="button" id="vid_newchrome" value="Novo chrome">
            <input type="button" id="vid_altf4" value="Fechar programa">
        </div>
        <div class="divis">
            <div>
                <input type="button" id="vid_newtab" value="Nova guia">
                <input type="button" id="vid_closetab" value="Fechar guia">
            </div>
            <div>
                <input type="button" id="vid_prevtab" value="Guia anterior">
                <input type="button" id="vid_nexttab" value="Próxima guia">
            </div>
        </div>
    </div>

    <div class="sect">
        <h2>Volume sistema:</h2>
        <div class="divis">
            <p>volume geral:</p>
            <div>
                <input id="vol_globalvalval" min="-96" max="0" type="range">
                <input id="vol_globalvalbtn" type="button" value="Ok">
            </div>
            <div>
                <input id="vol_globalMax" type="button" value="Maximo">
                <input id="vol_globalMin" type="button" value="Minimo">
            </div>
            <div>
                <input id="vol_globalMaxF" type="button" value="Maximo opc2">
                <input id="vol_globalMinF" type="button" value="Minimo opc2">
            </div>
        </div>
        <div class="divis">
            <p>volume por aplicativo:</p>
            <div>
                <input id="vol_indvvalval" min="0" max="1" step="0.01" type="range">
                <input id="vol_indvvalbtn" type="button" value="Ok">
            </div>
            <div>
                <input id="vol_indvMax" type="button" value="Maximo">
                <input id="vol_indvMin" type="button" value="Minimo">
            </div>
        </div>
    </div>
    <br><br><br><br>
    
    <div class="sect">
        <h2>Script:</h2>
        <div class="divis">
            <p>Use para atualizar e recarregar o script em cada maquina</p>
            <div>
                <input id="spt_update" type="button" value="Atualizar">
                <!-- <input id="spt_reload" type="button" value="Reiniciar"> -->
            </div>
        </div>
    </div>
</body>
</html>