import json
from pathlib import Path

from .sched.executor import QuarkExecutor, FakeExecutor
from .sched.sched import bootstrap as _bootstrap

etc = Path(__file__).parent.parent / 'etc'


def bootstrap(config_path: str = etc / 'bootstrap.json'):
    if not config_path.exists():
        config_path = etc / 'bootstrap.json.sample'

    with open(config_path) as f:
        config = json.load(f)

    if config['executor']['type'] == 'debug':
        with open(config['executor']['path']) as f:
            executor = FakeExecutor(json.load(f))
    else:
        executor = QuarkExecutor(config['executor']['host'])
    if config['data']['path'] == '':
        datapath = Path.home() / 'data'
        datapath.mkdir(parents=True, exist_ok=True)
    else:
        datapath = Path(config['data']['path'])
    if config['data']['url'] == '':
        url = None
    else:
        url = config['data']['url']
    repo = config.get('repo', None)

    _bootstrap(executor, url, datapath, repo)
