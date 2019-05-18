def fizzbuzz(n):
    if not isinstance(n, int):
        raise TypeError('n is not intiger')
    if n <= 0:
        raise TypeError('n is not positive')
    if n % 15 == 0:
        return 'fizzbuzz'
    if n % 3 == 0:
        return 'fizz'
    if n % 5 == 0:
        return 'buzz'
    return str(n)
