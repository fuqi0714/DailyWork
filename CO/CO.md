# 计算机概论
## 冯诺依曼的计算机结构特点
- 计算机硬件系统由运算器、存储器、控制器、输入设备和输出设备组成
- 指令和数据以等同的地位存储在存储器中，按地址寻访
- 指令和数据均以二进制表示
- 指令由操作码和地址码组成，操作码指出操作的类型，地址码指出操作数的地址
- 指令在存储器内按照顺序存放，通常情况下指令顺序执行；特定情况下可改变执行顺序
- 早期结构以运算器为中心，输入输出设备通过运算器与存储器进行数据传送

## 计算机性能指标
计算机的主要设备包括
- CPU
- 存储器
- 输入输出(IO)设备

影响计算机的性能指标主要取决于上述三类

# 二进制

## 定点数



| 符号位X<sub>0</sub> | 数值位X<sub>1</sub>~X<sub>n</sub> | 定点整数 | 定点小数 |
| :-----: | :----: | :----: | :----: |
| 0 | 均为1 | 原码可表示的最大正数2<sup>n</sup>-1 | 原码可表示的最大正数1-2<sup>-n</sup>  |
| 1 | 均为1 | 原码可表示的最小负数-(2<sup>n</sup>-1) | 原码可表示的最小负数-(1-2<sup>-n</sup>)  |


### 数值的表达方式
| 原码 | 反码 | 补码 | 移码 |
| :-----| :---- | :---- |:---- |
| 十进制数在计算机中的二进制表示形式，最高位为符号位：0代表为正数、1代表负数，但使用原码直接计算可能会导致结果错误 | 由原码转换而得，正数的原码以及反码一致；负数的话则除符号位外的所有数值位取反，解决负数加法运算问题，将减法运算转换为加法运算，从而简化运算规则 | 可由原码转换而得，正数的原码以及反码一致；负数则除符号位外的所有数值位取反并对最末位的数值加1。并且逢二进一(与十进制逢十进一的处理一致)，可把原码的相减操作转为补码的直接相加操作 | 常用于浮点数的阶码表示，对二进制数加上统一的值。在同一符号的基础上保证了原有数据的大小顺序，便于比较 |


### 基础公式
十进制数与二进制原码转换
- P21例2.2

补码加减法
- P28例2.12
- P29例2.14、2.15
    - [-y]<sub>补</sub>=-[y]<sub>补</sub>


### 溢出

运算结果超出数的表示范围，数的表示范围受可存放0/1的二进制位数影响

判断
- 双符号位判断：运算前将符号位的值扩展为两位(扩展后符号位的取值与原符号位相同)，并按照常规方式进行二进制加减。若最后双符号位的值相同则表示计算结果未溢出，相异则表示溢出
- 硬件电路判断：通过异或门的性质，设置溢出判断电路

## 浮点数
浮点数的规格化：通过移动二进制码的小数点，使得小数点后一位为有效值(另一种说法：尾数的最高位为有效值)。不同的二进制码类型规格化方式稍有不同，规格化的概念与十进制的科学计数法表示形式相似
- 原码规格化后，浮点数尾数最高位为1
- 补码规格化后，浮点数尾数最高位的值与尾数的符号位(数符)的值相反

浮点数计算
- P53例2.28

例:设有两个浮点数x=2<sup>Ex</sup>   * S<sub>x</sub>，y=2<sup>Ey</sup> * S<sub>y</sub>，Ex=(-10)<sub>2</sub>，Sx=(+0.1001)<sub>2</sub>，Ey=(+10)<sub>2</sub>，Sy=(+0.1011)<sub>2</sub>。若尾数4位，数符1位，阶码2位，阶符1位，求x+y并写出运算步骤及结果

流程
- 对阶
- 尾数计算
- 检查规格化
### 未统一表示形式的浮点数格式

二进制形式：N=2<sup>E</sup>×M，其中阶码和尾数选用何类二进制码表示以题目为准

