import requests
import time
import matplotlib.pyplot as plt

PAGE_ACCESS_TOKEN = 'page_access_token_here'
INSTAGRAM_BUSINESS_ACCOUNT_ID = 'instagram_business_account_id_here'

def fetch_account_info():
    url = f'https://graph.facebook.com/v13.0/{INSTAGRAM_BUSINESS_ACCOUNT_ID}?fields=name,username,biography,followers_count,follows_count,media_count&access_token={PAGE_ACCESS_TOKEN}'
    response = requests.get(url)
    return response.json()

def fetch_recent_posts():
    url = f'https://graph.facebook.com/v13.0/{INSTAGRAM_BUSINESS_ACCOUNT_ID}/media?fields=id,caption,media_type,media_url,thumbnail_url,permalink,timestamp,like_count,comments_count&access_token={PAGE_ACCESS_TOKEN}'
    response = requests.get(url)
    return response.json()

def calculate_average_likes(recent_posts):
    total_likes = 0
    post_count = len(recent_posts['data'])

    for post in recent_posts['data']:
        total_likes += post['like_count']
    
    average_likes = total_likes / post_count
    return average_likes

def plot_likes(recent_posts):
    post_ids = [post['id'] for post in recent_posts['data']]
    like_counts = [post['like_count'] for post in recent_posts['data']]

    plt.plot(post_ids, like_counts)
    plt.xlabel('Post ID')
    plt.ylabel('Number of Likes')
    plt.title('Likes per Recent Post')
    plt.xticks(rotation=90)
    plt.grid()
    plt.show()

account_info = fetch_account_info()
print("Account Info:")
print(account_info)

time.sleep(5)

recent_posts = fetch_recent_posts()
print("\nRecent Posts:")

if 'data' in recent_posts:
    for post in recent_posts['data']:
        print(post)
    
    average_likes = calculate_average_likes(recent_posts)
    print(f"\nAverage likes per post: {average_likes:.2f}")
else:
    print("Error: Unable to fetch recent posts.")
    print("Full response:")
    print(recent_posts)

time.sleep(5)

plot_likes(recent_posts)