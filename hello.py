# Defines a "repeat" function that takes 2 arguments.
def repeat(s, exclaim):
    """Returns the string s repeated 3 times.
    If exclaim is true, add exclamation marks.
    """

    result = s + s + s # can also use "s * 3" which is faster (Why?)
    if exclaim:
        result = result + '!!!'
    return result


def main():
	print repeat('Happy', False)
	print repeat('Woo Hoo',True)

if __name__ == '__main__':
	main()