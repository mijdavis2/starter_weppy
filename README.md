# Starter Weppy
[![Build Status](https://travis-ci.org/mijdavis2/starter_weppy.svg?branch=master)](https://travis-ci.org/mijdavis2/starter_weppy)
[![Coverage Status](https://coveralls.io/repos/github/mijdavis2/starter_weppy/badge.svg?branch=master)](https://coveralls.io/github/mijdavis2/starter_weppy?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/3e6e8b44b40a4f12937557a794b7d6a3)](https://www.codacy.com/app/mdavis/starter_weppy?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mijdavis2/starter_weppy&amp;utm_campaign=Badge_Grade)
[![Weppy Version](https://img.shields.io/badge/weppy-1.2.10-blue.svg)](https://github.com/gi0baro/weppy)

Starter Weppy is a python web application starter kit built on the [weppy framework](https://github.com/gi0baro/weppy). 
Current version is based on Weppy 1.2 with an MVC scaffolding. 
An api module, dev mode, and mostly 100% test coverage are included out of the box.

**Live demo: [https://starter-weppy.com](https://starter-weppy.com)**

## Start a New Project:
 Use the Starter Weppy yeoman generator: [generator-weppy-mvc](https://github.com/mijdavis2/generator-weppy-mvc).
 
 > # generator-weppy-mvc 
 > [![NPM version][npm-image]][npm-url] [![Build Status][travis-image]][travis-url] [![Coverage percentage][coveralls-image]][coveralls-url] [![Codacy Badge](https://api.codacy.com/project/badge/Grade/ce0ad20ca59947af86b0f17a5779c804)](https://www.codacy.com/app/mijdavis2/generator-weppy-mvc?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mijdavis2/generator-weppy-mvc&amp;utm_campaign=Badge_Grade)
 >
 > The definitive [starter-weppy](https://github.com/mijdavis2/starter_weppy) generator.

## Run
**Requirements**:

- Python 3.4 - 3.5+

For automated pip and virtual env setup and creation, 
clone this repository and in your terminal do:

```
. ./setup.sh
python run.py
```

Otherwise, do:
```
pip install -r requirements.txt
python run.py
```

### Docker
To make your application available at ```http://localhost/```:

```
docker build -t starter-weppy .
docker run -it -p 80:8000 --rm --name starter-weppy starter-weppy
```


## Develop
Running in development mode will enable debug pages,
automatically create test, users in multiple states,
and upon killing the app, those test users will automatically be 
deleted from the DB.

To start the app in development mode, do:

```
python run.py --dev
```

See ```starter_weppy/cli.py``` for cli commands. 

## Test

Client testing:

```
py.test -v -s --cov-report term-missing --cov=starter_weppy -r w tests/client
```

Integration (selenium) testing:

```
./tests/selenium/run.sh
```

## Caveats
- The current setup.sh script is set to Python 3.5.2. Though I 
suggest upgrading to 3.5.2, you can replace PYTHON_VERSION with 
3.4.3 in the script.

## License

MIT © [mijdavis2](http://mdavis.io)


[npm-image]: https://badge.fury.io/js/generator-weppy-mvc.svg
[npm-url]: https://npmjs.org/package/generator-weppy-mvc
[travis-image]: https://travis-ci.org/mijdavis2/generator-weppy-mvc.svg?branch=master
[travis-url]: https://travis-ci.org/mijdavis2/generator-weppy-mvc
[daviddm-image]: https://david-dm.org/mijdavis2/generator-weppy-mvc.svg?theme=shields.io
[daviddm-url]: https://david-dm.org/mijdavis2/generator-weppy-mvc
[coveralls-image]: https://coveralls.io/repos/mijdavis2/generator-weppy-mvc/badge.svg
[coveralls-url]: https://coveralls.io/r/mijdavis2/generator-weppy-mvc
