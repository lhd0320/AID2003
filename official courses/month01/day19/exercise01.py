def verif_permissions(func):
    def wrapper(*args,**kwargs):
        print("验证权限")
        return func(*args,**kwargs)
    return wrapper


# def verif_permissions():
#     print("验证权限")
@verif_permissions
def enter_background():
    print("进入后台")

@verif_permissions
def delete_order():
    print("删除订单")

enter_background()