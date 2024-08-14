def count_words(lines: list[str]):
    words = {}
    for line in lines:
        _word, _, match_count, _ = line.split("\t")
        if _word in words:
            words[_word] += int(match_count)
        else:
            words[_word] = int(match_count)
    return words


def mp_count_words(lines: list[str], counter, lock):
    # words_num = 0
    # step = 100
    words = {}
    for line in lines:
        _word, _, match_count, _ = line.split("\t")
        if _word in words:
            words[_word] += int(match_count)
        else:
            words[_word] = int(match_count)

        # monitoring
        # because of lock, this can slow down processing time
        #
        # words_num += 1
        # if words_num % step == 0:
        #     words_num = 0
        #         counter.value += step

    with lock:
        counter.value += len(lines)
    return words
