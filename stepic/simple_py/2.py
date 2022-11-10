commands = 'git push origin main'.split()

for command in commands:
    match command.split():
        case 'git', 'add', path:
            print(f'В индекс добавлены файлы по пути: {path}.')
        case 'git', 'commit':
            print('Файлы закоммичены.')
        case 'git', 'commit', '-m', message:
            print(f'Файлы закоммичены с сообщением {message}')
        case 'git', 'push', repository, branch:
            print(f'Файлы запушены в {repository} в ветку {branch}.')
        case _:
            print('Неизвестная команда.')