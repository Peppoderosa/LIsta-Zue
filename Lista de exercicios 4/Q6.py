def duration(start, end):
    start = start.split(':')
    end = end.split(':')
    hStart = int(start[0])
    mStart = int(start[1])
    hEnd = int(end[0])
    mEnd = int(end[1])
    if hStart <= 23 and hEnd <= 23 and mStart <= 59 and mEnd <=59:
        totalH = 0
        totalM = 0
        if hStart < hEnd and mStart < mEnd:
            totalH = hStart - hEnd
            totalM = mStart - mEnd
        elif hStart > hEnd and mStart < mEnd:
            totalH = hEnd - hStart + 24
            totalM = (mStart - mEnd)
        elif hStart > hEnd and mStart > mEnd:
            totalH = hEnd - hStart + 23
            totalM = mEnd - mStart + 60
        elif hStart < hEnd and mStart > mEnd:
            totalH = hEnd - hStart - 1
            totalM = mEnd - mStart + 60
        elif hStart == hEnd and mStart < mEnd:
            totalH = 0
            totalM = mStart - mEnd
        elif hStart > hEnd and mStart == mEnd:
            totalH = hEnd - hStart + 24
            totalM = 0
        elif hStart == hEnd and mStart > mEnd:
            totalH = 23
            totalM = mEnd - mStart + 60
        elif hStart < hEnd and mStart == mEnd:
            totalH = hEnd - hStart
            totalM = 0

        if totalH < 0:
            totalH = totalH * -1
        if totalM < 0:
            totalM = totalM * -1

        return '{}:{}'.format(totalH, totalM)

    else:
        print('Erro')

#################################################

print(duration('22:35','6:18'))

