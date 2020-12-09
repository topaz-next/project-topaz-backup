import os
import json
from github import Github

access_key = ""
old_repo_name = ""
new_repo_name = ""

# =========================================================

g = Github(access_key)
old_repo = g.get_repo(old_repo_name)
new_repo = g.get_repo(new_repo_name)

# =========================================================
def get_new_pr_body(pr):
    return f"""<a href="{pr['user_html_url']}"><img src="{pr['user_avatar_url']}" width="96" height="96" hspace="10"></img></a> **Issue by [{pr['user_login']}]({pr['user_html_url']})**
_{pr['created_at']}_
_Originally opened as: project-topaz/topaz - Issue {pr['number']}_

----

{pr['body'].replace('align="left"', '')}
"""

# =========================================================
def get_new_comment_body(comment):
    return f"""<a href="{comment['comment_user_html_url']}"><img src="{comment['comment_user_avatar_url']}" width="48" height="48" hspace="10"></img></a> **Comment by [{comment['comment_user_login']}]({comment['comment_user_html_url']})**
_{comment['created_at']}_

----

{comment['body'].replace('align="left"', '')}
"""


# =========================================================
def normalize_filename(fn):
    # https://stackoverflow.com/a/55101759/4600540
    validchars = "-_() "
    out = ""
    for c in fn:
      if str.isalpha(c) or str.isdigit(c) or (c in validchars):
        out += c
      else:
        out += "_"
    return out.strip()


# =========================================================
def save_pr_to_md(pr):
    if not os.path.exists('markdown'):
        os.makedirs('markdown')

    short_name = ""
    if len(pr['title']) < 25:
        short_name = pr['title']
    else:
        short_name = pr['title'][0:24]

    short_name = normalize_filename(short_name)

    filename = 'markdown/{} - {}'.format(pr['number'], short_name)
    if not os.path.exists(filename):
        os.makedirs(filename)
    
    with open(filename + "/{} - {} ({}).md".format(pr['number'], short_name, pr['state']), 'w', encoding='utf-8') as f:
        f.write("**Labels:**\n\n")
        for label in pr['labels']:
            f.write("{}\n\n".format(label))
        f.write("\n\n")

        f.write(get_new_pr_body(pr))
        
        for comment in pr['comments']:
            f.write("\n\n")
            f.write("----\n")
            f.write(get_new_comment_body(pr['comments'][str(comment)]))

        for comment in pr['review_comments']:
            f.write("\n\n")
            f.write("----\n")
            f.write(get_new_comment_body(pr['review_comments'][str(comment)]))

        for comment in pr['issue_comments']:
            f.write("\n\n")
            f.write("----\n")
            f.write(get_new_comment_body(pr['issue_comments'][str(comment)]))

    for pr_file in pr['files']:
        with open(filename + "/{}".format(normalize_filename(pr['files'][str(pr_file)]['filename'])), 'w', encoding='utf-8') as f:
            if pr['files'][str(pr_file)]['patch']:
                f.write(pr['files'][str(pr_file)]['patch'])

    with open(filename + "/commits.md", 'w', encoding='utf-8') as f:
        for commit in pr['commits']:
            f.write("{} - {} ({}) - {} ({}) - {}\n".format(pr['commits'][str(commit)]['sha'],
                                                           pr['commits'][str(commit)]['author'],
                                                           pr['commits'][str(commit)]['author_email'],
                                                           pr['commits'][str(commit)]['committer'],
                                                           pr['commits'][str(commit)]['committer_email'],
                                                           pr['commits'][str(commit)]['html_url']))


