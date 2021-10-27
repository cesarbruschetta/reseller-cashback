# Configurações do Sistema


## Arquivo `.env`
* É preciso criar o arquivo `.env` com as variáveis locais, obrigatoriamente deve gera a `SECRET_KEY`.

* Definir as variáveis locais

    ```shell
    export SECRET_KEY='12qweasdzxc'
    ```

* Executar o seguinte comando para criar o .env de desenvolvimento:

    ```shell
    $ make install-env-file
    ```
