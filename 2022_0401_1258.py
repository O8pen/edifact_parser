from lxml import html
import requests

page = requests.get('https://www.truugo.com/edifact/d07a/ordrsp/')
tree = html.fromstring(page.content)

view_message_divs = tree.xpath('//div[@id="view-message"]/div')
print(len(view_message_divs))
# unh_El = view_message_El[0].xpath('//a[@href="/edifact/d07a/unh/"]')
# unh_El = view_message_divs[0].xpath('//a[@href="/edifact/d07a/unh/"]')

for view_message_div in view_message_divs:

    aggr_seg_h3s = view_message_div.xpath('/h3')
    aggr_seg_divs = view_message_div.xpath('/div/div[1]/div')

    for x in aggr_seg_divs:
        print(repr(x.text_content()))
        print("-------------------------------")

    # print(x.attrib)
    # print("-------------------------------")
    # print(x.base)
    # print("-------------------------------")
    # print(x.nsmap)
    # print("-------------------------------")
    # print(x.prefix)
    # print("-------------------------------")
    # print(x.sourceline)
    # print("-------------------------------")
    # print(x.tag)
    # print("-------------------------------")
    # print(x.tail)
    # print("-------------------------------")
    # print(repr(x.text_content()))
    print("//////////////////////////////////////////////////////////////")
