def discount_calculator(price,discount):
    return price - (price*discount/100)

def test_10_percent_discount():
    assert discount_calculator(200, 10) ==180
def test_0_percent_discount():
    assert discount_calculator(200, 0) ==200
def test_0_percent_discount():
    assert discount_calculator(200, 100) == 0
