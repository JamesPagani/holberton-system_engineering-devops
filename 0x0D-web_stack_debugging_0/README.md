# 0x0D. Web stack debugging #0

## Introduction
This project consists on finding a problem with a container, fix it, and create a _shell_ script that automatically solves the problem. This kind of activities will be part of the Full-Stack software engineer, and the only way to get better at debugging is to do it since theory alone will **NEVER** be enough.

This directory only contains one file (besides this one), which is the fix of the problem described bellow. Also, _beware that this script will not work on a Windows terminal_.

## The Problem
We have a (Docker) image with Apache. However, when we try to make a request to a container with this image we get an error:

```
ubuntu@ubuntu:~$ curl 0:8080
curl: (56) Recv failure: Connection reset by peer
ubuntu@ubuntu:~$ 
```
After fixing the issue, this should be the expected response:
```
ubuntu@ubuntu:~$ curl 0:8080
Hello Holberton
ubuntu@ubuntu:~$ 
```

*Try solving the problem before looking at the answer.*

**Holberton School project solved by: Jaime Andrés Gálvez Villamarin**
