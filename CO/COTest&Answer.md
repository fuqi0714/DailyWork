
1、下列带符号位的数中，最小的数_____

A.补码101001&ensp;     B.(465)<sub>8</sub>&ensp;      **<font color="#660000">C.D4E1H&ensp;**   </font>    D.原码0.101101 

**<font color="#660000">二进制原码依次为110111、100110101、1101010011100001、0.101101</font>**

2、C7E5H和D4D3H相加结果为**19CB8**

3、5D2FH转为八进制的结果为**56457**

**<font color="#660000">二进制为0 101 110 100 101 111，从左至右三个二进制位计算得出一个八进制位数056457</font>**

4、一个10位无符号二进制数的表示范围为_________

**<font color="#660000">2<sup>10</sup>为1024，表示范围从0~1023</font>**

5、计算机主频为1.2GHz，指令分为4类，在基准程序所占比例及CPI如表。此计算机的MIPS数为_____
| |  |  |  |  |
| :-----| :----: | :----: |:----: |:----: |
| 指令类型| A | B | C | D |
| 所占比例| 50% | 20% | 10% | 20% |
| CPI| 2 | 3 | 4| 5 |

**CPI=0.5 * 2+0.2 * 3+0.1 * 4+0.2 * 5=3，MIPS=主频/CPI=400**

6、某程序在本机上的执行时间为20秒，优化程序结构后的指令数量减少到原来的70%，CPI增加到原来的1.2倍。则优化后的程序在本机的执行时间为**CPI * I<sub>指令数</sub> * t<sub>时钟周期</sub> * 0.84**

**CPI=m<sub>时钟周期数</sub></sub>/I<sub>指令数</sub>，T<sub>执行时间</sub>=m<sub>时钟周期数</sub> * t<sub>时钟周期</sub>=CPI * I<sub>指令数</sub> * t<sub>时钟周期</sub>**

7、冯诺依曼结构计算机中采用二进制编码表示的原因

**<font color="#660000">A.二进制运算规则简单&ensp;&ensp;&ensp; B.两个状态稳定的物理器件易于制作&ensp;&ensp;&ensp; C.通过逻辑电路可以实现信息表示和运算</font>**

8、若[X]<sub>补</sub>=1，1101101，则[X]<sub>原</sub>为**1，0010011**

9、[X]<sub>原</sub>为1101 1011，则[-X]<sub>补</sub>为**1101 1011**

10、8位原码可以表示的数据范围为 **-128~127**

11、n位定点整数(带符号位)表示的最大值为**2<sup>n-1</sup>-1**

**<font color="#660000">n位二进制序号0~n-1, 则n-2、n-3......直到0位全为1并把结果相加则为数值的最大值，最大值加上1的结果等于2<sup>n-1</sup>，因此最大值可得出为2<sup>n-1</sup>-1</font>**

12、当[X]<sub>补</sub>=1.xxxxxx,若X<-1/2，则多个x表示的取值范围为___________

**<font color="#660000">[X]<sub>补</sub>为负数，[-1/2]<sub>补</sub>为1.1000， 符号位相同则数值位越大则绝对值越大，因此第一个x为0，后续x取值可任意</font>**


13、若定点小数[X]<sub>补</sub>=X<sub>0</sub>.X<sub>1</sub>X<sub>2</sub>......X<sub>n</sub>运算时采取双符号位形式，则符号位X<sub>0</sub>与X<sub>1</sub>的关系为_________________时，补码左移将发生溢出

**<font color="#660000">双符号位溢出判断：运算后双符号位的值不相等则溢出，因此当X<sub>0</sub> $\not=$ X<sub>1成立</sub></font>**


14、由3个1和5个0组成的8位二进制补码能表示的最小整数为 **-125**

**<font color="#660000">补码数值位的位数为1越多，则结果越大。表示最小整数只需符号位取1，低位尽量取1即可1,0000011</font>**

15、用补码表示有符号整数，若int变量x、y的机器数(十六进制数)分别为FFFF FFDFH和0000 0041H，则x为 **-33**，y为**65**，x-y的机器数(十六进制数)为**FFFF FF9EH**

16、机器字长为32位的计算机，C语言程序在该机器上定义三个int型变量x、y、z，当x=127、y=-9时执行赋值语句z=x+y后，x、y、z的值用十六进制表示分别为__________________________________

**<font color="#660000">二进制通常以补码形式存储，int长度为32位，因此x=0 0 0 0 0 0 0111 1111=0000 007FH、y=1 1 1 1 1 1 1 0111= FFFF FFF7H、z=x+y，简写为007FH+FFF7H。7+F=22，16进1，低位值为6。z=0000 0076H </font>**

