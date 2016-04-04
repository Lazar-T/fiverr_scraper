import requests
from lxml import html
from termcolor import colored

url = raw_input('> Enter profile url: ')

page = requests.get(url, verify=False)
tree = html.fromstring(page.content)

title = tree.xpath(
    '//h1/span/text()')[0].strip()

country = tree.xpath(
    '//small[contains(text(), "From")]/following-sibling::text()')[0].strip()

user_name = tree.xpath(
    '//span[@itemprop="name"]/text()')[0]

number_reviews = tree.xpath(
    '//h4[@itemprop="reviewCount"]/text()')[0]

percentage_rating = tree.xpath(
    '//small[contains(text(), "Positive Rating")]/following-sibling::text()')[0].strip()

average_rating = tree.xpath(
    '//span[@itemprop="ratingValue"]/text()')[0]

average_response = tree.xpath(
    '//small[contains(text(), "Avg. Response Time")]/following-sibling::text()')[0].strip()


profile_picture = 'https:' + tree.xpath(
    '//div[@itemprop="logo"]/a/img/@src')[0]

description = tree.xpath(
    '//*[@class="seller-desc"]/p/text()')[0]

print '\n'
print colored('Information from: ', 'red'), colored(url, 'green')
print colored('Title: ', 'red'), colored(title, 'green')
print colored('From: ', 'red'), colored(country, 'green')
print colored('User name: ', 'red'), colored(user_name, 'green')
print colored('Number of reviews: ', 'red'), colored(number_reviews, 'green')
print colored('Rating: ', 'red'), colored(percentage_rating, 'green')
print colored('Average rating: ', 'red'), colored(average_rating, 'green')
print colored('Average response time: ', 'red'), colored(average_response, 'green')
print colored('Profile image url: ', 'red'), colored(profile_picture, 'green')
print colored('Description: ', 'red'), colored(description, 'green')
