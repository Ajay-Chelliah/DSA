class Solution:
    # Function to find the maximum number of meetings that can
    # be performed in a meeting room.
    def maximumMeetings(self, start, end):
        n = len(start)
        meetings = [(start[i], end[i]) for i in range(n)]
        meetings.sort(key=lambda x: x[1])
        sum = 1
        limit = meetings[0][1]
        for i in range(1, n):
            if meetings[i][0] > limit:
                sum += 1
                limit = meetings[i][1]
        return sum
