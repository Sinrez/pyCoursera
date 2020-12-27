def main():
    num_videos = int(input("Сколько видеоклипов в проекте" + '\n'))

    video_file = open('video_times.txt', 'w')

    print('введите длительность каждого видеоклипа' + '\n')
    for count in range(1, num_videos + 1):
        run_time = float(input('Видеоклип №' + str(count) + ': '))
        video_file.write(str(run_time) + '\n')

    video_file.close()
    print('Времена сохранены в video_times.txt')

main()
