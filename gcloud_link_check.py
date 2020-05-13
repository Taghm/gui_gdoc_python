#code to get a web link
import webbrowser

z = '<a class="gb1" href="https://mail.google.com/mail/?tab=wm">Gmail</a>'

def check_link(a):
    a_link1 = a.split("href=")
    a_link2 = a_link1[1]
    a_link3 = a_link2.split(">")
    a_link4 = a_link3[0]
    a_link5 = a_link4[1:-1]
    return a_link5


def main():
    print(check_link(z))
    webbrowser.open(check_link(z))

#run main
if __name__ == "__main__":
    main()