17、有4个整数r<sub>1</sub>=FEH、r<sub>2</sub>=F2H、r<sub>3</sub>=90H、r<sub>4</sub>=F8H存储于计算机中，若将任意两个整数的计算结果存储于8位二进制中，则发生溢出运算符与操作数为 **r<sub>1</sub> * r<sub>3</sub>、r<sub>2</sub> * r<sub>3</sub>、r<sub>4</sub> * r<sub>3</sub>**

**<font color="#660000">8位二进制的取值范围为-128~+127，r<sub>1</sub>=-2、r<sub>2</sub>=-14、r<sub>3</sub>=-112、r<sub>4</sub>=-8</font>**

18、C语言中的int长度为32位，short长度为16位。若执行下列命令得到y的机器数(十六进制数)为**0000 FFFAH**

    unsigned short x=65530;
    unsigned int y=x;

**<font color="#660000">unsigned short长度为16位，unsigned int长度为32位。位数少转为位数多则在高位补0，16位无符号数取值范围为0~65535(FFFFH)。x的部分十六进制值为FFFFH-5H=FFFAH</font>**

19、补码定点整数[X<sub>补</sub>]=11010101左移两位后的值为**11010100**
- [X<sub>补</sub>]右移三位后的值为**11111010**

正数算数移位规则
| 码制 | 左移 | 右移 | 
| :-----: | :----: | :----: |
| 原/补/反 | 补0 | 补0 |

负数算数移位规则
| 码制 | 左移 | 右移 | 
| :-----: | :----: | :----: |
| 原 | 补0 | 补0 |
| 补 | 补0 | 补1 |
| 反 | 补1 | 补1 |


20、8位二进制定点整数，补码表示的最小值为 **-128**



21、二进制位为8位，原码机器数(十六进制数)BAH左移一位和右移一位的值分别为_________

**<font color="#660000">原码二进制为1011 1010，左移为1111 0100(F4H)，右移为1001 1101(9DH)</font>**

- 若为补码，左移一位和右移一位的值分别为_________

**<font color="#660000">补码二进制为1011 1010，左移为1111 0100(F4H)，右移为1101 1101(DDH)</font>**

22、x=103，y=-25，8位定点补码运算结果为溢出的运算符与操作数为**x-y**

**<font color="#660000">8位二进制的取值范围为-128~+127</font>**

23、按照IEEE 754标准将float型变量x存储于32位二进制中，若x=-8.25，则存储结果用16进制表示为______________

**X原=-1000.01=-1.00001 * 2<sup>3</sup>，阶码E=127+指数e=130，阶码二进制为10000010.根据IEEE 754标准形式为1 1000 0010 0000 1000 0000 0000 0000 000，十六进制为C1040000H**

24、在对阶操作的过程中，阶码和尾数的变换关系为_______________________________________________________

25、IEEE 754标准下的浮点数为C6400000H，则结果为 **-1.5 * 2<sup>13</sup>**

**<font color="#660000">二进制为1100 0110 0100 0000 0000 0000 0000 0000，数符为1，阶码为1000 1100-127=0000 1101 =13，尾数为1.5</font>**

26、IEEE 754标准下两个float变量x、y分别为CC900000H、B0C00000H，x、y之间的大小关系为______________

**X二进制为1100 1100 1001 0 0 0 0 0，y二进制为1011 0000 1100 0 0 0 0 0。数符都为1则两数都为负数，x阶码10011001，指数e=10011001 -127=26；y阶码01100001，指数e=01100001-127=-30。则x=-1.001 * 2<sup>26</sup>，y=-1.1 * 2<sup>-30</sup>**

27、浮点运算中，下溢表示____________________________

28、在IEEE 754标准下，浮点数的结构与位数为______________

| 类型 | 数符位数 | 阶码位数 | 尾数数值位数 |总位数 |偏置值 |
| :-----| :----: | :----: |:----: |:----: |:----: |
| 单精度float| 1| 8|23|32|127 |
| 双精度double| 1 | 11|52|64 |1023|

29、IEEE 754标准下尾数的二进制编码格式为**原码**

30、对于机器数(十六进制数)C8000000H，在类型为int以及IEEE 754标准下的float表示下，代表的值分别为 **-7 * 2<sup>27</sup>**

**<font color="#660000">二进制为1100 1000 0 0 0 0 0 0 ，int类型下为补码，最高位为符号位，数值位取反+1，结果为1,011 1000 0 0 0 0 0 0**

**float类型下，数符为1则表示负数，阶码为1001 0000，指数e=1001 0000-127=17</font>**