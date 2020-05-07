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

## 函数
### `Encrypt(byte, loopTime, debug = False)`
此函数将会把`byte`参数传入的数据使用Base64编码`loopTime`次，然后返回加密后的数据，返回的数据类型为`bytes`。
#### 参数
`byte` (bytes) - 输入数据<br>
`loopTime` (int) - `byte`应该重复被base64编码几次<br>
`debug` (bool) - 显示“加密”的过程，输出`byte`已经被重复编码几次了

### `Decrypt(byte, loopTime, debug = False)`
此函数将会把`byte`参数传入的数据使用Base64解码`loopTime`次，然后返回解密后的数据，返回的数据类型为`bytes`。
#### 参数
`byte` (bytes) - 输入数据<br>
`loopTime` (int) - `byte`应该重复被base64解码几次<br>
`debug` (bool) - 显示“解密”的过程，输出`byte`已经被重复解码几次了

### `TryDecrypt(byte, decryptLastTime = False, debug = False)`
此函数将会尝试将`byte`参数传入的数据使用base64解码无限次，直到`stdbase64.py`出现一个Exception，然后返回解密后的数据，返回的数据类型为`bytes`。
#### Parameters
`byte` (bytes) - 输入数据<br>
`decryptLastTime` (bool) - 此参数将会决定`stdbase64.py`出现Exception后继续解码一次，因为`stdbase64.py`的`b64decode`函数使用`validate = True`参数时，无法解码Base64编码的非ASCII字符，设置此参数为`True`会尝试解码非ASCII字符的base64数据。如果将此参数设置为`True`后解码base64编码的ASCII字符将会返回乱码<br>
`debug` (bool) - 显示“解密”的过程，输出`byte`已经被重复解码几次了

### `EncryptToFile(byte, loopTime, path, debug = False)`
此函数将会把`byte`参数传入的数据使用Base64编码`loopTime`次，然后，然后将加密后的数据写入`path`参数指定的文件。
#### Parameters
`byte` (bytes) - 输入数据<br>
`loopTime` (int) - `byte`应该重复被base64编码几次<br>
`path` (str) - 写入文件的相对路径或绝对路径<br>
`debug` (bool) - 显示“加密”的过程，输出`byte`已经被重复编码几次了

### `DecryptToFile(byte, loopTime, path, debug = False)`
此函数将会把`byte`参数传入的数据使用Base64解码`loopTime`次，然后，然后将解密后的数据写入`path`参数指定的文件。
#### Parameters
`byte` (bytes) - 输入数据<br>
`loopTime` (int) - `byte`应该重复被base64解码几次<br>
`path` (str) - 写入文件的相对路径或绝对路径<br>
`debug` (bool) - 显示“解密”的过程，输出`byte`已经被重复解码几次了

### `DecryptFromFile(fileObj, loopTime, debug = False)`
此函数将会读取`fileObj`参数传入的file对象（`open()`）然后将数据使用Base64解码`loopTime`次，最后返回解密后的数据，返回的数据类型为`bytes`。
#### Parameters
`fileObj` (打开模式为`rb`的`open()`（file）对象) - 输入数据<br>
`loopTime` (int) - `fileObj`应该重复被base64解码几次<br>
`debug` (bool) - 显示“解密”的过程，输出`fileObj`已经被重复解码几次了

### `EncryptFromFile(fileObj, loopTime, debug = False)`
此函数将会读取`fileObj`参数传入的file对象（`open()`）然后将数据使用Base64编码`loopTime`次，最后返回加密后的数据，返回的数据类型为`bytes`。
#### Parameters
`fileObj` (打开模式为`rb`的`open()`（file）对象) - 输入数据<br>
`loopTime` (int) - `fileObj`应该重复被base64解码几次<br>
`debug` (bool) - 显示“加密”的过程，输出`fileObj`已经被重复编码几次了

# End
Congratulations, you have reached the end of this README (this is a documantation though). Here is some [resource](https://www.youtube.com/watch?v=dQw4w9WgXcQ) that might help you.

![I have achieved comedy](/docs/i_have_achieved_komedi.jpg)
