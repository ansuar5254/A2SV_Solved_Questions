class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        flipped_image = []
        n = len(image)
        m = len(image[0])
        for i in range(n):
            image[i].reverse()

        for i in range(n):
            for j in range(m):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        return image
                        
