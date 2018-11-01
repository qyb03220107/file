#! -*-  coding:utf-8-*-
db = {}
prompt = '''
    (N)注册用户
    (E)登陆用户
    (Q)退出
    请选择：
'''
def newuser():
    while True:
        name = input("请输入用户名:")
        if db.get(name):
            print("用户名存在，请重试！")
            continue
        else:
            break
    pwd = input("请输入密码:")
    db[name] = pwd
def olduser():
    name = input("请输入用户名:")
    pwd  = input("请输入密码:")
    passwd = db.get(name)
    if pwd == passwd:
        print("登陆成功")
    else:
        print("失败！")
while True:
    choice = input(prompt).strip()[0].lower()
    print("请输入你的选项:".format(choice))
    if choice not in "neq":
        print("请重试！")
    else:
        if choice == 'n':
            newuser()
        elif choice == 'e':
            olduser()
        else:
            print('退出')
            break