
def is_happy_ticket(ticket):
    half = len(ticket)//2
    first = [int(i) for i in ticket[:half]]
    second = [int(i) for i in ticket[half:]]
    return True if sum(first) == sum(second) else False


def test_is_happy_ticket():
    assert is_happy_ticket('0110')
    assert is_happy_ticket('341800')

    assert not is_happy_ticket('0010')
    assert not is_happy_ticket('12345678')
