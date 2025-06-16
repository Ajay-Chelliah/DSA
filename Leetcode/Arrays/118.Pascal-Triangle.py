class Solution:
    def generate(self, numRows: int):
        ans = []
        for row in range(1, numRows + 1):
            ans.append(self.generateRow(row))
        return ans

    def generateRow(self, row):
        ans = 1
        ansRow = [1]  # inserting the 1st element

        # calculate the rest of the elements:
        for col in range(1, row):
            ans *= row - col
            ans //= col
            ansRow.append(ans)
        return ansRow
