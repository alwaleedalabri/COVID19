# covid19.py - using Python

## What is COVID-19?
COVID-19 is basically an HTTP DOS attack tool not a VIRUS, It works like this:


1. It starts making lots of HTTP requests.
2. It sends headers every 15 seconds to keep the connections open, users can change the time period too.
3. It never closes the connection unless the server does, If the server closes a connection, It creates a new one keep doing the same thing.

This exhausts the servers, and the server can't reply to other people.
This type if attack called (low & slow attack).

## How to install and run?

You can clone the git repo or install using **pip**. Here's how you run it.

* `sudo pip3 install covid19`
* `covid19 example.com`

That's all it takes to install and run covid19.py.

If you want to clone using git instead of pip, here's how you do it.

* `git clone https://github.com/asa-asa/COVID19.git`
* `cd covid19`
* `python3 covid19 example.com`

### SOCKS5 proxy support

However, if you plan on using the `-x` option in order to use a SOCKS5 proxy for connecting instead of a direct connection over your IP address, you will need to install the `PySocks` library (or any other `socks` library) as well. [`PySocks`](https://github.com/Anorov/PySocks) is a fork from [`SocksiPy`](http://socksipy.sourceforge.net/) by GitHub user @Anorov and can easily be installed by adding `PySocks` to the `pip` command above or running it again like so:

* `sudo pip3 install PySocks`

You can then use the `-x` option to activate SOCKS5 support and the `--proxy-host` and `--proxy-port` option to specify the SOCKS5 proxy host and its port, if they are different from the standard `127.0.0.1:8080`.

## Configuration options
It is possible to modify the behaviour of covid19 with command-line arguments.

## License
The code is licensed under the MIT License.
