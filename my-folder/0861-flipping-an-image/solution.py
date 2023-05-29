class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        m = len(image[0])

        for i in range(0, n):
            image[i] = image[i][::-1]

            for j in range(0, m):
                if image[i][j] == 1:
                    image[i][j] = 0
                else:
                    image[i][j] = 1
        return image
