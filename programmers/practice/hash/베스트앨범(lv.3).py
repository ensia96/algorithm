def solution(genres, plays):
    '''
    input
        - genres : [노래의 장르] (1 <= [] <= 10,000, 종류 < 100)
        - plays  : [재생된 횟수] (len(genres))
    output
        - answer : [곡 고유번호]
    result
        - 정확성 : 100/100
    '''
    answer      = []
    genre_table = {}
    
    for song, play in enumerate(plays):
        genre = genres[song]
        if genre not in genre_table:
            genre_table[genre] = {}
            genre_table[genre]['plays'] = 0
            genre_table[genre]['songs'] = []

        genre_table[genre]['plays'] += play
        genre_table[genre]['songs'].append(song)

    sorted_list = sorted(genre_table.values(), key=lambda x: x['plays'], reverse=True)

    for genre in sorted_list:
        answer.extend(sorted(genre['songs'], key=lambda x: plays[x], reverse=True)[:2])

    return answer

print(solution(
    ["classic", "pop", "classic", "classic", "pop"],
    [500, 600, 150, 800, 2500]
)) # [4, 1, 3, 0]
