def insert_word(w_dict, word):
    word_len = len(word)
    if word_len in w_dict:
        w_dict[word_len][''][0] += 1
    else:
        w_dict[word_len] = {'': [1, {}]}
    next_dict = w_dict[word_len]
    for string in word:
        if string in next_dict:
            next_dict[string][0] += 1
        else:
            next_dict[string] = [1, {}]
        next_dict = next_dict[string][1]
    return w_dict


def find_word(w_dict, query, query_len):
    find_dict = w_dict[query_len]
    for string in query:
        if string in find_dict:
            ans = find_dict[string][0]
            find_dict = find_dict[string][1]
        elif string == '?':
            break
        else:
            ans = 0
            break
    return ans


def solution(words, queries):
    answer = []
    word_dict = {}
    reverse_word_dict = {}
    for word in words:
        word_dict = insert_word(word_dict, word)
        reverse_word = word[::-1]
        reverse_word_dict = insert_word(reverse_word_dict, reverse_word)
    print(word_dict)
    for query in queries:
        query_len = len(query)
        if query_len not in word_dict:
            answer.append(0)
            continue
        if query[0] == '?' and query[-1] == '?':
            if query_len in word_dict:
                answer.append(word_dict[query_len][''][0])
            else:
                answer.append(0)
        elif query[-1] == '?':
            answer.append(find_word(word_dict, query, query_len))
        else:
            answer.append(find_word(reverse_word_dict, query[::-1], query_len))

    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
               ["fro??", "????o", "fr???", "fro???", "pro?"]))

