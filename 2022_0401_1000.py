from lxml import html
import requests

page = requests.get('https://www.truugo.com/edifact/d07a/ordrsp/')
tree = html.fromstring(page.content)
view_message_El = tree.xpath('//div[@id="view-message"]')
# view_message_El_String = html.tostring(view_message_El)  # '//*[@id="view-message"]'

# for x in view_message_El:
#     print(x[0].tag)

print(view_message_El[0].attrib)
print("-------------------------------")
print(view_message_El[0].base)
print("-------------------------------")
print(view_message_El[0].nsmap)
print("-------------------------------")
print(view_message_El[0].prefix)
print("-------------------------------")
print(view_message_El[0].sourceline)
print("-------------------------------")
print(view_message_El[0].tag)
print("-------------------------------")
print(view_message_El[0].tail)
print("-------------------------------")
print(repr(view_message_El[0].text_content()))
