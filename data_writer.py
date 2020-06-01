import csv
import json
import dev_api


def csv_writer():
    response = dev_api.user_article()
    data = json.loads(response.text)
    with open('data.csv', mode='w') as file:
        fields = ['Title', 'ID', 'Tags', 'Views', 'Comments', 'Reactions', 'Date', 'Status']
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()

        for post in data:
            row = {
                'Title': post['title'],
                'ID': post['id'],
                'Tags': post['tag_list'],
                'Views': post['page_views_count'],
                'Comments': post['comments_count'],
                'Reactions': post['positive_reactions_count'],
                'Date': post['published_at'],
                'Status': post['published']
            }

            writer.writerow(row)
