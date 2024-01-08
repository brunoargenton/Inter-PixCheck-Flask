
<h1>PixCheck App</h1>

<p>O PixCheck é uma aplicação web simples desenvolvida em Flask que recupera e exibe transações Pix da API do Banco Inter. Ele calcula o valor total recebido por meio de transações Pix, excluindo destinatários específicos definidos na lista "exclusoes".</p>

<h2>Caso de Uso</h2>
<p>O 
PixCheck é uma ferramenta que oferece uma alternativa para contornar as taxas associadas ao Pix, geralmente cobradas por adquirentes de maquininhas de cartão. Ele proporciona ao vendedor uma confirmação instantânea sobre a entrada de um pagamento na conta corrente empresarial. Dessa forma, o atendente pode validar a transação sem a necessidade de acessar diretamente a conta bancária do estabelecimento. Ao final do dia, os valores ficam visíveis, facilitando o fechamento do caixa. No exemplo fornecido, essa solução foi desenvolvida utilizando a API do Banco Inter.</p>
<ul>
    <li>Passo 1: Atendente passa a chave PIX e o valor da compra ao cliente</li>
    <li>Passo 2: Cliente realiza o pagamento pelo PIX</li>
    <li>Passo 3: Atendente confirma o recebimento na tabela de Pagamentos Recebidos</li>   
</ul>

<h2>Pré-requisitos</h2>

<p>Antes de executar o aplicativo PixCheck, certifique-se de ter o seguinte instalado:</p>

<ul>
    <li>Python (versão 3.6 ou superior)</li>
    <li>Flask</li>
    <li>Requests</li>
</ul>

<h2>Configuração</h2>

<p>Você pode personalizar a aplicação modificando as seguintes variáveis no arquivo <code>app.py</code>:</p>

<ul>
    <li><code>exclusoes</code>: Lista de destinatários a serem excluídos do cálculo total.</li>
    <li><code>inicio</code> e <code>fim</code>: Caso queira testar em um dia específico, use um intervalo de datas para transações Pix (formato: "AAAA-MM-DD").</li>
    <li><code>request_body</code>: preencha com as credenciais obtidas na plataforma de Desenvolvedor do Banco Inter.</li>
    <li><code>cert_paths</code>: preencha com o caminho dos arquivos "certificado.crt" e "chave.key"</li>
    <li>Certifique-se de que os certificados obtidos na plataforma de desenvolvedor do Banco Inter estejam na pasta indicada.</li>
    <li>Certifique-se de copiar a pasta "templates", com os arquivos HTML.</li>
</ul>

<h2>Uso</h2>

<ul>
    <li>Execute o aplicativo:</li>
</ol>

<pre><code>python app.py</code></pre>

<p>A aplicação estará acessível em <a href="http://localhost:80/">http://localhost:80/</a> em seu navegador. Ou através do ip do servidor, caso esteja acessando de outro host.</p>

![image](https://github.com/brunoargenton/Inter-PixCheck-Flask/assets/38015713/b224d507-e644-46cd-b2a9-df0d9425a687)


<h2>Reconhecimentos</h2>

<ul>
    <li>Esta aplicação utiliza o Flask, um microframework web para Python.</li>
    <li>A biblioteca Requests é utilizada para fazer requisições HTTP.</li>
    <li>Desenvolvido por Bruno Argenton.</li>
</ul>
