# Web stack debugging #2

## Introduction
This is the third part of the web stack debugging projects of Holberton School.
Previous parts:
* [Web stack debugging #0](https://github.com/JamesPagani/holberton-system_engineering-devops/tree/master/0x0D-web_stack_debugging_0)
* [Web stack debugging #1](https://github.com/JamesPagani/holberton-system_engineering-devops/tree/master/0x0E-web_stack_debugging_1)

## The problem
There is no "problem" per se, nothing to fix here. Instead, we want to run nginx with another user instead of root. The purpose of this is to minimize the risks of a hacker damaging your server machine should (s)he gain access to that restricted user, since if it gains access to root you may end up having a fancy and heavy paper holder.

### Fixed example
As mentioned above, the objective is to run nginx with another user, which we'll call "nginx", on port 8080.

**Holberton School project solved by: Jaime Andrés Gálvez Villamarin**
