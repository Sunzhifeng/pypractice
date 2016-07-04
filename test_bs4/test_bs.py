from bs4 import BeautifulSoup as BS

def get_element_index(elt):
     count = 1;
     for sib in elt.previous_siblings:
         if sib.name == elt.name:
             count = count + 1
     return count

def get_element_xpath(root, element):
    path = ''
    index = get_element_index(element)
    name = element.name
    if index > 1:
        name = name + "[" + str(index) + "]"
        path = '/' + name + path
    else:
        path = '/' + name
    for elt in element.parents:
        xname = elt.name
        index = get_element_index(elt)
        if index > 1:
            xname = xname + "[" + str(index) + "]"
        path = '/' + xname + path
        if root.name == xname:
            break
    path = '/' + path if root.name != 'html' else path
    return path

def get_parents(root, element):
    parents = []
    for ele in element.parents:
        parents.append(ele)
    if root in parents:
        root_index = parents.index(root)
        return parents[0: root_index+1]
    else:
        raise TypeError('%s has no parent called %s' % (element.name, root.name))

soup = BS(open('index.html'), 'html5lib')
table = soup.table
body = soup.body
button = soup.button
html = soup.html
xpath = get_element_xpath(html, button)
print xpath
