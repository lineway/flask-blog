# coding:utf-8
__author__ = "piels"

import datetime
import random

from faker import Faker

from webapp.main import db, User, Tag, Post
fake = Faker()

user = User.query.get(1)

tag_one = Tag('jinja')
tag_two = Tag('python')
tag_three = Tag('flask')

tag_list = [tag_one, tag_two, tag_three]

for i in xrange(100):
    new_post = Post(fake.company())
    new_post.user = user
    new_post.publish_date = datetime.datetime.now()
    new_post.text = fake.text()
    new_post.tags = random.sample(tag_list, random.randint(0,3))
    db.session.add(new_post)
db.session.commit()