# DataSanitizer

DataSanitizer é um script Python que ajuda a proteger informações sensíveis em arquivos de log. O script identifica e substitui e-mails, números de telefone e endereços IP por termos genéricos para anonimizar os dados.

#Funcionalidades:

- Anonimiza endereços de e-mail
- Anonimiza números de telefone
- Anonimiza endereços IP
- Cria um backup opcional do arquivo de log original
- Registra a quantidade de substituições para cada tipo de dado

#Requisitos:

- Python 3.x

#Instalação:

Clone o repositório e navegue até o diretório onde o script foi salvo.

```
git clone https://github.com/Marrogrigues/DataSanitizer.git
cd DataSanitizer
```

#Uso

Para utilizar o script, você pode usar o seguinte comando:
```
python3 data_sanitizer.py --input /caminho/para/arquivo_de_log_original.log --output /caminho/para/arquivo_de_log_higienizado.log
```
Se desejar criar um backup do arquivo de log original, adicione o parâmetro --backup:
```
python3 data_sanitizer.py --input /caminho/para/arquivo_de_log_original.log --output /caminho/para/arquivo_de_log_higienizado.log --backup
```
O backup será salvo com o mesmo nome do arquivo original, acrescido de .bak.

#Output

O script imprimirá a quantidade de e-mails, números de telefone e endereços IP que foram anonimizados:
```
Sanitization complete. Sanitized log saved to /caminho/para/arquivo_de_log_higienizado.log.
Emails sanitized: 10
Phone numbers sanitized: 5
IP addresses sanitized: 20
```
