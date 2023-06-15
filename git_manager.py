import os 
import openai
from git import Repo
from pathlib import Path

openai.api_key = os.getenv("OPENAI_API_KEY")

PATH_TO_REPO = Path(r'C:\Users\pbolduc2354\Desktop\blogGeneratorAI\pbolduc2354.github.io\.git')
PATH_TO_BLOG = PATH_TO_REPO.parent
PATH_TO_CONTENT = PATH_TO_BLOG / 'content'
PATH_TO_CONTENT.mkdir(exist_ok=True, parents=True)


def update_blog(commit_message='Updates blog'):
    repo = Repo(PATH_TO_REPO)
    repo.git.add(all=True)
    repo.index.commit(commit_message)
    origin = repo.remote(name='origin')
    origin.push()

random_text_string = 'ldlfkjahlfkjhad'


if __name__ == '__main__':  

    with open(PATH_TO_BLOG/'index.html', 'w') as f:
        f.write(random_text_string)

    update_blog(commit_message='Updates blog')