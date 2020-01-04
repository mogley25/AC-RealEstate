import webbrowser
import mechanize
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
webbrowser.open(sub.geturl())