| 阶符 | 阶码数值部分 | 数符 | 尾数数值部分 |
| :-----| :----: | :----: |:----: |
| 指数E的正负| E的绝对值部分 | M的正负 | M的绝对值部分 |


### 统一表示形式的浮点数格式IEEE 754(了解即可)

| 类型 | 数符位数 | 阶码位数(移码表示) | 尾数数值位数(原码表示) |总位数 |偏置值 |
| :-----| :----: | :----: |:----: |:----: |:----: |
| 单精度float| 1| 8|23|32|127 |
| 双精度double| 1 | 11|52|64 |1023|

[不同类型的表示范围](https://learn.microsoft.com/zh-cn/dotnet/csharp/language-reference/builtin-types/floating-point-numeric-types)
### 阶码有效范围(了解即可)
以8位为例,1(00000001) $\leq$ 阶码有效值 $\leq$ 254(11111110)
- 阶码有效值为0(00000000)代表非规格化数，阶码有效值255(11111111)代表无穷大



### 编码格式(了解即可)

| 符号位 | 阶码 | 尾数 | 表示 | 
| :-----| :----: | :----: |:----: |
| 0/1| 255| M $\neq$ 0|NaN|
| 0/1| 255| 0|+ $\infty$ , - $\infty$|
| 0/1| 1~254| M(正常规格化的情况)|(−1)<sup>S</sup>* (1.M) ×2<sup>(E−127)</sup>|
| 0/1| 0| M $\neq$ 0(无法规格化的情况)|(−1)<sup>S</sup>* (0.M) ×2<sup>(−126)</sup>|
| 0/1| 0| 0|+0，-0|

## 逻辑运算
| 操作数1 | 操作数2 | 与 | 或 | 异或 |
| :-----| :----: | :----: |:----: |:----: |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 0 | 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 1 | 0 |


## 乘除运算(了解即可)

### 原码一位乘法
计算规则
- 数值位取绝对值计算，最终结果的符号通过取两数符号进行异或运算决定
- 从乘数最低位开始，若最低位为1，部分积加上被乘数的绝对值后右移一位；若为0，则加上0后右移一位
    - 重复此操作，次数等于乘数的位数

|  乘数最低位(由于参与移位，每次相加操作后最低位发生变化)| 操作 |
| :-----| :----: |
| 0 | 部分积仅右移一位 |
| 1 | 部分积加上 $\vert X \vert $,之后右移一位 |

例：X=-13, Y=11, 数值位4位，符号位1位。计算X*Y 

$\vert X \vert $=1101 ， $\vert Y \vert $=1011

| 操作 |  部分积的高位| 部分积的低位/乘数| 舍弃部分 | 根据乘数最低位的值按照计算规则进行操作|
| :-----| :-----| ----: | :---- |:---- |
| 初始状态，进行比较| 00,0000| 101<font color="#dd0000">1</font> | <font color="#dd0000"></font> |按照计算规则对比乘数最低位的值。此时部分积加上 $\vert X \vert $,之后右移一位 |
| 加上 $\vert X \vert $| 00,1101| | <font color="#dd0000"></font> ||
| 结果| 00,1101| 101<font color="#dd0000">1</font> | <font color="#dd0000"></font> ||
| |  |  |  |相加操作结束 |
| 右移| 00,0110| 110<font color="#dd0000">1 </font>| 1  | 移位作用于整个积(高位积和低位积) |
| |  |  |  |右移一位操作结束 |
| 比较| 00,0110| 110<font color="#dd0000">1 </font>| 1  |部分积加上 $\vert X \vert $,之后右移一位 |
| 加上 $\vert X \vert $| 00,1101|  |  ||
| 结果| 01,0011| 110<font color="#dd0000">1</font> | 1 ||
| |  |  |  |相加操作结束 |
| 右移| 00,1001| 111<font color="#dd0000">0 </font>| 11  | 移位作用于整个积(高位积和低位积) |
| |  |  |  |右移一位操作结束 |
| 比较| 00,1001| 111<font color="#dd0000">0 </font>| 11  |仅右移一位 |
| 加上0| 00,0000| |   | |
| 结果| 00,1001| 111<font color="#dd0000">0 </font>| 11  | |
| |  |  |  |相加操作结束 |
| 右移| 00,0100| 101<font color="#dd0000">1 </font>| 011  | 移位作用于整个积(高位积和低位积) |
| |  |  |  |右移一位操作结束 |
| 比较| 00,0100| 111<font color="#dd0000">1 </font>| 011  |仅右移一位 |
| 加上 $\vert X \vert $| 00,1101|  |  ||
| 结果| 01,0001| 111<font color="#dd0000">1 </font>| 011  | |
| 右移| 00,1000| 111<font color="#dd0000">1 </font>| 1011  |移位作用于整个积(高位积和低位积) |
| 得出结果| <u>00,1000</u>| <u>111<font color="#dd0000">1 </font></u>| 1011  |下划线部分为二进制原码绝对值 |

X、Y的符号进行异或运算：0 $\bigoplus$ 1=1
### 补码一位乘法
计算规则
- 符号位与数值位共同参与运算，被乘数取双符号位，乘数取单符号位
- 乘数末尾后增加一个辅助判断位，初值为0
- 对比乘数原末尾和辅助判断位的值，按照下表操作
    - 移位产生的补位需要符合补码性质
    - 重复移位-相加的操作直到乘数的符号位出于最末尾，此时根据下表内容做最后一次加法。将结果拼接得出最后的补码结果

|  乘数最低位(由于参与移位，每次相加操作后最低位发生变化)| 辅助位 | 操作 |
| :-----| :----: | :----: |
| 0 | 0 | 部分积仅右移一位 |
| 0 | 1 | 部分积加上[X]<sub>补</sub>,之后右移一位 |
| 1 | 0 | 部分积加上[-X]<sub>补</sub>,之后右移一位 |
| 1 | 1 | 部分积仅右移一位 |

例：X=-27, Y=13, 数值位5位，符号位1位，被乘数使用双符号位，乘数使用单符号位。计算X * Y

[X]<sub>原</sub>=11,11011, [X]<sub>补</sub>=11,00101, [-X]<sub>补</sub>=00,11011, [Y]<sub>原</sub>=[Y]<sub>补</sub>=00,01101
| 操作|  部分积的高位| 部分积的低位/乘数| 辅助位 | 根据辅助位红色字符与乘数位红色字符的组合，按照计算规则操作 |
| :-----| :-----| ----: | :---- |:----|
| 初始状态，进行比较| 00,00000| 0,0110<font color="#dd0000">1</font> | <font color="#dd0000">0</font> |辅助位初始上0，按照计算规则对比两位的组合。此时部分积先加上[-X]<sub>补</sub>,之后右移一位 |
| 加上[-X]<sub>补</sub>| 00,11011|  |  ||
| 结果| 00,11011|  |  | |
| |  |  |  |相加操作结束 |
| 右移| 00,01101| 10,0110 |  | 移位作用于整个积(高位积和低位积) |
| |  |  |  |右移一位操作结束 |
| 比较| 00,01101| 10,011<font color="#dd0000">0</font> | <font color="#dd0000">1</font>0 |部分积加上[X]<sub>补</sub>,之后右移一位 |
| 加上[X]<sub>补</sub>| 11,00101|  |   |
| 结果| 11,10010|  |   |
| |  |  |  |相加操作结束 |
| 右移| 11,11001| 10,0110 |  | 移位作用于整个积(高位积和低位积) |
| |  |  |  |右移一位操作结束 |
| 比较| 11,11001| 010,01<font color="#dd0000">1</font> | <font color="#dd0000">0</font>10 |部分积加上[-X]<sub>补</sub>,之后右移一位 |
| 加上[-X]<sub>补</sub>| 00,11011|  |   |
| 结果| 00,10100|  |   |
| |  |  |  |相加操作结束 |
| 右移| 00,01010| 0010,01 |  |移位作用于整个积(高位积和低位积) |
| |  |  |  |右移一位操作结束 |
| 比较| 00,01010| 0010,0<font color="#dd0000">1</font> | <font color="#dd0000">1</font>010 |部分积仅右移一位 |
| 加上0| 00,00000|  |   |
| 结果| 00,10100|  |   |
| |  |  |  |相加操作结束 |
| 右移| 00,00101| 00010,0 |  |移位作用于整个积(高位积和低位积)  |
| |  |  |  |右移一位操作结束 |
| 比较| 00,00101| 00010,<font color="#dd0000">0</font> | <font color="#dd0000">1</font>1010 |部分积加上[X]<sub>补</sub>,之后右移一位 |
| 加上[X]<sub>补</sub>| 11,00101|  |   |
| 结果| 11,01010|  |   |
| |  |  |  |相加操作结束 |
| 右移| 11,10101| 00001<font color="#dd0000">0</font>, | <font color="#dd0000">0</font>11010 |部分积仅右移一位 |
| 得出结果| <u>11,10101</u>| <u>00001</u><font color="#dd0000">0</font>, | <font color="#dd0000">0</font>11010 |下划线部分为计算结果的二进制补码 |







### 原码一位除法

计算规则
- 数值位取绝对值计算，最终结果的符号通过取两数符号进行异或运算决定
- 先用被除数减去除数，当余数为正时商上1，余数和商左移一位再减去除数；当余数为负，商上0，余数和商左移一位，再加上除数
    - 当第n+1次相加/减后的余数为负时，需加上$\vert Y \vert  $得到第n+1步正确的余数
        - 最后操作使余数与被除数同号


例：X=0.1011, Y=0.1101, 数值位4位，符号位1位。计算X/Y 


$\vert X \vert $=0.1011, $\vert Y \vert $=0.1101, 

 ($\vert X \vert $)<sub>补</sub>=0.1101, ( - $\vert Y \vert $)<sub>补</sub>=1.0011

![](https://github.com/fuqi0714/DailyWork/blob/main/CO/res/YD.png)

X、Y的符号进行异或运算：0 $\bigoplus$ 0=0， X/Y=+0.1101, 余数为0.0111*2<sup>-4</sup>

### 补码一位除法

计算规则
- 符号位与数值位共同参与运算，被除数取双符号位，除数取单符号位
- 先判断除数与被除数同号，用被除数减去除数；若异号，被除数加上除数
- 根据上一步计算结果，若被除数与除数同号，商上1，之后余数左移一位减去除数；异号则商上0，余数左移一位加上除数
    - 重复执行n次

例：X=0.1000, Y=-0.1011, 数值位4位，符号位1位。用补码除法计算X / Y

符号位两位，[X]<sub>原</sub>=00.1000, [X]<sub>补</sub>=00.1000,  [Y]<sub>原</sub>=11.1011, [Y]<sub>补</sub>=11.0101, [-Y]<sub>补</sub>=00.0101

![](https://github.com/fuqi0714/DailyWork/blob/main/CO/res/BD.png)

[X/Y]<sub>补</sub>=1.0101, 余数为0.0111*2<sup>-4</sup>




# 存储器
## 只读存储器
| MROM| PROM | EPROM | Flash Memory | Solid State Drives |
| :-----: | :-----: | :----: | :----: | :----: | 
| 掩膜式只读存储器 | 一次可编程只读存储器 | 可擦除可编程只读存储器 | 闪速存储器 | 固态存储器 | 
| 生产过程中直接写入，写入后无法修改内容 | 生产不含内容的只读存储器，允许用户利用编程设备自由写入。写入后内容无法修改 | 不仅允许用户自由写入，还允许对存储器上的内容全部擦除重新编程写入新数据。分为光擦除和电擦除两类 | 在EPROM的基础上发展，可长期保存数据，擦除与重写的速度快 | 在Flash的基础上发展，整体性能更优异 |  





## 随机存储器
### SRAM&DRAM

| 类型| SRAM | DRAM | 
| :-----: | :-----: | :----: | 
| 存储结构| 组合式电容固件触发器 | 单个电容固件 | 
| 破坏性读出| 否 | 是 | 
| 读出数据后是否需要重新生成信息| 否 | 是 | 
| 运行速度| 快 | 慢 | 
| 工艺| 复杂 | 简单 | 
| 制作成本| 高 | 低 | 
| 是否易失| 是 | 是 | 


### 2-4译码器
根据此结构可发展结构更丰富的3-8译码器、4-16译码器
| | 输入电信号 | 电信号保持 | 电信号取反 !A<sub>x</sub> | 
| :-----: |:-----: | :----: | :----: |
| A<sub>0</sub> | 0 | 0 | 1 | 
| A<sub>1</sub> | 1 | 1 | 0 | 
| A<sub>0</sub> | 1 | 1 | 0 | 
| A<sub>1</sub> | 0 | 0 | 1 | 



| 输入端电信号1 | 输入端电信号2 | 逻辑与 | 等于 | 输出端电信号 | 
| :-----: | :-----: | :----: | :----: | :----: |
| !A<sub>1</sub> | !A<sub>0</sub> | & | → | Y<sub>0</sub> |
| !A<sub>1</sub> | A<sub>0</sub> | & | → | Y<sub>1</sub> |
| A<sub>1</sub> | !A<sub>0</sub> | & | → | Y<sub>2</sub> |
| A<sub>1</sub> | A<sub>0</sub> | & | → | Y<sub>3</sub> | 


## 多模块存储器
模块的含义：多个单张存储芯片按照某种方式编一个独立的单位，该模块内的存储单元数等于多个芯片的存储单元总数

存储器容量：主存内以模块为基本单位或者以单张芯片为基本单位，多个基本单位具有的存储单元总数为该存储器的容量

例1：机器字长为16位的计算机存储容量为2MB，若按字节编址，存储单元寻址范围为多少
- 若按字长编址，存储单元寻址范围为多少



例2：机器字长为16位的计算机的主存结构采用半导体存贮器，地址码长度20位，按字节编址，若使用8K×8位的RAM芯片组成该计算机所允许的最大主存空间，并使用模块条的形式，则
- 若每个模块条为256K×8位，共需几个模块条？
- 每个模块内共有多少片RAM芯片？
- 主存共需多少RAM芯片？
### 模块设计方式
顺序方式

交叉方式


# 指令
## 寻址方式
P128-P130

## 指令和数据
指令和数据都是以二进制的形式存放在存储器中。存储器存储的内容本身无法反映是指令还是数据，因为它们都是二进制代码。计算机在读取指令阶段把从存储器中读到的信息都看作是指令，而在分析指令后的执行阶段则把从存储器中读到的信息都看作是操作数数据。所以为了不产生混乱，在进行汇编程序设计时要注意区分存储器中的信息是程序还是数据，而用高级语言设计程序一般不会产生上述问题。

# CPU
## CPU的组成
### 主要寄存器
数据缓冲寄存器Data Register

指令寄存器Instruction Register

程序计数器Program Count

数据地址寄存器Address Register

通用寄存器Register

程序状态字寄存器Program Status Word Register

# 总线
## 总线内部结构

| 地址线| 数据线 | 控制线 | 
| :-----: | :-----: | :----: | 
| 单向传输 | 双向传输 | 双向传输 | 
| 指定主存和 I / O 设备接口电路的地址 | 对应主存单元内的读写操作 | 传输分析指令所得的电信号并控制硬件执行 | 


## 总线传送方式
串行传送、并行传送、分时复用传送
## 总线仲裁方式
集中式仲裁、分布式仲裁
