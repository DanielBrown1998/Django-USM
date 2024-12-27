<h1 align='center'>MON_UERJ_PROJECT</h1> 

# Finalidade do Projeto
<p align='center'>Projeto de site iterativo feito em Django5 com a finalidade de atender à demanda dos alunos da disciplina de arquitetura de computadores, o site consiste em marcar monitorias junto ao monitor da disciplina.</p>

# Status
<h4 align="center"> 
    :construction:  Projeto em etapa de finalização  :construction:
</h4>

# :hammer: Funcionalidades do projeto


- `Funcionalidade 1`: marcar monitoria mediante disponibildade de horários.
- `Funcionalidade 2`: dispor ao usuário os dias e horários disponíveis para marcação de monitoria.
- `Funcionalidade 3`: O monitor pode alterar os dias e os horarios da monitoria.
- `Funcionalidade 4`: O usuário pode cancelar a monitoria, mas só até o dia anterior da data.
- `Funcionalidade 5`: O monitor pode alterar o status da monitoria somente após o dia monitoria.
- `Funcionalidade 6`: Para o usuário cadastrar na plataforma, é necessário que o monitor disponibilize uma matrícula a ele.
- `Funcionalidade 7`: O monitor pode bloquear um usuário.
- `Funcionalidade 8`: O sistema irá disponibilizar ao usuário o histórico de monitorias marcadas pelo usuário.
- `Funcionalidade 9`: O sistema irá disponibilizar ao monitor o histórico de monitorias marcadas por todos os usuários.

# Pictures

- Funcionalidade 9, 2;
![Monitoria e mais 1 página - Escola — Microsoft​ Edge 26_12_2024 11_46_14](https://github.com/user-attachments/assets/e4efb664-b3f4-4907-8073-5f6f5aa6c2ca)

- Funcionalidade 3;
![Monitoria e mais 1 página - Escola — Microsoft​ Edge 26_12_2024 11_47_18](https://github.com/user-attachments/assets/2c86ebd2-b7c0-4c73-b778-5e0aac9272f4)

- Funcionalidade 8, 2, 1;
![Monitoria e mais 1 página - Escola — Microsoft​ Edge 26_12_2024 11_53_51](https://github.com/user-attachments/assets/0189a169-39ea-49e2-84a2-2fec75e155cd)

- Funcionalidade 4;
![Monitoria - Escola — Microsoft​ Edge 26_12_2024 12_15_37](https://github.com/user-attachments/assets/2e8fac2a-690f-429e-8dee-9db870a62780)

- Funcionalidade 6;
![Monitoria e mais 1 página - Escola — Microsoft​ Edge 26_12_2024 11_47_49](https://github.com/user-attachments/assets/7da69601-7ffe-4b64-b206-ccf245f49548)

# Instalação e Uso
1- Baixe o arquivo no github ou clone este repositório

    git clone 'https://github.com/DanielBrown1998/Django-USM'

2- Crie um arquivo local_settings.py, ponha o arquivo abaixo e salve.
    
    DEBUG = 1
    ALLOWED_HOSTS = []
    SECRET_KEYS = ''

3- abra o terminal na pasta raiz
4- digite o comando: 
    
    pip install -r requirements.txt

5- crie o super-usuário digite o camando: 

    django-admin create superuser

6- IMPORTANTE!!! ao pedir o username: digite um número aleátorio de 11 números
SEM O SUPERUSUÁRIO o programa irá crachar

7- em seguida, digite os comandos:
    
    python manage.py migrate
    python manage.py runserver

9-digite seu username e faça o login
10- vá em update e termine o cadastro do superusuário

# Tecnologias e técnicas utilizadas.

- Python3;
- Django5;
- CSS3;
- POO;
- VsCode;

# Autor

- Daniel Brown R. M. dos Passos -> https://github.com/DanielBrown1998
    
  


