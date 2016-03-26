import decimal

def infix2postfix(exp):
    '''中缀表达式转后缀表达式'''
    postfix=[]      #存储后缀表达式
    stack=['#']     #存储操作符
    pro={'#':0,'(':1,'+':2,'-':2,'*':3,'/':3,'^':4,'%':4,'~':4,')':5} #操作符优先级
    number_str_list = [] #操作数字符

    for token in exp:
        if token=='(':
            stack.append(token)
        elif token==')':

            number_str = ''.join(number_str_list)
            postfix.append(number_str)
            number_str_list = []

            while stack[-1]!='(':
                postfix.append(stack.pop())
            stack.pop()

        elif token in ['/','*','+','-','^','%','~']:
            if number_str_list != []:

                number_str = ''.join(number_str_list)
                postfix.append(number_str)
                number_str_list = []

            while pro[stack[-1]]>=pro[token]:
                postfix.append(stack.pop())
            else:
                stack.append(token)
        else:
            number_str_list.append(token)

    if number_str_list != []:
        number_str = ''.join(number_str_list)
        postfix.append(number_str)


    postfix.extend(stack[:0:-1])

    return postfix


def getTotalofPostfix(exp):
    '''求后缀表达式的值'''
    stack=[]
    operator={
        '+':lambda x,y:x+y,
        '-':lambda x,y:y-x,
        '*':lambda x,y:x*y,
        '/':lambda x,y:y/x,
        '%':lambda x,y:y%x,
        '~':lambda x,y:y**(1/x),
        '^':lambda x,y:y**x
    }

    for token in exp:
        if token in ['+','-','*','/','^','%','~']:
            if len(stack)==1:
                x=0
                y=decimal.Decimal(stack.pop())
                stack.append(operator[token](0,y))
            else:
                x=decimal.Decimal(stack.pop())
                y=decimal.Decimal(stack.pop())
                stack.append(operator[token](x,y))
        else:
            stack.append(token)
    return stack[0]

def calculate(exp):
    result =  getTotalofPostfix(infix2postfix(exp))
    if int(result) == result:
        return int(result)
    return result

if __name__=='__main__':
    exp_list=["(1.2+2)*3-(4-5)*(6+7)",'1+2*3/4+5/6','(1+2*3)']
    for total in map(calculate,exp_list):
        print(total,end='\n\n')

