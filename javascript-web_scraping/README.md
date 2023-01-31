# JavaScript - Web scraping

## Resources
### Read or watch:

- [Working with JSON data](https://intranet.aluswe.com/rltoken/MiTgYMkQEYW7Ydfr2Enb-A)
- [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://intranet.aluswe.com/rltoken/FaAMZnG2vwWwzlkrYrhC0A)
- [request module](https://intranet.aluswe.com/rltoken/ZOiv4Q-sjWN87QlfMxg2PQ)
- [Modern JS](https://intranet.aluswe.com/rltoken/ULF1RX7OyNexRK1q7qpcwA)

## Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://intranet.aluswe.com/rltoken/y1YyQMtdFjC6uqUzoggDkQ), without the help of Google:

### General
- Why JavaScript programming is amazing
- How to manipulate JSON data
- How to use request and fetch API
- How to read and write a file using fs module
## Requirements
### General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 14.04 LTS using node (version 10.14.x)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/node
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
- All your files must be executable
- The length of your files will be tested using wc
- You are not allowed to use var

# More Info
### Install Node 10
```$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -```
```$ sudo apt-get install -y nodejs```

### Install semi-standard
[Documentation](https://intranet.aluswe.com/rltoken/ZDy8VNGPo5AIV8I4YAJ7nA)

```$ sudo npm install semistandard --global```
### Install request module and use it
[Documentation](https://intranet.aluswe.com/rltoken/ZOiv4Q-sjWN87QlfMxg2PQ)

```$ sudo npm install request --global```
```$ export NODE_PATH=/usr/lib/node_modules```
### Notes:
Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).