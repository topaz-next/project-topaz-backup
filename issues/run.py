import os
import json
from github import Github

access_key = ""
old_repo_name = ""
new_repo_name = "topaz-next/topaz"

# =========================================================

g = Github(access_key)
#old_repo = g.get_repo(old_repo_name)
new_repo = g.get_repo(new_repo_name)

# =========================================================
def get_new_issue_body(issue):
    return f"""<a href="{issue['user_html_url']}"><img src="{issue['user_avatar_url']}" width="96" height="96" hspace="10"></img></a> **Issue by [{issue['user_login']}]({issue['user_html_url']})**
_{issue['created_at']}_
_Originally opened as: project-topaz/topaz - Issue {issue['number']}_

----

{issue['body'].replace('align="left"', '')}
"""

# =========================================================
def get_new_comment_body(comment):
    return f"""<a href="{comment['comment_user_html_url']}"><img src="{comment['comment_user_avatar_url']}" width="48" height="48" hspace="10"></img></a> **Comment by [{comment['comment_user_login']}]({comment['comment_user_html_url']})**
_{comment['created_at']}_

----

{comment['body'].replace('align="left"', '')}
"""

# TODO: Finish me
# =========================================================
def push_issue_to_new_repo(issue):
    # Clone issue
    new_issue = new_repo.create_issue(title=issue['title'],
                                      body=get_new_issue_body(issue))
    
    for label in issue['labels']:
        new_issue.add_to_labels(label)

    # Copy comments
    for comment in issue['comments']:
        new_issue.create_comment(get_new_comment_body(issue['comments'][str(comment)]))

    # Copy state
    new_issue.edit(state=issue['state'], labels=issue['labels'])


# =========================================================
def normalize_filename(fn):
    # https://stackoverflow.com/a/55101759/4600540
    validchars = "-_.() "
    out = ""
    for c in fn:
      if str.isalpha(c) or str.isdigit(c) or (c in validchars):
        out += c
      else:
        out += "_"
    return out   


# =========================================================
def save_issue_to_md(issue):
    if not os.path.exists('markdown'):
        os.makedirs('markdown')

    filename = 'markdown/{} - {} ({}).md'.format(issue['number'], normalize_filename(issue['title']), issue['state'])
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("**Labels:**\n\n")
        for label in issue['labels']:
            f.write("{}\n\n".format(label))
        f.write("\n\n")

        f.write(get_new_issue_body(issue))
        
        for comment in issue['comments']:
            f.write("\n\n")
            f.write("----\n")
            f.write(get_new_comment_body(issue['comments'][str(comment)]))


# =========================================================
def add_issue_to_json_data(data, issue):
    print("Add issue to JSON '{} - {} ({})'".format(issue.number, issue.title, issue.state))
    
    data[str(issue.number)] = {}
    data[str(issue.number)]['title'] = issue.title
    data[str(issue.number)]['number'] = issue.number
    data[str(issue.number)]['body'] = issue.body
    data[str(issue.number)]['created_at'] = issue.created_at.strftime('%A %b %d, %Y at %X')
    data[str(issue.number)]['state'] = issue.state
    data[str(issue.number)]['user_html_url'] = issue.user.html_url
    data[str(issue.number)]['user_avatar_url'] = issue.user.avatar_url
    data[str(issue.number)]['user_login'] = issue.user.login

    data[str(issue.number)]['labels'] = []
    for label in issue.get_labels():
        data[str(issue.number)]['labels'].append(label.name)

    data[str(issue.number)]['comments'] = {}
    for comment in issue.get_comments():
        data[str(issue.number)]['comments'][str(comment.id)] = {}
        data[str(issue.number)]['comments'][str(comment.id)]['body'] = comment.body
        data[str(issue.number)]['comments'][str(comment.id)]['created_at'] = comment.created_at.strftime('%A %b %d, %Y at %X')
        data[str(issue.number)]['comments'][str(comment.id)]['comment_user_html_url'] = comment.user.html_url
        data[str(issue.number)]['comments'][str(comment.id)]['comment_user_avatar_url'] = comment.user.avatar_url
        data[str(issue.number)]['comments'][str(comment.id)]['comment_user_login'] = comment.user.login


# =========================================================
def rebuild_from_json_data(data):
    issues = {}
    for issue_number in data:
        issue = {}
        issue['title'] = data[str(issue_number)]['title']
        issue['number'] = data[str(issue_number)]['number']
        issue['body'] = data[str(issue_number)]['body']
        issue['created_at'] = data[str(issue_number)]['created_at']
        issue['state'] = data[str(issue_number)]['state']
        issue['user_html_url'] = data[str(issue_number)]['user_html_url']
        issue['user_avatar_url'] = data[str(issue_number)]['user_avatar_url']
        issue['user_login'] = data[str(issue_number)]['user_login']

        issue['labels'] = []
        for n in range(len(data[str(issue_number)]['labels'])):
            issue['labels'].append(data[str(issue_number)]['labels'][n])

        issue['comments'] = {}
        for comment_id in data[str(issue_number)]['comments']:
            comment = {}
            comment['body'] = data[str(issue_number)]['comments'][comment_id]['body']
            comment['created_at'] = data[str(issue_number)]['comments'][comment_id]['created_at']
            comment['comment_user_html_url'] = data[str(issue_number)]['comments'][comment_id]['comment_user_html_url']
            comment['comment_user_avatar_url'] = data[str(issue_number)]['comments'][comment_id]['comment_user_avatar_url']
            comment['comment_user_login'] = data[str(issue_number)]['comments'][comment_id]['comment_user_login']
            issue['comments'][comment_id] = comment

        issues[issue_number] = issue

    return issues
    

# =========================================================
def main():
    data = {}

    # Test
    #save_issue_to_md(old_repo.get_issue(19))
    #add_issue_to_json_data(data, old_repo.get_issue(19))

    #for issue in old_repo.get_issues(state='all'):
    #    add_issue_to_json_data(data, issue)

    #with open('json_dump.txt', 'w') as json_file:
    #    json.dump(data, json_file)

    issues = {}
    with open('json_dump.txt', 'r') as json_file:
        issues = rebuild_from_json_data(json.load(json_file))

    keys = sorted(issues, key=lambda x: int(x))
    for key_number in keys:
        issue_obj = issues[str(key_number)]
        print("{} {}".format(issue_obj['number'], issue_obj['title']))
        push_issue_to_new_repo(issue_obj)

# =========================================================
if __name__ == "__main__":
    main()
