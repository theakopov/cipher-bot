# Cipher bot
[<img src=https://img.shields.io/badge/Telegram-%40TheCipher__bot-blue>](https://t.me/TheCipher_bot)
<img src=https://img.shields.io/badge/Aiogram-3.0.0b7-blue>

**Telegram bot for encrypting and hashing text**

### Installing

* Clone the git repository:

```
git clone https://github.com/theakopov/cipher-bot.git
cd cipher-bot
```


* Create venv and install dependencies:

```
python3 -m venv venv

# for windows
venv\Scripts\activate
# for linux
source venv/bin/activate

pip3 install -r requirements.txt
```

### Next you need to connect the databases.
Here is an example of postgresql connection.
- Installation of *postgresql* (https://www.postgresql.org/download/)
- Next, you need to create an empty database using the sql query: `CREATE DATABASE cipher;`. You can do this, for example, using the `psql` utility, launched as a user in postgresql.
- After, you must create tables in the database. You can use the alembic utility. Using the command: `alembic upgrade head`
However, this will not be enough to launch the application. You will also need to download and install the `redis` service.

*! All connection data must be specified in .env, which you can create using the example `.env.example`*
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
