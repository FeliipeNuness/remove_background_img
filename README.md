# 🖼️ AI Background Remover

Uma aplicação web desenvolvida com Flask que permite remover o fundo de imagens automaticamente utilizando inteligência artificial, gerando imagens PNG com fundo transparente.

Este projeto foi criado com o objetivo de aplicar conceitos de desenvolvimento web backend, manipulação de arquivos, requisições HTTP e integração com modelos de IA para processamento de imagens.

---

## 🚀 Tecnologias Utilizadas

- **Python** – Linguagem principal da aplicação
- **Flask** – Framework web responsável por gerenciar rotas e requisições
- **rembg** – Biblioteca que utiliza modelo de Deep Learning para remoção automática de fundo
- **Pillow** – Manipulação e suporte a imagens
- **HTML5** – Estrutura da interface
- **CSS3** – Estilização e layout da aplicação

---

## 📸 Demonstração

O fluxo da aplicação é simples e direto:

1. O usuário envia uma imagem através da interface web.
2. O servidor processa a imagem utilizando IA para remover o fundo.
3. A aplicação gera uma nova imagem em PNG com transparência.
4. Um botão é exibido para permitir o download do resultado final.

---

## 🧠 Como Funciona

A aplicação segue o modelo clássico cliente-servidor. O navegador envia requisições HTTP para o servidor Flask, que processa os dados e retorna respostas dinâmicas.

---

## ⚙️ Funcionamento Técnico Detalhado

### 1️⃣ Inicialização do Servidor

Ao rodar o comando:

```bash
python app.py
```

O Flask inicia um servidor web local na porta `5000`.  
Sua máquina passa a funcionar temporariamente como um servidor, aguardando requisições HTTP do navegador.

No código, isso acontece através de:

```python
if __name__ == "__main__":
    app.run(debug=True)
```

Esse bloco garante que:

- O servidor Flask seja iniciado
- A aplicação rode em modo de desenvolvimento (`debug=True`)
- O servidor reinicie automaticamente caso o código seja alterado

Após isso, a aplicação pode ser acessada em:

```
http://127.0.0.1:5000
```

---

### 2️⃣ Requisição Inicial (GET)

Quando o usuário acessa a página, o navegador envia uma requisição HTTP do tipo **GET** para a rota principal `/`.

Essa rota está definida como:

```python
@app.route("/", methods=["GET", "POST"])
```

Se for uma requisição GET, o Flask executa:

```python
return render_template("index.html", download_file=None)
```

Nesse momento:

- A página HTML é carregada
- Nenhuma imagem foi processada ainda
- O botão de download não aparece

---

### 3️⃣ Envio da Imagem (POST)

Ao selecionar uma imagem e clicar em **Remover Fundo**, o navegador envia uma requisição HTTP do tipo **POST** contendo o arquivo.

O Flask identifica isso com:

```python
if request.method == "POST":
```

O arquivo é capturado com:

```python
file = request.files["image"]
```

Aqui o servidor recebe o arquivo enviado pelo formulário.

---

### 4️⃣ Geração de Nome Único

Para evitar conflitos de nomes, a aplicação utiliza:

```python
filename = str(uuid.uuid4()) + ".png"
```

O `uuid` gera um identificador único universal, garantindo que cada imagem tenha um nome exclusivo.

---

### 5️⃣ Salvamento da Imagem Original

A imagem enviada é salva na pasta `uploads/`:

```python
file.save(input_path)
```

Nesse momento, o arquivo passa a existir fisicamente no servidor.

---

### 6️⃣ Processamento com Inteligência Artificial

Após o salvamento, a imagem é aberta em modo binário:

```python
with open(input_path, "rb") as i:
    input_data = i.read()
    output_data = remove(input_data)
```

A função `remove()` da biblioteca **rembg**:

- Detecta o objeto principal
- Separa automaticamente o fundo
- Remove o background
- Retorna uma nova imagem com canal alfa (transparência)

Todo o processamento ocorre no backend.

---

### 7️⃣ Geração da Imagem Transparente

O resultado da IA é salvo como um novo arquivo PNG:

```python
with open(output_path, "wb") as o:
    o.write(output_data)
```

O formato PNG é utilizado porque suporta transparência.

---

### 8️⃣ Atualização da Interface

Após o processamento, o Flask renderiza novamente o template:

```python
return render_template("index.html", download_file=output_path)
```

Agora `download_file` contém o caminho da imagem processada.

No HTML existe uma condição:

```html
{% if download_file %}
```

Isso faz com que o botão de download apareça apenas quando a imagem estiver pronta.

---

### 9️⃣ Download da Imagem

Ao clicar em **Baixar Imagem**, o navegador envia uma requisição para `/download`.

O Flask utiliza:

```python
send_file(file_path, as_attachment=True)
```

Essa função:

- Lê o arquivo no servidor
- Define os cabeçalhos HTTP corretamente
- Força o download no navegador

---

## 🔄 Fluxo Completo da Aplicação

1. Usuário acessa a página → GET `/`
2. Usuário envia imagem → POST `/`
3. Servidor salva a imagem
4. IA remove o fundo
5. Nova imagem PNG é criada
6. Página é renderizada novamente
7. Botão de download aparece
8. Usuário baixa o arquivo final

---

## 📂 Estrutura do Projeto

```
ai-background-remover/
│
├── app.py
├── static/
│   └── style.css
├── templates/
│   └── index.html
└── uploads/
```

---

## 🛠️ Como Rodar o Projeto Localmente

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Acesse a pasta do projeto:

```bash
cd seu-repositorio
```

3. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

4. Instale as dependências:

```bash
pip install flask rembg pillow
```

5. Execute a aplicação:

```bash
python app.py
```

---

## 🎯 Conceitos Aplicados

Este projeto demonstra aplicação prática de:

- Requisições HTTP (GET e POST)
- Upload e manipulação de arquivos
- Processamento backend
- Integração com modelo de Inteligência Artificial
- Template Engine (Jinja2)
- Estrutura cliente-servidor
- Organização de projeto Flask
- Geração dinâmica de arquivos

---

## 👨‍💻 Autor

Felipe Gomes dos Santos Nunes  
Desenvolvedor Back-End  

---

## 📌 Possíveis Melhorias Futuras

- Implementar sistema de autenticação
- Adicionar preview da imagem antes do download
- Criar fila de processamento para múltiplos usuários
- Hospedar em servidor cloud (Render, Railway, AWS)
- Melhorar UI/UX com animações e feedback visual

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!
