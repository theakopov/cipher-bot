# Cipher bot
[<img src=https://img.shields.io/badge/Telegram-%40TheCipher__bot-blue>](https://t.me/TheCipher_bot)
<img src=https://img.shields.io/badge/Aiogram-3.0.0b7-blue>

Telegram bot for encrypting and hashing text

### Installing

* Clone the git repository:

```
git clone https://github.com/theakopov/cipher-bot.git
cd cipher-bot
```


* Create venv and install dependencies:

```
python -m venv venv

# for windows
venv\Scripts\activate
# for linux
source venv/bin/activate

pip3 install -r requirements.txt
```

Also, you must have redis service deployed,
as well as postgresql with an existing database, the details of which can be viewed in migration/versions folder
### Running

```
python -m run
```
<i>To use tests, use the command in the virtual environment

```pytest ./tests/ciphers_test.py ```

## Admin Features

- ```/stat``` - Number of users in the bot
- ```/config``` - Bot configuration data
- ```/logs``` - Log file
## License

This project is licensed under the MIT License - see the
[LICENSE](https://github.com/theakopov/cipher-bot/blob/main/LICENSE) file for details.
