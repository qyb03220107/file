#-*- coding:utf-8 -*-
db={}
promt = '''
    (N)注册用户
    (E)登陆用户
    (D)删除用户
    (S)查看用户
    (Q)退出
'''
while True:
    choice = input(promt).strip()[0].lower()
    print("请输入你的选择是:{}".format(choice))
    if choice not in "nedsq":
        print("你输入的无效！")
    else:
        if choice == "n":
            while True:
                name = input("请输入你的名字：")
                if db.get(name):
                    print("该用户存在，请重试！")
                    continue
                else:
                    break
            pwd = input("请输入你的密码:")
            db[name] = pwd
        elif choice == "e":
            name = input("请输入你需要登陆的名字:")
            pwd  = input("请输入你登陆用户的密码:")
            password = db.get('name')
            if password == pwd:
                print("登陆成功！")
            else:
                print("登陆失败！")
        elif choice == "s":
            value = db.keys()
            print("所有值如下{}".format(value))
        elif choice == "d":
            name = input("请输入你需要删除的用户:")
            get_name = 'name' in db
            print(get_name)
            if get_name == "False":
                db.pop('name')
                print("已经删除用户为{}".format(name))
            else:
                print("用户不存在！")
        else:
            print("退出！")
            break
