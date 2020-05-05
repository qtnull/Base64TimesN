# Base64\*n
A joke "encryption" algorithm which involves encoding base64 data with base64 n times

# WARNING
This is a joke "encryption" algorithm, what it does is basically encode base64 data with base64, and therefore it's **NOT** secure.
If you are using Solid State Drive, do **NOT TRY THIS ON YOUR SYSTEM**, this will shorten your SSD lifespan and I **AM NOT RESPONSIBLE FOR ANY DAMAGES**

# Using this module
This is a Python3 module, you can compile it to get better performance (but not much) using the `setup.py` or just use `base64N.py` and `stdbase64.py`

To import them to your script, make sure the `base64N.py` and `stdbase64.py` (or the two compiled files if you used the `setup.py`) is in the same folder or installed in your python module library. And just import them:

`import base64N`

## Functions
### `Encrypt(byte, loopTime, debug = False)`
This function will take the `byte` input parameter and encode it self with base64 `loopTime` times, it will return a bytes data type.
#### Parameters
byte (bytes) - input data
loopTime (int) - how many times should be `byte` encoded
debug (bool) - show additional information: shows the "encrypting" process, how many times has `byte` been encoded

### `Decrypt(byte, loopTime, debug = False)`
This function will take the `byte` input parameter and decode it self with base64 `loopTime` times, it will return a bytes data type.
#### Parameters
byte (bytes) - input data
loopTime (int) - how many times should be `byte` encoded
debug (bool) - show additional information: shows the "decrypting" process, how many times has `byte` been decoded

# Does this have any practical use?
No, it doesn't. It's basically a base64 *Matroska*.
