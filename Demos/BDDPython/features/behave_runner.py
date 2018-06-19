def getfiles():
    import glob

    mylist = [f for f in glob.glob("*.feature")]
    return mylist


if __name__ == '__main__':
    from behave import __main__ as behave_executable
    features = getfiles()
    behave_executable.main(features)