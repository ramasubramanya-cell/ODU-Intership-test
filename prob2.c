/*Represent mathematical equations such as “(( 3 + 4) + 5) * 3” in an efficient data structure. 
For the next step, assume that the data is in the designed data structure, write helper functions to compute the result of the equation stored.#include <stdio.h>*/
//1.	If the character is operand push it to stack 
//2.	If the character is operator then pop two values from stack, make them child and push current node again

#include <ctype.h>
#define SIZE 50 /* Set size of Stack */

char s[SIZE];
int top = -1; /* beginning, stack is empty, so top points to -1 */
/* Function to Remove Spaces inbetween */
void RemoveSpaces(char* source) {
 char* i = source;
 char* j = source;
 while(*j != 0) {
 *i = *j++;
 if(*i != ' ')
 i++;
 }
 *i = 0;
}

/* Function for PUSH operation */
void push(char elem) { 
 s[++top] = elem;
}
/* Function for POP operation */
char pop() { 
 return (s[top--]);
}
/* Function for precedence */
int pr(char elem) { 
 switch (elem) {
 case '#':
 return 0;
 case '(':
 return 1;
 case '+':
 case '-':
 return 2;
 case '*':
 case '/':
 return 3;
 }
}

/* Function to convert from infix to postfix expression */
void infix_to_postfix(char *infix, char *postfix) {
 char ch, elem;
 int i = 0, k = 0;
 
 RemoveSpaces(infix);
 push('#');//base of stack has pound character 
 
 while ((ch = infix[i++]) != '\n') {
 if (ch == '(')
 push(ch);
 else if (isalnum(ch))
 postfix[k++] = ch;
 else if (ch == ')') {
    while (s[top] != '(')
    postfix[k++] = pop();
    elem = pop(); /* Remove ( */
 } 
 else { /* Operator */
    while (pr(s[top]) >= pr(ch))
    postfix[k++] = pop();
    push(ch);
 }
 }
 
 while (s[top] != '#') /* Pop from stack till empty */
 postfix[k++] = pop();
 
 postfix[k] = 0; /* Make postfix as valid string */
}

/* Function to evaluate a postfix expression */
int eval_postfix(char *postfix) {
 char ch;
 int i = 0, op1, op2;
while((ch = postfix[i++]) != 0) {
    if(isdigit(ch)) 
    push(ch-'0'); /* Push the operand */
    else { /* Operator,pop two operands */
    op2 = pop();
    op1 = pop();
    switch(ch) {
        case '+' : push(op1+op2); 
        break;
        case '-' : push(op1-op2); 
        break;
        case '*' : push(op1*op2);
        break;
        case '/' : push(op1/op2);
        break;
        }
    }
 }
 return s[top];
}

void main() { 
 
 char infx[50], pofx[50];
 printf("Enter an infix expression: ");
 fgets(infx, 50, stdin);
 
 infix_to_postfix(infx, pofx);

 printf("\nEntered Infix Expression: %sPostfix Expression: %s", infx, pofx);
 top = -1;
 printf("\nResult of postfix expression: %d", eval_postfix(pofx));
}
