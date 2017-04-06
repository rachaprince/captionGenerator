from application import db
from application import Contest
import csv
import codecs

with codecs.open('./cartoonDescriptions.csv', 'r') as csvfile:
  next(csvfile)
  for line in csvfile:
      args = [l.strip() for l in line.split(',')]
      encoded = [s.decode('utf8') for s in args]
      encoded += [None, None]
      contest = Contest(*encoded)
      db.session.add(contest)

db.session.commit()

contests = Contest.query.all()
print len(contests)
