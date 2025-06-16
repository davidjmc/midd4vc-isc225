<h1 align="center">Midd4VC: A Middleware for Vehicular Cloud Computing</h1>

## 📝 Índice <a name="summary"></a>

- [📖 About](#about)
- [🏁 Getting Started](#getting_started)
- [📱 Executing](#usage)
- [⛏️ Tecnologias Utilizadas](#built_using)

## 📖 Midd4VC <a name = "about"></a>

## 🏁 Getting Started <a name = "getting_started"></a>

Estas instruções irão ajudá-lo a obter uma cópia deste projeto e executá-lo em sua máquina local para fins de desenvolvimento e teste.

Clone este repositório em sua máquina local:

```bash
git clone https://github.com/davidjmc/Midd4VC.git
```

Entre no diretório do projeto:

```bash
cd Midd4VC
```

Este software foi desenvolvido para ser executado em um ambiente Linux.

### Pré-requisitos

Caso deseje utilizar o Docker, siga diretamente para a seção [Docker](#docker). Caso contrário, continue com as instruções abaixo.

Para executar o projeto, você precisará ter o Node.js e o npm instalados em sua máquina. Você pode baixar o Node.js [aqui](https://nodejs.org/) ou através do comando abaixo:

```bash
# Gerenciador de versões do Node.js:
curl -o- https://fnm.vercel.app/install | bash

# Baixar e instalar o Node.js:
fnm install 22.14.0

# Definir a versão do Node.js:
fnm use 22.14.0
```

Adicionalmente, instale os pacotes necessários para gerar os gráficos:

```bash
sudo apt-get install build-essential libcairo2-dev libpango1.0-dev libjpeg-dev libgif-dev librsvg2-dev
```

### Instalação

Após clonar o repositório, entre no diretório do projeto e instale as dependências:

```bash
npm install
```

### Clientes

Siga as instruções para configurar o(s) [cliente(s)](https://github.com/MalwareDataLab/autodroid-watcher-client) na máquina onde o [AutoDroid Worker](https://github.com/MalwareDataLab/autodroid-worker) está instalado.

## 📱 Utilização <a name="usage"></a>

Certifique-se de que o túnel HTTP esteja operacional e o(s) [cliente(s)](https://github.com/MalwareDataLab/autodroid-watcher-client) estejam configurados para enviar os dados para a URL que foi gerada ao executar o túnel.

### Executando o Servidor

Para executar o servidor, utilize o comando abaixo:

```bash
npm run dev -q 10 -p 3000 -e prod -i 1 -t "secure_token" --email john@doe.com --password "123456"
```

### Resultados

Os resultados são armazenados na pasta `experiments` e são organizados por data e hora. Cada iteração é armazenada em um arquivo separado.

Os resultados dos experimentos são armazenados em arquivos CSV e gráficos, que podem ser utilizados para análise e visualização dos dados coletados, uma amostra de uma iteração completa está disponível na [pasta `examples`](https://github.com/MalwareDataLab/autodroid-watcher-server/tree/main/docs/examples) deste repositório.

## ⛏️ Tecnologias Utilizadas <a name = "built_using"></a>

- [TypeScript](https://www.typescriptlang.org/) - Linguagem de programação
- [Node.js](https://nodejs.org/) - Ambiente de execução
- [Axios](https://axios-http.com/) - Cliente HTTP
- [Chart.js](https://www.chartjs.org/) - Biblioteca de gráficos
- [Socket.io](https://socket.io/) - Biblioteca para comunicação em tempo real