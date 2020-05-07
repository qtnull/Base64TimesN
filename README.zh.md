# Base64\*n
一个玩具性质的“加密算法”把普通的Base64变成了Base64*N

# 警告！
这玩意是一个特别艹蛋的加密算法，本质上是用base64来加密base64的数据，所以这玩意一点也不(重点)安全。
如果你用的是SSD硬盘，别去一次又一次的试验这玩意，我敢打包票，这会让你的SSD更早报废，使用这个项目造成设备损坏的，保留免责权利(也就是我不管)，如果你因为使用这个项目造成不可逆伤害的，发生的后果自负。
*我对你在这个项目上干的一切事情都不会负责的。
#这玩意有啥用啊？
没用，一点用都没有，基本上没啥用，唯一的作用是基准测试(范围包括你的CPU，HDD，SSD或许还有RAM)或者说是干翻你的电脑，干死你的硬盘，
除了这些以外，没啥用了，严重的会造成内存溢出，因为吧，Python的内存管理不太可信(主观)
请注意，如果在“EncryptToFile（）”或“Encrypt（）”中指定了一个大的“loopTime”，例如“loopTime=73”，则可能会创建一个大小为70或40 GiB的巨大文件，请因为算法的特色，这个文件的大小随“loopTime”的增加呈指数增长。
# 这个算法有够安全吗
不，这玩意一点都不安全，base64防君子不防小人，就算加密个几百次都没用，如果你想来个真正的加密算法，看看这个 [PGP](https://en.wikipedia.org/wiki/Pretty_Good_Privacy) 而不是这个艹蛋的算法
好了吗，孩子，接下来我们看一些更枯燥的东西，确保你能看得下去，可以考虑吃一点零食。



![Pani Poni Dash - Dancing GIF](/docs/__pani_poni_dash__96c16f2f4669e8f7b7e7717dbda89411.gif)


#我咋用啊？
这是一个Python3模块，您可以使用'setup.py'来编译它以获得更好的性能（但不是很多），或者只使用'base64N.py'和'stdbase64.py'（请注意，如果您决定使用'setup.py'来编译该模块，请确保通过'pip3 install cython'和'Python3 setup.py build_ext --inplace`'来安装cython从而编译它）
base64N 是多次编码或解码base64的主要逻辑代码。
stdbase64.py`只是从Python 3.8.1的标准模块库中获取的'base64'模块(从winx64版本提取出来的)
要将它们导入到脚本中，请确保“base64N.py”和“stdbase64.py”这两个东西都还在（如果使用“setup.py”则为两个编译文件）位于同一文件夹中或安装在python模块库中。然后干就完了:import base64N


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
