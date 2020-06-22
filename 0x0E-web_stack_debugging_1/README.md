# 0x0E. Web stack debugging #1

## Introduction
The second part of the web stack debugging (we're counting from 0).
Previous parts:
* [Web stack debugging #1](https://github.com/JamesPagani/holberton-system_engineering-devops/tree/master/0x0D-web_stack_debugging_0)

Unlike Web stack debugging 0, this directory contains 2 files. Both fix the same mistake, but the second one is a shorter solution.

## The problem
We have an Ubuntu image with _nginx_, a popular and light web server, insatlled on it. By default, it listents all requests done on port 80, the default port for all HTTP communications. However, if you try to make a request to the container it will respond with an error:
```
root@container_id:~# curl 0:80
curl: (7) Failed to connect to 0 port 80: Connection refused
```

### Fixed example
After making the fix, this is how the output should be:
```
root@container_id:~# curl:80
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

**Holberton School project solved by: Jaime Andrés Gálvez Villamarin**
