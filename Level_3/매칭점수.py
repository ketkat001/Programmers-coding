import re


def solution(word, pages):
    answer = 999
    url_idx = {}
    url_score = {}
    url_link = {}
    url_list = []
    word = word.lower()
    for i in range(len(pages)):
        temp = pages[i].lower()
        url = re.search(r'<meta[^>]*content="https://([\S]*)"/>', temp).group(1)  # url 이름
        url_idx[url] = i
        url_list.append(url)

        link_site = set()  # url 링크
        for site in re.findall(r'<a href="https://[\S]*">', temp):
            link_site.add(re.search(r'<a href="https://([\S]*)"', site).group(1))
        url_link[url] = list(link_site)

        cnt = 0  # url 기본 점수
        for find_word in re.findall(r'[a-zA-Z]+', temp):
            if find_word == word:
                cnt += 1
        url_score[url] = [cnt]
    for url in url_list:
        link_site_list = url_link[url]
        for link in link_site_list:
            if link in url_list:
                url_score[link].append(url_score[url][0]/len(link_site_list))

    for url in url_list:
        url_score[url] = sum(url_score[url])

    max_value_url = [key for key, value in url_score.items() if max(url_score.values()) == value]

    for url in max_value_url:
        temp = url_idx[url]
        if answer > temp:
            answer = temp

    return answer


print(solution("blind", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
print(solution("Muzi", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))