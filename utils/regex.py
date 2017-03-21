import re

# user_input ="beata1223.123.hd@gm1a2il.do2"
user_input ="www.github.com/bexpe/dojo-flask.git"
# user_input ="Maedhbahdb-jsndjd"


def email_validation(user_input):
    if not re.match(r'^[A-Za-z0-9-]+(\.[a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', user_input):
        # lower and upper-case, dotes and numbers allowed before @, dotes and numbers allowed after @ but no upper-case!
        # after . not allowed upper- case in the end but .edu.com allowed!
        print(user_input + ' not allowed')
        return False
    print(user_input + '  allowed')
    return user_input


def is_empty(user_input):
    if re.match(r'^\s*$', user_input):  # don't allow empty user_input or input with only white spaces
        return False
    return user_input


def delete_white_spaces_between(user_input):
    user_input = re.sub("\s\s+", " ", user_input)  # if its more than two spaces between words or at the beginning and
    # in the and of user_input, then they're changed for one space
    return user_input


def ignoring_scripts(user_input):
    if re.search(r'<script.*?>', user_input):  # don't allow scripts in all user_input even between some different words
        return False
    return user_input


def name_surname_validation(user_input):
    regex = re.compile(r'(^[A-Z])+(-[^\W_]+)?([a-z]{2,})?(\-)([a-z]{2,})$', re.U)  # Upper-case at the beginning
    # required, one - allowed but without empty spaces!!! eg Catherine-Meg, no numbers allowed,
    # no upper-case at the end of a string allowed

    if  not regex.match(user_input):
        print(user_input+'  not allowed')
        return False
    return user_input


def submit_link(user_input):
    if user_input.startswith('http'):
        if not re.match(r'^(http|https)://(.+)\.(.+)', user_input):  # looking for http/s on the beginning with // and:
            return False

        k = re.match(r'^(http|https)://(.+)\.(.+)', user_input)  # assigning to variable k this matching regex
        link_name = 'assignment_link'
        user_input = re.sub(r'^(http|https)://(.+)\.(.+)', '<a href = "' + k.string + '">' + link_name + '</a>',
                            user_input)  # swapping a link for a html url with href
        return user_input


    elif user_input.startswith('www'):
        if not re.match(r'^www.(.+)\.(.+)$', user_input):  # looking for www. on the beginning
            return False

        k = re.match(r'^www.(.+)\.(.+)$', user_input)  # assigning to variable
        link_name = 'assignment_link'
        user_input = re.sub(r'^www.(.*)\.(.*)', '<a href = "http://' + k.group(1) + '.' + k.group(2) + '">' +
                            link_name + '</a>', user_input)
        print(user_input)
        return user_input



    # user_input = re.sub(r'<.*?>', ' ', user_input, 0, re.DOTALL)  # ignoring html tags


# name_surname_validation(user_input)
# email_validation(user_input)
submit_link(user_input)
