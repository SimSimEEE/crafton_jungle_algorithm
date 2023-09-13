def solution(m, musicinfos):
    answer = '(None)'
    musics = {}

    def replace_sharp(melody):
        melody = melody.replace("C#", "c").replace("D#", "d").replace("E#", "e").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        return melody

    m = replace_sharp(m)

    for musicinfo in musicinfos:
        music = musicinfo.split(",")
        start_time = int(music[0][:2]) * 60 + int(music[0][3:5])
        end_time = int(music[1][:2]) * 60 + int(music[1][3:5])
        time_diff = end_time - start_time
        melody = replace_sharp(music[3])

        full_melody = melody * (time_diff // len(melody)) + melody[:time_diff % len(melody)]
        musics[music[2]] = [time_diff, full_melody]

    sorted_dict = sorted(musics.items(), key=lambda item: item[0])

    for name, mel in musics.items():
        if m in mel[1]:
            if answer == '(None)' or musics[answer][0] < mel[0]:
                answer = name

    return answer