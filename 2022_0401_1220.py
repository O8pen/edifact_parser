from lxml import html
import requests

page = requests.get('https://www.truugo.com/edifact/d07a/ordrsp/')
tree = html.fromstring(page.content)

view_message_El = tree.xpath('//div[@id="view-message"]')
unh_El = view_message_El[0].xpath('//a[@href="/edifact/d07a/unh/"]')
# view_message_El_String = html.tostring(view_message_El)  # '//*[@id="view-message"]'

# for x in view_message_El:
#     print(x[0].tag)

print(unh_El[0].attrib)
print("-------------------------------")
print(unh_El[0].base)
print("-------------------------------")
print(unh_El[0].nsmap)
print("-------------------------------")
print(unh_El[0].prefix)
print("-------------------------------")
print(unh_El[0].sourceline)
print("-------------------------------")
print(unh_El[0].tag)
print("-------------------------------")
print(unh_El[0].tail)
print("-------------------------------")
print(repr(unh_El[0].text_content()))
