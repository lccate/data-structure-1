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
### 树  
计算机科学中的树可以看过倒挂的树，根在上，分支在下  
![树示意图](1.png)  
从图中看，1节点就是根节点，从1分叉出了2,3,4节点  
2,3,4是1的孩子节点  
2,3,4互为兄弟节点  
1为2,3,4的父节点  
这棵树的深度为4（一共4层）  
多棵树组成森林  
#### 常用的树：二叉树（每个节点最多有2个子节点）  
![二叉树示意图](2.png)  
遍历：  
前序遍历（根左右）{1,2,5,6,3,7,8,9}  
中序遍历（左根右）{5,2,6,1,8,7,9,3}  
后序遍历（左右根）{5,6,2,8,9,7,3,1}  
[用python实现二叉树前序遍历](py_tree.py)  
### 排序   
#### 插入排序  
类似于打牌时整理手牌的过程  
#### 冒泡排序  
第一个和第二个比，大的往后排（或者往前排），以此类推，一直到队尾  
#### 快速排序  
最经典的排序方法