# =========================================================
def add_pr_to_json_data(data, pr):
    print("Add PR to JSON '{} - {} ({})'".format(pr.number, pr.title, pr.state))
    
    data[str(pr.number)] = {}
    data[str(pr.number)]['title'] = pr.title
    data[str(pr.number)]['number'] = pr.number
    data[str(pr.number)]['body'] = pr.body
    data[str(pr.number)]['created_at'] = pr.created_at.strftime('%A %b %d, %Y at %X')
    data[str(pr.number)]['state'] = pr.state
    data[str(pr.number)]['user_html_url'] = pr.user.html_url
    data[str(pr.number)]['user_avatar_url'] = pr.user.avatar_url
    data[str(pr.number)]['user_login'] = pr.user.login

    data[str(pr.number)]['labels'] = []
    for label in pr.get_labels():
        data[str(pr.number)]['labels'].append(label.name)

    data[str(pr.number)]['commits'] = {}
    for commit in pr.get_commits():
        data[str(pr.number)]['commits'][str(commit.sha)] = {}
        if commit.author:
            data[str(pr.number)]['commits'][str(commit.sha)]['author'] = commit.author.name or ""
            data[str(pr.number)]['commits'][str(commit.sha)]['author_email'] = commit.author.email or ""
        else:
            data[str(pr.number)]['commits'][str(commit.sha)]['author'] = ""
            data[str(pr.number)]['commits'][str(commit.sha)]['author_email'] = ""
        
        if commit.committer:
            data[str(pr.number)]['commits'][str(commit.sha)]['committer'] = commit.committer.name or ""
            data[str(pr.number)]['commits'][str(commit.sha)]['committer_email'] = commit.committer.email or ""
        else:
            data[str(pr.number)]['commits'][str(commit.sha)]['committer'] = ""
            data[str(pr.number)]['commits'][str(commit.sha)]['committer_email'] = ""

        data[str(pr.number)]['commits'][str(commit.sha)]['sha'] = commit.sha or ""
        data[str(pr.number)]['commits'][str(commit.sha)]['html_url'] = commit.html_url or ""

    data[str(pr.number)]['comments'] = {}
    for comment in pr.get_comments():
        data[str(pr.number)]['comments'][str(comment.id)] = {}
        data[str(pr.number)]['comments'][str(comment.id)]['body'] = comment.body
        data[str(pr.number)]['comments'][str(comment.id)]['created_at'] = comment.created_at.strftime('%A %b %d, %Y at %X')
        data[str(pr.number)]['comments'][str(comment.id)]['comment_user_html_url'] = comment.user.html_url
        data[str(pr.number)]['comments'][str(comment.id)]['comment_user_avatar_url'] = comment.user.avatar_url
        data[str(pr.number)]['comments'][str(comment.id)]['comment_user_login'] = comment.user.login

    data[str(pr.number)]['review_comments'] = {}
    for comment in pr.get_review_comments():
        data[str(pr.number)]['review_comments'][str(comment.id)] = {}
        data[str(pr.number)]['review_comments'][str(comment.id)]['body'] = comment.body
        data[str(pr.number)]['review_comments'][str(comment.id)]['created_at'] = comment.created_at.strftime('%A %b %d, %Y at %X')
        data[str(pr.number)]['review_comments'][str(comment.id)]['comment_user_html_url'] = comment.user.html_url
        data[str(pr.number)]['review_comments'][str(comment.id)]['comment_user_avatar_url'] = comment.user.avatar_url
        data[str(pr.number)]['review_comments'][str(comment.id)]['comment_user_login'] = comment.user.login

    data[str(pr.number)]['issue_comments'] = {}
    for comment in pr.get_issue_comments():
        data[str(pr.number)]['issue_comments'][str(comment.id)] = {}
        data[str(pr.number)]['issue_comments'][str(comment.id)]['body'] = comment.body
        data[str(pr.number)]['issue_comments'][str(comment.id)]['created_at'] = comment.created_at.strftime('%A %b %d, %Y at %X')
        data[str(pr.number)]['issue_comments'][str(comment.id)]['comment_user_html_url'] = comment.user.html_url
        data[str(pr.number)]['issue_comments'][str(comment.id)]['comment_user_avatar_url'] = comment.user.avatar_url
        data[str(pr.number)]['issue_comments'][str(comment.id)]['comment_user_login'] = comment.user.login

    data[str(pr.number)]['files'] = {}
    for pr_file in pr.get_files():
        data[str(pr.number)]['files'][str(pr_file.filename)] = {}
        data[str(pr.number)]['files'][str(pr_file.filename)]['filename'] = pr_file.filename
        data[str(pr.number)]['files'][str(pr_file.filename)]['patch'] = pr_file.patch
        data[str(pr.number)]['files'][str(pr_file.filename)]['sha'] = pr_file.sha
        data[str(pr.number)]['files'][str(pr_file.filename)]['status'] = pr_file.status

    return data[str(pr.number)]


# =========================================================
def main():
    data = {}

    # Test
    #pr = old_repo.get_pull(1208)
    #pr_object = add_pr_to_json_data(data, pr)
    #save_pr_to_md(pr_object)

    for pr in old_repo.get_pulls(state='all'):
        # Track Progress (rate limiting)
        if pr.number < 483:
            pr_object = add_pr_to_json_data(data, pr)
            save_pr_to_md(pr_object)


# =========================================================
if __name__ == "__main__":
    main()
