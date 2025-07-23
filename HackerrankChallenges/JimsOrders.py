def jimOrders(orders):

    customer = {idx+1: sum(item) for idx, item in enumerate(orders)}

    prep_time = sorted(customer.items(), key=lambda x: x[1])

    return [customer for customer, _ in prep_time]


if __name__ == '__main__':

    n = int(input())

    orders = []

    for i in range(n):
        orders.append(list(map(int, input().split())))

    result = jimOrders(orders)
    print(result)