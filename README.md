# 数据结构
### 数组和链表    
数组：连续，定长，不适合做插入删除等操作，可以直接通过下标进行访问  
打个形象的比方，停车场的每一排都可以看做一个数组，定长，连续，如果要插入停车，后面的每辆车都要移动位置，所以不适合做插入，直接追加很快  
python中的list与数组类似，但是长度可变，可视作动态的数组  
链表：不连续，不定长，适合做插入删除等操作，不可以直接通过下标访问（与数组正好相反）  
形象的比方：曲别针  
### 队列和栈  
队列：先进先出，只能从队列末尾插入数据，从队列头部取出数据  
形象的比方：食堂排队打饭  
[用python实现队列](py_queue.py)  
栈：后进先出，从末尾插入数据，从末尾取出数据  
形象的比方：硬币筒  
[用python实现栈](py_stack.py)  