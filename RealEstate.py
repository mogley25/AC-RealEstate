import webbrowser
import mechanize
ans = True
validAddress = True
while ans == True and validAddress == True:
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent','Firefox')]
    br.open('http://www2.county.allegheny.pa.us/RealEstate/search.aspx')
    br.select_form(nr=0)
    HouseNum = int(input("Enter House number: "))
    StreetName = input("Enter Street Name: ")
    br.form['txtStreetNum'] = str(HouseNum)
    br.form['txtStreetName'] = str(StreetName)
    sub = br.submit()
    if sub.geturl() == 'http://www2.county.allegheny.pa.us/RealEstate/search.aspx':
        validAddress == False
        print("Address does not exist. Try again.")
        continue

    else:
        validAddress == True

    webbrowser.open(sub.geturl())

    question = input("Would you like to run again? y/n ")
    if question == 'y':
        ans = True
    else:
        ans = False
