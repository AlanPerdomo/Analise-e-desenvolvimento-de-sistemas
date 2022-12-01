<?php 
    $conexao = mysqli_connect("127.0.0.1","root","","mirrorfashion");
    $dados = mysqli_query($conexao,"SELECT * FROM produtos WHERE id = $_GET[id]");
    $produto = mysqli_fetch_array($dados);
?>

<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width">
        <title><?=$produto['nome']?></title>
        <link rel="stylesheet" href="css/reset.css">
        <link rel="stylesheet" href="css/estilos.css">
        <link rel="stylesheet" href="css/produto.css">
    </head>
    <body>

        <?php 
        $cabecalho_title = "Sobre a Mirror Fashion";
        include("cabecalho.php");
        ?>

        <div class="produto-back">
            <div class="container">
                <div class="produto">
                    <h1><?=$produto['nome']?></h1>
                    <p>por apenas <?=$produto['preco']?></p>
                    <form action = "checkout.php" method = "POST">
                    <input type="hidden" name="id" value="<?= $produto['id'] ?>">
                    <input type="hidden" name="nome" value="Fuzzy Cardigan">
                    <input type="hidden" name="preco" value="129,00">
                        <fieldset class="cores">
                            <legend>Escolha a cor:</legend>
                            <input type="radio" name="cor" value="verde" id="verde" checked>
                            <label for="verde">
                                <img src="img/produtos/foto<?= $produto['id'] ?>-verde.png">
                            </label>
                            <input type="radio" name="cor" value="rosa" id="rosa">
                            <label for="rosa">
                                <img src="img/produtos/foto<?= $produto['id'] ?>-rosa.png">
                            </label>
                            <input type="radio" name="cor" value="azul" id="azul">
                            <label for="azul">
                                <img src="img/produtos/foto<?= $produto['id'] ?>-azul.png">
                            </label>
                        </fieldset>
                        <fieldset class="tamanhos">
                            <legend>Escolha o tamanho:</legend>
                            <input type="range" min="36" max="46" value="42" step="2" name="tamanho" id="tamanho">
                            <output for="tamanho" name="valortamanho">42</output>
                        </fieldset>
                        <button class="comprar">Comprar</button>
                    </form>
                </div>
                <div class="detalhes">
                    <h2>Detalhes do produto</h2>
                    <p>
                        <p><?= $produto['descricao'] ?></p>
                    </p>
                    <table>
                        <thead>
                            <tr>
                                <th>Característica</th>
                                <th>Detalhe</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Material</td>
                                <td>Algodão e poliester</td>
                            </tr>
                            <tr>
                                <td>Cores</td>
                                <td>Azul, Rosa e Verde</td>
                            </tr>
                            <tr>
                                <td>Lavagem</td>
                                <td>Lavar a mão</td>
                            </tr>
                        </tbody>
                    </table>
        
        
                </div>

            </div>
        </div>
        <?php include("rodape.php");?>
        <script type="text/javascript" src="js/produto.js"></script>
    </body>
</html>