# 0x0F. Load balancer

A continuation of 0x0C. Web server. In this project, we are going to set up ANOTHER web server using the exact same configuration used in 0x0C while adding a new header to the HTTP responses (on both web servers). After that, we are setting up a server as a *Load Balancer*, which will balance the incoming traffic between both web servers.

## Contents

**0. Double the number of webservers** (bash script): Configure a new server to be used as a *web server* (using NGINX). On top of having the same configuration as the first web server, it also has a new header variable which will be used to distinguish (in the future) which machine processed the request.
**1. Install your load balancer** (bash script): Configure a new server to be used as a *load balancer* (using HAproxy).

*Made by: Jaime Andrés Gálvez Villamarin*
