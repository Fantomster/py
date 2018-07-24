name_for_userid = {
    382: 'Alice',
    950: 'Bob',
    590: 'Dilbert',
}

# Non Pythonic way
# def greeting(userid):
#     if userid in name_for_userid:
#         return 'Hi %s!' % name_for_userid[userid]
#     else:
#         return 'Hi there!'

# More Pythonic way
def greeting(userid):
    try:
        return 'Hi %s!' % name_for_userid[userid]
    except KeyError:
        return 'Hi there!'

# Pythonic way
def greeting1(userid):
    return 'Hi %s!' % name_for_userid.get(userid, 'there')

print(greeting1(382))
print(greeting1(3821))