import json
import dev_api


def show_data():
    response = dev_api.user_article()
    data = json.loads(response.text)

    for post in data:
        print('=============================')
        print(post['title'])
        print('=============================')
        print("ID: ", post['id'])
        print("\n---------------------------------")

        print("Published: ", post['published'])
        print("Publishing date: ", post['published_at'])
        print("Tags used: ", post['tag_list'])
        print("\n--------------------------------")

        print("Total views: ", post['page_views_count'])
        print("Total reactions: ", post['positive_reactions_count'])
        print("Total comments: ", post['comments_count'])
        print("\n--------------------------------")

        print("Short description: ", post['description'])
        print("Link to the post: ", post['url'])

        print('\n\n')

def show_feed():
    response = dev_api.feed()
    data = json.loads(response.text)

    for post in data:
        print('=====================================')
        print("Title: ", post['title'])
        print("Tags list: ", post['tag_list'])
        print("Published date: ", post['readable_publish_date'])
        print("Short description: ", post['description'])
        print("Link to the post: ", post['url'])
        print('\n\n')

def list_all():
    response = dev_api.user_article()
    data = json.loads(response.text)

    print("[ID] [Published] [Title] [Views] [Comments] [Reactions] [PublishedDate]")
    for post in data:
        title = post['title']
        ids = post['id']
        views = post['page_views_count']
        comments = post['comments_count']
        reactions = post['positive_reactions_count']
        status = post['published']
        date = post['published_at']
        try:
            date = date.split('T')
            date = date[0]
        except Exception:
            pass

        print(f"[{ids}] [{status}] [{title}] [{views}] [{comments}] [{reactions}] [{date}]")

def show_data_singe():
    ids = int(input("Enter the post ID >>> "))
    response = dev_api.user_article()
    data = json.loads(response.text)

    found = False

    for post in data:
        if post['id'] == ids:
            found = True

            print('=============================')
            print(post['title'])
            print('=============================')
            print("ID: ", post['id'])
            print("\n---------------------------------")

            print("Published: ", post['published'])
            print("Publishing date: ", post['published_at'])
            print("Tags used: ", post['tag_list'])
            print("\n--------------------------------")

            print("Total views: ", post['page_views_count'])
            print("Total reactions: ", post['positive_reactions_count'])
            print("Total comments: ", post['comments_count'])
            print("\n--------------------------------")

            print("Short description: ", post['description'])
            print("Link to the post: ", post['url'])

            print('\n\n')

            break

    if found == False:
        print('No matching post for the ID you mentioned')
