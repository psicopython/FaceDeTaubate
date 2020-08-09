# FaceDeTaubate
uma rede social, ou quase...


Bora lá!

Obs:
```sh
° Necessário:
    • Python 3
    • VirtualEnv
    • pip3
```

(Adapte seu código, caso seja de plataforma
ou versão do python diferente)

Preparando o Ambiente:
```sh

python -m venv .venv
. venv/bin/activate
cd FaceDeTaubate/social/
pip install -r requirements.txt

```

Iniciando o banco de dados
```sh
flask db init
flask db migrate
flask db upgrade
```

Rodando o app:
```sh
flask run
```

Após, vá ao navegador e digite:
```sh
127.0.0.1:5000
```

Aparecerá a tela inicial, 
clique no botão de menu no canto superior direito.
Clique em cadastro, preencha da maneira que achar melhor.
Em seguida será redirecionado ao Index novamente,
Note q tera um link 'no que esta pensando?' 
Se clique nele vc sera redirecionado a uma página para criar
Uma publicação, escreva oq quiser, selecione uma imagem (ou várias)
E cliente no botão 'enviar', após isso, volte a tela inicial e vc poderá ver sua publicação!
