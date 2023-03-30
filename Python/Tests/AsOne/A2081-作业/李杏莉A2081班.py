#include<stdlib.h>
#include<stdio.h>

typedef struct LNode{
	int data;
	struct LNode* next;
}LNode,*LinkList;

LNode* create(int data[], int n){
	LNode* head, * rear, * p;                              
	head = (LNode*)malloc(sizeof(LNode));
	head->next = NULL;
	rear = head;
	for (int i = 0; i < n; i++)
	{
		p = (LNode*)malloc(sizeof(LNode));
		p->data = data[i];
		p->next = NULL;
		rear->next = p;
		rear = p;
	}
	return head;
}

void show(LNode* head) {
	LNode* p;
	p = head->next;
	while (p)
	{
		printf("%d", p->data);
		p=p->next;
	}
	printf("\n");
}

//删除值为a的节点
bool dlt(LNode* head,int a) {
	if (head->next==NULL)
	{
		return false;
	}
	LNode* p = head;
	LNode* r;
	while (p)
	{	//没有这个if的话，下面的if会报错？
		if (p->next==nullptr)
		{
			return false;
		}
		if (p->next->data == a) {
			r = p->next;
			p->next = r->next;
			free(r);
			r = NULL;
		}
		p = p->next;
	}
	return true;
}

int main() {
	int data[10] = { 1, 2, 3, 4, 5, 1, 2, 3, 4, 5 };
	LNode* head = create(data, 10);
	dlt(head,3);
	show(head);
	return 0;
}
