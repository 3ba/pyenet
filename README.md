# pyenet

pyenet is a python wrapper for the ENet library by Lee Salzman,
 http://enet.bespin.org

This fork is modified to build against [3ba/enet](https://github.com/3ba/enet/tree/ubisoft),
which adds support for the Ubisoft protocol and SOCKS5 proxy implementation.

## License
pyenet is licensed under the BSD license, see LICENSE for details.
enet is licensed under the MIT license, see http://enet.bespin.org/License.html

## Dependencies

Building pyenet requires all the same dependencies as enet plus Cython and,
obviously, Python.

## Installation

The enet sources live in the enet/ submodule, so clone pyenet recursively to
pull them in:
```
$ git clone --recursive <repository-url>
```
If you already cloned without `--recursive`, fetch the submodule with:
```
$ git submodule update --init --recursive
```

Next step is to run the setup.py build:
```
$ python setup.py build
```
Once that is complete, install the new pyenet module:
```
$ python setup.py install
```

## Usage

Once you have installed pyenet, you only need to import the enet module to
start using enet in your project.

Example server:
```py
>>> import enet
>>> host = enet.Host(enet.Address("localhost", 33333), 1, 0, 0)
>>> event = host.service(0)
```
Example client:
```py
>>> import enet
>>> host = enet.Host(None, 1, 0, 0)
>>> peer = host.connect(enet.Address("localhost", 33333), 1)
```
More information on usage can be obtained from:
 http://enet.bespin.org/Tutorial.html
