
def get_item():
    items = [1,2,3,4]
    for item in items:
        yield item

for i in range(10):
    res = get_item()
    print(res)