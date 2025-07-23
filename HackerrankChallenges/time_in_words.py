def timeInWords(hours: int, minutes: int) -> str:
    time = {1: 'one', 2: 'two', 3: 'three', 4: 'four',
            5: 'five', 6: 'six', 7: 'seven', 8: ' eight',
            9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
            13: 'thirteen', 14: 'fourteen', 15: 'quarter', 16: 'sixteen',
            17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: "twenty", 30: "half"}
    min_words = str(minutes)

    if 0 < minutes <= 30:
        if minutes == 1:
            s = time[int(min_words)]
            return s + " minute past " + time[hours]
        if minutes == 30:
            s = time[int(min_words)]
            return s + " past " + time[hours]
        if int(min_words) <= 20:
            s = time[int(min_words)]
            return s + " past " + time[hours] if s == 'quarter' else s + " minutes past " + time[hours]
        else:
            return time[20] + " " + time[int(min_words[1])] + " minutes past " + time[hours]
    elif minutes > 30:
        word = str(60 - minutes)
        if int(word) > 20:
            return time[20] + " " + time[int(word[1])] + ' minutes to ' + time[hours+1]
        s = time[60 - minutes]
        if s == 'quarter':
            return s + " to " + time[hours+1]
        else:
            return s + " minutes to " + time[hours+1]

    else:
        return time[hours] + " o' clock"


if __name__ == '__main__':
    h = int(input())
    m = int(input())

    answer = timeInWords(h, m)
    print(answer)
