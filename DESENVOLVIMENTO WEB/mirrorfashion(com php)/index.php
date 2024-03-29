<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Mirror Fashion</title>
        <link rel="stylesheet" href="css/reset.css">
        <link rel="stylesheet" href="css/estilos.css">
    </head>
    <body>
        <?php 
        $cabecalho_title = "Home da Mirror Fashion";
        include("cabecalho.php");
        ?>
        <div class="container destaque">
            <section class="busca">
                <h2>Busca</h2>
                <form>
                    <input type="search">
                    <button>Buscar</button>
                </form>
            </section>

            <section class="menu-departamentos">
                <h2>Departamentos</h2>
                <nav>
                    <ul>
                        <li>
                            <a href="#">Blusas e Camisas</a>
                            <ul>
                                <li><a href="#">Manga curta</a></li>
                                <li><a href="#">Manga comprida</a></li>
                                <li><a href="#">Camisa social</a></li>
                                <li><a href="#">Camisa casual</a></li>
                            </ul>
                        </li>
                        <li><a href="#">Calças</a></li>
                        <li><a href="#">Saias</a></li>
                        <li><a href="#">Vestidos</a></li>
                        <li><a href="#">Sapatos</a></li>
                        <li><a href="#">Bolsas</a></li>
                        <li><a href="#">Acessórios</a></li>
                    </ul>
                </nav>
            </section>

            <section class="banner-destaque">
                <figure>
                    <a href="#" class="pause"></a>
                    <img src="img/destaque-home.png" alt="Promoção: Big City Night">
                </figure>
            </section>
        </div>

        <div class="container paineis">
            <section class="painel novidades">
                <h2>Novidades</h2>
                <ol>
                    <?php
                        $conexao = mysqli_connect("127.0.0.1","root","","mirrorfashion");
                        $dados = mysqli_query($conexao,"SELECT * FROM produtos ORDER BY data DESC LIMIT 0,12");
                        while ($produto = mysqli_fetch_array($dados)):
                    ?>
                    <li>
                        <a href="produto.php?id=<?=$produto['id']?>">
                            <figure>
                                <img src = "img/produtos/miniatura<?=$produto['id']?>.png" alt = "<?=$produto['nome']?>">
                                <figcaption><?=$produto['nome']?>por<?=$produto['preco']?></figcaption>
                            </figure>
                        </a>
                    </li>
                    <?php endwhile; ?>
                </ol>
            </section>
            <section class="painel mais-vendidos">
                <h2>Mais Vendidos</h2>
                <ol>
                <?php
                        $conexao = mysqli_connect("127.0.0.1","root","","mirrorfashion");
                        $dados = mysqli_query($conexao,"SELECT * FROM produtos ORDER BY vendas DESC LIMIT 0,12");
                        while ($produto = mysqli_fetch_array($dados)):
                    ?>
                    <li>
                        <a href="produto.php?id=<?=$produto['id']?>">
                            <figure>
                                <img src = "img/produtos/miniatura<?=$produto['id']?>.png" alt = "<?=$produto['nome']?>">
                                <figcaption><?=$produto['nome']?>por<?=$produto['preco']?></figcaption>
                            </figure>
                        </a>
                    </li>
                    <?php endwhile; ?>
                </ol>
            </section>
        </div>        
        <?php include("rodape.php");?> 
        <script type="text/javascript" src="js/banner.js"></script>  
    </body>
</html>