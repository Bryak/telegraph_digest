import telepot
import yaml

from article_creator import create_article
from digest import load_posts


def send_boobs_to_chat(chat_id):
    config_name = 'prod.yml'
    token = yaml.load(open(config_name).read())['telegram']['token']
    bot = telepot.Bot(token)
    posts = load_posts(config_name, None)
    url = create_article(posts, config_name)
    bot.sendMessage(chat_id, url);  #//hehe


if __name__ == '__main__':
    send_boobs_to_chat('-1001052042617')
