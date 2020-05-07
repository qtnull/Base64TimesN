# Base64\*n
A joke "encryption" algorithm which involves encoding base64 data with base64 n times

# WARNING
This is a joke "encryption" algorithm, what it does is basically encode base64 data with base64, and therefore it's **NOT** secure.
If you are using Solid State Drive, **DO NOT TRY TO TEST THIS MODULE REPEATEDLY ON YOUR SYSTEM**, this will shorten your SSD lifespan and I **AM NOT RESPONSIBLE FOR ANY DAMAGES EITHER FOR ANY EQUIPMENT DAMAGES AND/OR INAPPROPRIATE USE**, if you use this module, you assume all the responsibility for any consequences that will occur.

**I AM NOT RESPONSIBLE WITH ANYTHING YOU DO WITH THIS MODULE**

# Does this have any practical use?
No, it doesn't. It's basically a base64 *Matroska*. I see no practical use besides benchmarking (either CPU, HDD, SSD or even RAM) or destroying SSD and hogging up the CPU, you may even get a memory overflow because I don't really trust Python's memory management.

Please note that if a large `loopTime` has been specified in `EncryptToFile()` or `Encrypt()`, like something like `loopTime = 73`, you may end up creating a monstrous file with a size of 70 or 40 GiB, trust me on that one. The size increases exponentially with the `loopTime` increase.

# Is this algorithm safe?
No, it **isn't**, base64 is just an **encoding scheme and NOT an encryption algorithm**, therefore encoding base64 data with base64 several times **WILL NOT** make your data or data transfer safe and/or secure, if you are looking for that, please take look at [PGP](https://en.wikipedia.org/wiki/Pretty_Good_Privacy) and not this

U got it? GUUD. Let's dive into the nerdy stuff

![Pani Poni Dash - Dancing GIF](/docs/__pani_poni_dash__96c16f2f4669e8f7b7e7717dbda89411.gif)

# Using this module
This is a Python3 module, you can compile it to get better performance (but not much) using the `setup.py` or just use `base64N.py` and `stdbase64.py` (Please note that if you decided to use `setup.py` to compile the module, make sure you install cython by `pip3 install cython` and `python3 setup.py build_ext --inplace` to compile it)

`base64N.py` is the main logic code for encoding or decoding base64 several times.

`stdbase64.py` is just the `base64` module taken from the standard module library from Python 3.8.1 (specifically, taken from Windows x64 installation of Python 3.8.1)

To import them to your script, make sure the `base64N.py` and `stdbase64.py` (or the two compiled files if you used the `setup.py`) is in the same folder or installed in your python module library. And just import them:

`import base64N`

## Functions
### `Encrypt(byte, loopTime, debug = False)`
This function will take the `byte` input parameter and encode it self with base64 `loopTime` times, then returns the encrypted content as a bytes object.
#### Parameters
`byte` (bytes) - input data<br>
`loopTime` (int) - how many times should be `byte` encoded<br>
`debug` (bool) - show additional information: shows the "encrypting" process, how many times `byte` has been encoded

### `Decrypt(byte, loopTime, debug = False)`
This function will take the `byte` input parameter and decode it self with base64 `loopTime` times, then returns the decrypted content as a bytes object.
#### Parameters
`byte` (bytes) - input data<br>
`loopTime` (int) - how many times should be `byte` decoded<br>
`debug` (bool) - show additional information: shows the "decrypting" process, how many times `byte` has been decoded

### `TryDecrypt(byte, decryptLastTime = False, debug = False)`
This function will take the `byte` input parameter will try to decode it as base64 infinite times until an exception has been raised by the `stdbase64.py`, then returns the decrypted content as a bytes object.
#### Parameters
`byte` (bytes) - input data<br>
`decryptLastTime` (bool) - this parameter will decide if the decoding should keep decoding after the `stdbase64.py` raised an exception, this is implemented because `b64decode` from `stdbase64.py` with `validate = True` as parameter cannot decode a base64 encoded non-ASCII character, and enabling this will attempt to decode the encoded non-ascii character. And also enabling this while decoding encoded ASCII data will return a garbled bytes<br>
`debug` (bool) - show additional information: shows the "decrypting" process, how many times has `byte` been decoded

### `EncryptToFile(byte, loopTime, path, debug = False)`
This function will take the `byte` input parameter and encode it self with base64 `loopTime` times, then it writes the result to the file specified in `path`.
#### Parameters
`byte` (bytes) - input data<br>
`loopTime` (int) - how many times should be `byte` encoded<br>
`path` (str) - the absolute or relative path of a file to be written or created<br>
`debug` (bool) - show additional information: shows the "encrypting" process, how many times `byte` has been encoded

### `DecryptToFile(byte, loopTime, path, debug = False)`
This function will take the `byte` input parameter and decode it self with base64 `loopTime` times, then it writes the result to the file specified in `path`.
#### Parameters
`byte` (bytes) - input data<br>
`loopTime` (int) - how many times should be `byte` decoded<br>
`path` (str) - the absolute or relative path of a file to be written or created<br>
`debug` (bool) - show additional information: shows the "decrypting" process, how many times `byte` has been decoded

### `DecryptFromFile(fileObj, loopTime, debug = False)`
This function will read the `fileObj` file object (`open()`) supplied in the parameter and decode the content inside the file `loopTime` times, then returns the decrypted content as a bytes object.
#### Parameters
`fileObj` (`open()` object with open mode `rb`) - input data<br>
`loopTime` (int) - how many times should be `fileObj` decoded<br>
`debug` (bool) - show additional information: shows the "decrypting" process, how many times `byte` has been decoded

### `EncryptFromFile(fileObj, loopTime, debug = False)`
This function will read the `fileObj` file object (`open()`) supplied in the parameter and encode the content inside the file `loopTime` times, then returns the encrypted content as a bytes object.
#### Parameters
`fileObj` (`open()` object with open mode `rb`) - input data<br>
`loopTime` (int) - how many times should be `fileObj` encoded<br>
`debug` (bool) - show additional information: shows the "encrypting" process, how many times `byte` has been encoded

# End
Congratulations, you have reached the end of this README (this is a documantation though). Here is some [resource](https://www.youtube.com/watch?v=dQw4w9WgXcQ) that might help you.

![I have achieved comedy](/docs/i_have_achieved_komedi.jpg)
