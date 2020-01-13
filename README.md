# AC-RealEstate
A simple python program to search street addresses on the Allegheny County PA Real Estate Website.
**This program will open the web browser you have set as default with the requested parcel info.**
http://www2.county.allegheny.pa.us/RealEstate/search.aspx
Running this is simple.
1. Download Python if you dont have it. https://www.python.org/downloads/
2. Open CMD as ADMIN and run ```pip install mechanize``` This installs the mechanize web browser python integration for the program to properly interact with websites.
3. Download and Double click RealEstate.py
4. Enter house number and press Return.
5. Enter street name and press Return. If it is a directional street, type the whole direction out. Ex. ```South Park``` NOT ```S Park```.
6. If you did it correctly, your browser should open up to the real estate website with your desired house info. If the address is invalid, the program will not open the browser and will tell you that you entered an invalid address and to try again.
7. Enjoy:)
