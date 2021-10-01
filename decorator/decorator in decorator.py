def header(func):
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')
    return inner


def table(func):
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')
    return inner


# title = table(header(title))
@table
@header
def title(author, company, year):
    print(f"{author} - {company}. {year} year")


title('Mikhail', 'sbkits', '2021')

# <table>
# <h1>
# Mikhail - sbkits. 2021 year
# </h1>
# </table>
