class Solution:
    def groupAnagrams(self, strs):
        """
        Groups a list of strings into anagrams.

        Parameters:
        strs (list): A list of strings to be grouped.

        Returns:
        list: A list of lists, where each inner list contains strings that are anagrams of each other.
        """

        result = {}
        for i in strs:
            # Sort the characters in the string and join them into a new string
            x = "".join(sorted(i))
            if x in result:
                result[x].append(i)
            else:
                result[x] = [i]
        return list(result.values())

# Example usage
ob1 = Solution()
print(ob1.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
