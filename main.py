from dummyio import DummyIOPlugin

if __name__ == '__main__':

    plugin = DummyIOPlugin("64ca1a4a578a3b943f1c0520")
    plugin1 = DummyIOPlugin("j")

    # connectivity check
    print("checking with correct app-id:")
    plugin.check_connection()
    print("checking with fake app-id:")
    plugin1.check_connection()

    # getting user list
    for page_number in range(5):
        plugin.user_list(10, page_number)
    print("Getting all users completed")

    # getting post list
    plugin.post_list()
    print("Getting posts and comments completed")
