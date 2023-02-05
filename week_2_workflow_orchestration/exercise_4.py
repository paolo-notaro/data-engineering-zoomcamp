from prefect import flow, task
from prefect.filesystems import GitHub


def get_repository():
    github_block = GitHub.load("zoom-github-storage")
    code = github_block.get_directory("week_2_workflow_orchestration")
    code.save('homework4')
    

if __name__ == '__main__':
    get_repository()