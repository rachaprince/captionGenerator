from application import db
from application import Contest
import csv

with open('./cartoonDescriptions.csv', 'r') as csvfile:
  next(csvfile)
  for line in csvfile:
      args = [l.strip() for l in line.split(',')]
      try:
        encoded = [s.encode('utf8') for s in args]
        print encoded
        exit()
        contest = Contest(*encoded)
        db.session.add(contest)
      except:
        continue

db.session.commit()
