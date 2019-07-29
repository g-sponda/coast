# Coast

The purpose of this project is to collect some data provided by www.alphavantage.co and find the greatest relative span.

## Getting Started

### Prerequisites

This project was written in Python3.7. 

So you will need Python3.7, pip(python3.7) and SQLite3 installed in your machine.

### Installing

If you have all prerequisites, you will be able to install the dependencies or if you prefer to use Docker read the next session.

First enter in the directory of the project.

To install the dependencies execute:

```
pip install -r requirementes.txt
```

After that, open the default.toml and modify the level log which you prefer and add the token of www.alphavantage.co.

The file you will be something like:

```
[logging]
level = "DEBUG"

[api]
token = "<YOUR_TOKEN>"
```

If you would like to run migrations, you can set an enviroment variable with value "yes"

```
export RUN_MIGRATIONS="yes"
```

If you don't need or don't want to reset the tables, you don't need to set this variable, the sqlite database with this project already have the necessary tables.

Now, you will be able to execute the project. Just execute:

```
python coast.py
```

### Docker

If you prefer to run dockerized project, follow the steps bellow:

First build the image:

```
docker build -t coast .
```

```
docker run -itd -p 5000:5000 --name coast coast:latest
```

### Accessing the endpoint

You can see the results the follow addrress: http://127.0.0.1:5000/maxspan

## Running the tests

TODO

## Built With

* [Python 3.7](https://docs.python.org/3.7/) - The Language used
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Micro framework web
* [SQLAlchemy](https://docs.sqlalchemy.org/en/13/) - Python SQL toolkit
* [Requests](https://2.python-requests.org/en/master/) - Non-GMO HTTP library for Python

## Authors

* **Guilherme Sponda** - *Initial work* - [g-sponda](https://github.com/PurpleBooth)

<!-- See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc -->
