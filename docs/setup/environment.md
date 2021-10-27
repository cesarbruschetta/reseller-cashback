# Ambiente de Desenvolvimento

## PyEnv
Se for executar o projeto usando virtualenv:


Instruções no site oficial do [pyenv](https://github.com/pyenv/pyenv#basic-github-checkout)


Comandos usados:

* Clonar o projeto:

```shell
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```
* Executar comandos abaixo para add configurações no profile:

```shell
echo -e '\n# Pyenv' >> ~/.bashrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc
exec "$SHELL"
```

* Instalar dependências (pode mudar de acordo com o SO, ver o link das instruções):

```shell
sudo apt-get update; sudo apt-get install --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

* Instalar a versão do Python usada no Projeto e setar como global:
```shell
$ pyenv install 3.8.6
$ pyenv global 3.8.6
```

Checagem (reiniciar o terminal antes)
Vai abrir o console, executar para saber se o path está pegando da pasta do Pyenv:

```shell
$ python
>>> import sys
>>> sys.path
```
## VirtualEnv

* Virtualenvwrapper

Caso queira usar o plugin para criar manualmente os ambientes virtuais pode se informar [aqui](https://github.com/pyenv/pyenv-virtualenv)

* Comandos usados:

```shell
$ git clone https://github.com/pyenv/pyenv-virtualenvwrapper.git $(pyenv root)/plugins/pyenv-virtualenvwrapper

$ echo 'export PYENV_VIRTUALENVWRAPPER_PREFER_PYVENV="true"' >> ~/.bashrc

$ pyenv virtualenvwrapper
```
