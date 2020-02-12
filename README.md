c:\>mkdir flask

c:\>cd flask

c:\flask>virtualenv venv
Using base prefix 'c:\\python37-32'
New python executable in c:\flask\venv\Scripts\python.exe
Installing setuptools, pip, wheel...
done.

c:\flask>venv\scripts\activate
(venv) c:\flask>pip install Flask
Collecting Flask
  Using cached Flask-1.1.1-py2.py3-none-any.whl (94 kB)
Collecting Werkzeug>=0.15
  Downloading Werkzeug-1.0.0-py2.py3-none-any.whl (298 kB)
     |████████████████████████████████| 298 kB 242 kB/s
Collecting click>=5.1
  Using cached Click-7.0-py2.py3-none-any.whl (81 kB)
Collecting itsdangerous>=0.24
  Using cached itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
Collecting Jinja2>=2.10.1
  Downloading Jinja2-2.11.1-py2.py3-none-any.whl (126 kB)
     |████████████████████████████████| 126 kB 2.2 MB/s
Collecting MarkupSafe>=0.23
  Using cached MarkupSafe-1.1.1-cp37-cp37m-win32.whl (15 kB)
Installing collected packages: Werkzeug, click, itsdangerous, MarkupSafe, Jinja2, Flask
Successfully installed Flask-1.1.1 Jinja2-2.11.1 MarkupSafe-1.1.1 Werkzeug-1.0.0 click-7.0 itsdangerous-1.1.0

c:\flask>python Hello.py
 * Serving Flask app "Hello" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [12/Feb/2020 19:36:33] "GET / HTTP/1.1" 404 -
127.0.0.1 - - [12/Feb/2020 19:36:33] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [12/Feb/2020 19:36:49] "GET /hello.py HTTP/1.1" 404 -
127.0.0.1 - - [12/Feb/2020 19:37:02] "GET /hello HTTP/1.1" 200 -
